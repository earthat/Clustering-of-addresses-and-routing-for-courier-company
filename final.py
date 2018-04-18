"""
This file cluster the data. the input used is teh co-ordinates from the csv file which is saved after
extraction from geo.py
"""

import numpy as np
import googlemaps
import pandas as pd
import simplejson, urllib
import csv
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from geopy.distance import great_circle
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
from mapAPI import GoogleStaticMapsAPI
from io import BytesIO
import requests
from PIL import Image
from matplotlib import pyplot as plt
import math


# ##########Distance calculation in a cluster using google map api   ###############################

def calcDist(coordinates,gmaps):
    geocode_result_depot = gmaps.geocode('64 Pound road West Dandenong South, Australia')[0]  # depot address
    lat_depot = (geocode_result_depot['geometry']['location']['lat'])
    lng_depot = (geocode_result_depot['geometry']['location']['lng'])
    # result.append(lat_depot,lng_depot)
    np.append([lat_depot, lng_depot], coordinates)
    dist = np.zeros(
        (np.size(coordinates, 0), np.size(coordinates, 0)))  # create an empty matrix for dsiatnce between all locations

    for index in range(0, np.size(coordinates, 0)):
        src = coordinates[index]

        for ind in range(0, np.size(coordinates, 0)):
            dst = coordinates[ind]
            dist[index,ind]=distance(src[0],src[1],dst[0],dst[1])

    return dist

def distance(lat1, long1, lat2, long2):
    # Note: The formula used in this function is not exact, as it assumes
    # the Earth is a perfect sphere.

    # Mean radius of Earth in miles
    radius_earth = 3959

    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
    phi1 = lat1 * degrees_to_radians
    phi2 = lat2 * degrees_to_radians
    lambda1 = long1 * degrees_to_radians
    lambda2 = long2 * degrees_to_radians
    dphi = phi2 - phi1
    dlambda = lambda2 - lambda1

    a = haversine(dphi) + math.cos(phi1) * math.cos(phi2) * haversine(dlambda)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius_earth * c
    return d

def haversine(angle):
  h = math.sin(angle / 2) ** 2
  return h


# Distance callback
class CreateDistanceCallback(object):
  """Create callback to calculate distances between points."""
  def __init__(self,dist):
    """Array of distances between points."""

    self.matrix = dist

  def Distance(self, from_node, to_node):
    return self.matrix[from_node][to_node]
# ####Route Optimisation function in a cluster form depot to depot ########################################
def routeOptimisation(dist,address):
    # Delivery locations

    city_names=address.tolist()
    city_names.insert(0, "64 Pound road West Dandenong South, Australia")

    tsp_size = len(city_names)-1
    num_routes = 1  # The number of routes, which is 1 in the TSP.
    # Nodes are indexed from 0 to tsp_size - 1. The depot is the starting node of the route.
    depot = 0

    # Create routing model
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()

        # Setting first solution heuristic: the
        # method for finding a first solution to the problem.
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        dist_between_nodes = CreateDistanceCallback(dist)
        dist_callback = dist_between_nodes.Distance
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)

        # Solve, returns a solution if any.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            # Solution cost.
            print("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
            # Inspect solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
            route_number = 0
            index = routing.Start(route_number)  # Index of the variable for the starting node.
            route = ''
            while not routing.IsEnd(index):
                # Convert variable indices to node indices in the displayed route.
                route += str(city_names[routing.IndexToNode(index)]) + ' -> '
                index = assignment.Value(routing.NextVar(index))
            route += str(city_names[routing.IndexToNode(index)])
            print("Route:\n\n" + route)
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')

# ####### main function      ################################################
def main():
    results = []
    labels=[]
    gmaps = googlemaps.Client(key='AIzaSyDQWvqAqdRZNoTDtOXZUAuvF21LmXPtIfE')

    #df = pd.read_csv('coordinates.csv')                         #read the co-ordinates csv
    df = pd.read_csv("data3.csv")
    df['lat'] = pd.Series(np.repeat(0, df.size),dtype=float)
    df['long'] = pd.Series(np.repeat(0, df.size),dtype=float)


    a = (df.as_matrix())

    result = np.zeros([df.size, 2])
    for index, row in df.iterrows():
        # print(row['Address'])
        geocode_result = gmaps.geocode(row['Address'])[0]
        lat = (geocode_result['geometry']['location']['lat'])
        lng = (geocode_result['geometry']['location']['lng'])
        result[index] = lat, lng
        print(result[index])
        df.lat[index]=lat
        df.long[index]=lng

    coords = df.as_matrix(columns=['lat', 'long'])

    print('************************ DBSCAN Starts Here*******************************************8')

    DB = DBSCAN(eps=0.0005, min_samples=3, metric='haversine',         #DSCAN Algorithm
          metric_params=None, algorithm='ball_tree',
          leaf_size=30, p=None, n_jobs=1).fit(np.radians(coords))
    core_samples_mask = np.zeros_like(DB.labels_, dtype=bool)
    core_samples_mask[DB.core_sample_indices_] = True
    DBSCANsPrediction=DB.labels_
    print('DBscanlabels= ',DB.labels_)

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(DBSCANsPrediction)) - (1 if -1 in DBSCANsPrediction else 0)
    unique_labels = set(DBSCANsPrediction)
    unique_value = np.unique(DBSCANsPrediction)          # find out the total unique labels

    ######### Plot the Markers on google static map #################

    df['color'] = pd.Series(np.repeat('black', np.size(DBSCANsPrediction)))  # make a color column in the
    colr = (['red', 'green', 'blue', 'black', 'purple', 'yellow','orange','brown','gray'])
    for i in range(0, np.size(unique_value)):
        df.color[DBSCANsPrediction == unique_value[i]] = colr[i]

    url = GoogleStaticMapsAPI.urlConstruct(markers=df.T.to_dict().values(),
                                           zoom=8, center='64 Pound road West Dandenong South, Australia')
    #print(url)
    img = Image.open(BytesIO((requests.get(url).content)))
    plt.figure(1, figsize=(5, 5))
    plt.imshow(np.array(img))  # Background map
    plt.title('DBSCAN clustered')
    plt.axis('off')
    plt.tight_layout()


    for k in zip(unique_labels):
        clas=DBSCANsPrediction==k
        cluster1=coords[clas & core_samples_mask]
        address=df.Address[clas & core_samples_mask]
        #print(np.size(cluster1,0))
        dist=calcDist(cluster1,gmaps)                 # calculate the distance between cluster nodes
        print(['========== DBSCAN Cluster ',str(k), 'results =================================='])
        routeOptimisation(dist,address)              #optimise the route from depot to delivery locatiosn and back to depot

    ###============ Kmeans Algorithm ==========================##
    print('************************ Kmeans Starts Here*******************************************')
    kmeans = KMeans(n_clusters=5, init='k-means++',            #kmeans algorithm
                n_init=10, max_iter=300, tol=0.0001,
                precompute_distances=True, verbose=0,
                random_state=None, copy_x=True, n_jobs=1,
                algorithm='auto').fit(coords)
    PredictedCluster=kmeans.labels_
    print('Kmeanslabels= ', kmeans.labels_)
    unique_labels_kmeans = set(PredictedCluster)
    unique_value = np.unique(PredictedCluster)          # find out the total unique labels
    ######### Plot the Markers on google static map #################

    df['color'] = pd.Series(np.repeat('black', np.size(PredictedCluster)))  # make a color column in the
    colr = (['red', 'green', 'blue', 'black', 'purple', 'yellow','orange','brown','gray'])
    for i in range(0, np.size(unique_value)):
        df.color[PredictedCluster == unique_value[i]] = colr[i]

    url = GoogleStaticMapsAPI.urlConstruct(markers=df.T.to_dict().values(),
                                           zoom=8, center='64 Pound road West Dandenong South, Australia')
    #print(url)
    img = Image.open(BytesIO((requests.get(url).content)))
    plt.figure(2, figsize=(5, 5))
    plt.imshow(np.array(img))  # Background map
    plt.title('Kmeans clustered')
    plt.axis('off')
    plt.tight_layout()
    for i in zip(unique_labels_kmeans):
        #print(i)
        clas=PredictedCluster==i
        kmeans_cluster=coords[clas]
        address = df.Address[clas ]
        dist = calcDist(kmeans_cluster, gmaps)  # calculate the distance between cluster nodes
        print(['========== kmeans Cluster ', str(i), 'results =================================='])
        routeOptimisation(dist,address)  # optimise the route from depot to delivery locatiosn and back to depot

    print('************************ Original label plotting**************')
    """with open("truelabel.csv") as csvfile1:                     # read the original clusters
           reader=csv.reader(csvfile1,quoting=csv.QUOTE_ALL)
           for row in reader:
               labels.append(row)"""
    labeldf = pd.read_csv("truelabel.csv")
    labels = labeldf['Original']
    print('Original labels= ', labels)
    #unique_labels_original = set(labels)

    unique_value = np.unique(labels)  # find out the total unique labels
    ######### Plot the Markers on google static map #################

    df['color'] = pd.Series(np.repeat('black', np.size(labels)))  # make a color column in the
    colr = (['red', 'green', 'blue', 'black', 'purple', 'yellow', 'orange', 'brown', 'gray'])
    for i in range(0, np.size(unique_value)):
        df.color[labels == unique_value[i]] = colr[i]

    url = GoogleStaticMapsAPI.urlConstruct(markers=df.T.to_dict().values(),
                                           zoom=8, center='64 Pound road West Dandenong South, Australia')
    # print(url)
    img = Image.open(BytesIO((requests.get(url).content)))
    plt.figure(3, figsize=(5, 5))
    plt.imshow(np.array(img))  # Background map
    plt.title('Original clustered')
    plt.axis('off')
    plt.tight_layout()
    for i in range(0, np.size(unique_value)):
        # print(i)
        clas = labels == unique_value[i]
        original_cluster = coords[clas]
        address = df.Address[clas]
        dist = calcDist(original_cluster, gmaps)  # calculate the distance between cluster nodes
        print(['========== Original Cluster ', str(unique_value[i]), 'results =================================='])
        routeOptimisation(dist, address)  # optimise the route from depot to delivery locatiosn and back to depot

    plt.show()

# #########################################################################
if __name__ == '__main__':
  main()



