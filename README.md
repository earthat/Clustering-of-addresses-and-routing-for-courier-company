# Clustering of addresses and routing for courier company
The delivery cost of a courier company can be reduced by geographical clustering of addresses in desired number of clusters dpeending upon the courier boys availablity. This code is using two different clustering algorithm for comparison purpose: kmeans, DBSCAN. DBSCAN is suitable clustering approach for the geographical clustering. The actual geographical distance is calculated by using gogle map API since we have addresses of dleivery locatiosn, we fetched the co-ordinates from google map and calculated the distance. Based on this distance optimal routing for courier boy is planned in every cluster. For the provided data the following were formed geographical clusters by kmeans and DBSCAN. The clusters are formed as
![figure_1](https://github.com/earthat/Clustering-of-addresses-and-routing-for-courier-company/blob/master/Results/Figure_1.png)

```************************ DBSCAN Starts Here*******************************************8
DBscanlabels=  [-1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 -1 -1 -1
  1 -1  1 -1 -1 -1 -1 -1 -1  2  1  1  2  2 -1  2  2  1 -1  0  0  0  0  0  0
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 -1  3  4 -1  5  4  4  4  5
  5 -1  3 -1  3  4  3  5  3  6  6  6  6  4]
 ['========== DBSCAN Cluster ', '(0,)', 'results ==================================']
Total distance: 16 miles

Route:

64 Pound road West Dandenong South, Australia -> 217 PRINCES HIGHWAYDANDENONG,3175Australia -> 19 TURNER CTANDENONG,3175Australia -> 1449 Heatherton Road DandenongDANDENONG,3175Australia -> 7 Robyn CourtDANDENONG NORTH,3175Australia -> 10 Glenelg streetDANDENONG NORTH,3175Australia -> 234 HIGH STREETASHBURTON,3147Australia -> 215/207-219 Browns RoadNOBLE PARK,3174Australia -> 10 JONATHAN COURTNOBLE PARK,3174Australia -> 28 GUNTHER AVENUESPRINGVALE,3171Australia -> 785 PRINCES HWYSPRINGVALE,3171Australia -> UNIT 36/632 CLAYTON ROADCLAYTON,3168Australia -> 31-35 Bendix DriveCLAYTON SOUTH,3169Australia -> 1418A CENTRE RDCLAYTON,3168Australia -> 81-83 Fairbank RdCLAYTON SOUTH,3169Australia -> 224 FERNTREE GULLYNOTTING HILL,3168Australia -> 28 Haughton RoadOAKLEIGH,3166Australia -> 1/2A COORA RDOAKLEIGH SOUTH,3167Australia -> 27 Clarinda RoadOAKLEIGH SOUTH,3167Australia -> 2 / 45 Bunney RoadCLARINDA,3169Australia -> 1090 Centre RdOAKLEIGH SOUTH,3167Australia -> 43 George StreetOAKLEIGH,3166Australia -> 6 EAT ON MALLOAKLEIGH,3166Australia -> 6/27 Ross StreetHUNTINGDALE,3166Australia -> 1/196 clayton roadCLAYTON,3168Australia -> Shop-2355, 1341 Dandenong RoadCHADSTONE CENTRE,3148Australia -> Unit13 18-20 Edward StreetOAKLEIGH,3166Australia -> 101 Atkinson St,OAKLEIGH,3166Australia -> 1 3 Crana CourtCHADSTONE,3148Australia -> 134 DANEDENONG ROADCHADSTONE,3148Australia -> Chadstone S/CentreCHADSTONE,3148Australia -> 1341 Dandenong RoadMALVERN EAST,3145Australia -> Chadstone S/CentreCHADSTONE,3148Australia -> 1341 DANDENONG ROADCHADSTONE,3148Australia -> 97 Huntingdale RoadASHWOOD,3147Australia -> Unit 3A, 215 Browns RoadNOBLE PARK,3174Australia -> 29B AVONDALE GROVEMT WAVERLEY,3149Australia -> Mt Waverly Display HomesMT WAVERLEY,3149Australia -> UNIT 1/ 340 HIGHBURY ROADMT WAVERLEY,3149Australia -> 38 Kinrade StreetHUGHESDALE,3166Australia -> 16/45 Normanby RoadNOTTING HILL,3168Australia -> CSIRO ENQUIRIES, Gate 3 , Nor manby RoadCLAYTON,3168Australia -> Monash University Clayton CampCLAYTON,3168Australia -> 4/ 20 Duerdin StCLAYTON,3168Australia -> 47 MYRTLE STREETGLEN WAVERLEY,3150Australia -> UNIT 97/45 Gilby RoadMT WAVERLEY,3149Australia -> 25 GEDDES STREETMULGRAVE NORTH,3170Australia -> LEVEL 1, 41 LEXIA PLACEMULGRAVE,3170Australia -> 23 Almray PlaceGLEN WAVERLEY,3150Australia -> 72 Glen Tow er DriveGLEN WAVERLEY,3150Australia -> VIEWMOUNT RDGLEN WAVERLEY,3150Australia -> 10 belinda crescentWHEELERS HILL,3150Australia -> 3 Whalley DriveWHEELERS HILL,3150Australia -> 224 BRANDON PARK DRIVEWHEELERS HILL,3150Australia -> WORTLEY GROUP 25 GEDDES STREETMULGRAVE,3170Australia -> 74-86 GARDEN ROADCLAYTON,3168Australia -> 1860 DANDENONG ROADCLAYTON,3168Australia -> 767 SPRINGVALE RDMULGRAVE,3170Australia -> 2/30 MILES STMULGRAVE,3170Australia -> 46-48 GLENVALE CRESCENTMULGRAVE,3170Australia -> 8 Seaview CrescentMULGRAVE,3170Australia -> 71 OSBORNE AVENUESPRINGVALE,3171Australia -> 4/820 PRINCES HIGHWAYSPRINGVALE,3171Australia -> 177-179 SPRINGVALE ROADSPRINGVALE,3171Australia -> 294 springvale rdSPRINGVALE,3171Australia -> 7 Upwey AveSPRINGVALE,3171Australia -> Unit 2 / 6 Bowmore RoadNOBLE PARK,3174Australia -> 9 Douglas StNOBLE PARK,3174Australia -> 64 Pound road West Dandenong South, Australia
['========== DBSCAN Cluster ', '(1,)', 'results ==================================']
Total distance: 3 miles

Route:

64 Pound road West Dandenong South, Australia -> 3 Macs PlaceELTON SOUTH,3338Australia -> 3 SCARCROFT TERRACEMELTON WEST,3337Australia -> 7 CAMPBELL COURTBROOKFIELD,3338Australia -> 64 Pound road West Dandenong South, Australia
['========== DBSCAN Cluster ', '(2,)', 'results ==================================']
Total distance: 4 miles

Route:

64 Pound road West Dandenong South, Australia -> 8 Hilda StreetDARLEY,3340Australia -> 189 MAIN STBACCHUS MARSH,3340Australia -> 5 SECOND MEWSMADDINGLEY,3340Australia -> 64 Pound road West Dandenong South, Australia
['========== DBSCAN Cluster ', '(3,)', 'results ==================================']
Total distance: 1 miles

Route:

64 Pound road West Dandenong South, Australia -> 4 WARREN AVEWALLAN,3756Australia -> 4 Lanter n Cour tWALLAN,3756Australia -> 12 TREEVIOLET LANEALLAN,3756Australia -> 58 Raglan StWALLAN,3756Australia -> 64 Pound road West Dandenong South, Australia
['========== DBSCAN Cluster ', '(4,)', 'results ==================================']
Total distance: 4 miles

Route:

64 Pound road West Dandenong South, Australia -> 27 Golfview DveCRAIGIEBURN,3064Australia -> 20 Cowes StreetCRAIGIEBURN,3064Australia -> 12 WATERBURY TURNCRAIGIEBURN,3064Australia -> 93 FRONTIER AVENUEGREENVALE,3059Australia -> 64 Pound road West Dandenong South, Australia
['========== DBSCAN Cluster ', '(5,)', 'results ==================================']
Total distance: 3 miles

Route:

64 Pound road West Dandenong South, Australia -> 9 PICCADILLY COURTGREENVALE,3059Australia -> 1 Yandoit CourtMEADOW HTS,3048Australia -> 19 Tollkeepers ParadeATTWOOD,3049Australia -> 64 Pound road West Dandenong South, Australia
['========== DBSCAN Cluster ', '(6,)', 'results ==================================']
Total distance: 0 miles

Route:

64 Pound road West Dandenong South, Australia -> 86-88 MAIN ROADRIDDELLS CREEK,3431Australia -> 15 SOUTHBOURNE ROADRIDDELLS CREEK,3431Australia -> 64 Pound road West Dandenong South, Australia 
```

K-means

``` ************************ Kmeans Starts Here*******************************************
Kmeanslabels=  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 4 1 2 4 4 4 2 4 4 2 2 2 4 4 4 4 4 2 4 4 4 2 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 3 3 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 2
 2 2 3]
 ['========== kmeans Cluster ', '(0,)', 'results ==================================']
Total distance: 24 miles

Route:

64 Pound road West Dandenong South, Australia -> 9 Douglas StNOBLE PARK,3174Australia -> Unit 2 / 6 Bowmore RoadNOBLE PARK,3174Australia -> 7 Upwey AveSPRINGVALE,3171Australia -> 10 JONATHAN COURTNOBLE PARK,3174Australia -> 28 GUNTHER AVENUESPRINGVALE,3171Australia -> 71 OSBORNE AVENUESPRINGVALE,3171Australia -> 767 SPRINGVALE RDMULGRAVE,3170Australia -> 25 GEDDES STREETMULGRAVE NORTH,3170Australia -> UNIT 97/45 Gilby RoadMT WAVERLEY,3149Australia -> 47 MYRTLE STREETGLEN WAVERLEY,3150Australia -> UNIT 1/ 340 HIGHBURY ROADMT WAVERLEY,3149Australia -> Mt Waverly Display HomesMT WAVERLEY,3149Australia -> 29B AVONDALE GROVEMT WAVERLEY,3149Australia -> Unit 3A, 215 Browns RoadNOBLE PARK,3174Australia -> 97 Huntingdale RoadASHWOOD,3147Australia -> 1341 DANDENONG ROADCHADSTONE,3148Australia -> Chadstone S/CentreCHADSTONE,3148Australia -> 1341 Dandenong RoadMALVERN EAST,3145Australia -> Chadstone S/CentreCHADSTONE,3148Australia -> 134 DANEDENONG ROADCHADSTONE,3148Australia -> 1 3 Crana CourtCHADSTONE,3148Australia -> 101 Atkinson St,OAKLEIGH,3166Australia -> 43 George StreetOAKLEIGH,3166Australia -> 1090 Centre RdOAKLEIGH SOUTH,3167Australia -> 2 / 45 Bunney RoadCLARINDA,3169Australia -> 27 Clarinda RoadOAKLEIGH SOUTH,3167Australia -> 1/2A COORA RDOAKLEIGH SOUTH,3167Australia -> 81-83 Fairbank RdCLAYTON SOUTH,3169Australia -> 1418A CENTRE RDCLAYTON,3168Australia -> 1860 DANDENONG ROADCLAYTON,3168Australia -> 2/30 MILES STMULGRAVE,3170Australia -> 46-48 GLENVALE CRESCENTMULGRAVE,3170Australia -> 8 Seaview CrescentMULGRAVE,3170Australia -> 4/820 PRINCES HIGHWAYSPRINGVALE,3171Australia -> 177-179 SPRINGVALE ROADSPRINGVALE,3171Australia -> 294 springvale rdSPRINGVALE,3171Australia -> 785 PRINCES HWYSPRINGVALE,3171Australia -> UNIT 36/632 CLAYTON ROADCLAYTON,3168Australia -> 31-35 Bendix DriveCLAYTON SOUTH,3169Australia -> 224 FERNTREE GULLYNOTTING HILL,3168Australia -> 28 Haughton RoadOAKLEIGH,3166Australia -> 6/27 Ross StreetHUNTINGDALE,3166Australia -> 6 EAT ON MALLOAKLEIGH,3166Australia -> Unit13 18-20 Edward StreetOAKLEIGH,3166Australia -> Shop-2355, 1341 Dandenong RoadCHADSTONE CENTRE,3148Australia -> 1/196 clayton roadCLAYTON,3168Australia -> 38 Kinrade StreetHUGHESDALE,3166Australia -> 16/45 Normanby RoadNOTTING HILL,3168Australia -> CSIRO ENQUIRIES, Gate 3 , Nor manby RoadCLAYTON,3168Australia -> Monash University Clayton CampCLAYTON,3168Australia -> 4/ 20 Duerdin StCLAYTON,3168Australia -> 74-86 GARDEN ROADCLAYTON,3168Australia -> LEVEL 1, 41 LEXIA PLACEMULGRAVE,3170Australia -> 23 Almray PlaceGLEN WAVERLEY,3150Australia -> 72 Glen Tow er DriveGLEN WAVERLEY,3150Australia -> VIEWMOUNT RDGLEN WAVERLEY,3150Australia -> 10 belinda crescentWHEELERS HILL,3150Australia -> 3 Whalley DriveWHEELERS HILL,3150Australia -> 224 BRANDON PARK DRIVEWHEELERS HILL,3150Australia -> WORTLEY GROUP 25 GEDDES STREETMULGRAVE,3170Australia -> 7 Robyn CourtDANDENONG NORTH,3175Australia -> 1449 Heatherton Road DandenongDANDENONG,3175Australia -> 10 Glenelg streetDANDENONG NORTH,3175Australia -> 234 HIGH STREETASHBURTON,3147Australia -> 215/207-219 Browns RoadNOBLE PARK,3174Australia -> 19 TURNER CTANDENONG,3175Australia -> 217 PRINCES HIGHWAYDANDENONG,3175Australia -> SHOP L3, 368 DANDENONG PLAZADANDENONG,3175Australia -> 64 Pound road West Dandenong South, Australia
['========== kmeans Cluster ', '(1,)', 'results ==================================']
Total distance: 0 miles

Route:

64 Pound road West Dandenong South, Australia -> 64 Pound road West Dandenong South, Australia
['========== kmeans Cluster ', '(2,)', 'results ==================================']
Total distance: 63 miles

Route:

64 Pound road West Dandenong South, Australia -> 69 Outlook LnGISBORNE,3437Australia -> 12 CLOWES STREETTYLDEN,3444Australia -> 10 Hopbush AvenueSUNBURY,3429Australia -> 10 TRENTHAM ROADTYLDEN,3444Australia -> 153 Markham RdIDDELLS CREEK,3431Australia -> 86-88 MAIN ROADRIDDELLS CREEK,3431Australia -> 15 SOUTHBOURNE ROADRIDDELLS CREEK,3431Australia -> 78 Hutchinsons LaneROMSEY,3434Australia -> 14 REES RDSUNBURY,3429Australia -> 96 High StreetTRENTHAM,3458Australia -> 230 PEARSONS ROADTRENTHAM EAST,3458Australia -> 64 Pound road West Dandenong South, Australia
['========== kmeans Cluster ', '(3,)', 'results ==================================']
Total distance: 40 miles

Route:

64 Pound road West Dandenong South, Australia -> 10 queensferr y placeGREENVALE,3059Australia -> 12 TREEVIOLET LANEALLAN,3756Australia -> 20 Cowes StreetCRAIGIEBURN,3064Australia -> 1 Yandoit CourtMEADOW HTS,3048Australia -> 22 Groveton StreetCRAIGIEBURN,3064Australia -> 93 FRONTIER AVENUEGREENVALE,3059Australia -> 4 WARREN AVEWALLAN,3756Australia -> 58 Raglan StWALLAN,3756Australia -> 19 Tollkeepers ParadeATTWOOD,3049Australia -> 27 Golfview DveCRAIGIEBURN,3064Australia -> 5 MCCARTHY CRTWALLAN,3756Australia -> 4 Lanter n Cour tWALLAN,3756Australia -> 12 WATERBURY TURNCRAIGIEBURN,3064Australia -> 9 PICCADILLY COURTGREENVALE,3059Australia -> 18 Sanctuary CctBEVERIDGE,3753Australia -> 43 AFFLECK STWANDONG,3758Australia -> 64 Pound road West Dandenong South, Australia
['========== kmeans Cluster ', '(4,)', 'results ==================================']
Total distance: 36 miles

Route:

64 Pound road West Dandenong South, Australia -> 7 CAMPBELL COURTBROOKFIELD,3338Australia -> 5 Karr i Cour tBROOKFIELD,3338Australia -> 1 aubisque closePLUMPTON,3335Australia -> 3 SCARCROFT TERRACEMELTON WEST,3337Australia -> 3 Macs PlaceELTON SOUTH,3338Australia -> 5 SECOND MEWSMADDINGLEY,3340Australia -> 5 Parr is Av eMELTON WEST,3337Australia -> 8 Hilda StreetDARLEY,3340Australia -> 59 DARLEY DRIVEDARLEY,3340Australia -> 161 HIGH STREETMELTON,3337Australia -> 2051 Wester n HighwayROCKBANK,3335Australia -> 11 Grifth StMADDINGLEY,3340Australia -> UNIT 5 2 RESERVE ROADMELTON,3337Australia -> 189 MAIN STBACCHUS MARSH,3340Australia -> 64 Pound road West Dandenong South, Australia
************************ Original label plotting**************
['========== Original Cluster ', '0', 'results ==================================']
Total distance: 21 miles

Route:

64 Pound road West Dandenong South, Australia -> SHOP L3, 368 DANDENONG PLAZADANDENONG,3175Australia -> 19 TURNER CTANDENONG,3175Australia -> 217 PRINCES HIGHWAYDANDENONG,3175Australia -> 1449 Heatherton Road DandenongDANDENONG,3175Australia -> 7 Robyn CourtDANDENONG NORTH,3175Australia -> 10 Glenelg streetDANDENONG NORTH,3175Australia -> 234 HIGH STREETASHBURTON,3147Australia -> 215/207-219 Browns RoadNOBLE PARK,3174Australia -> 177-179 SPRINGVALE ROADSPRINGVALE,3171Australia -> 71 OSBORNE AVENUESPRINGVALE,3171Australia -> 8 Seaview CrescentMULGRAVE,3170Australia -> 2/30 MILES STMULGRAVE,3170Australia -> Unit 3A, 215 Browns RoadNOBLE PARK,3174Australia -> LEVEL 1, 41 LEXIA PLACEMULGRAVE,3170Australia -> 25 GEDDES STREETMULGRAVE NORTH,3170Australia -> 767 SPRINGVALE RDMULGRAVE,3170Australia -> 46-48 GLENVALE CRESCENTMULGRAVE,3170Australia -> 4/820 PRINCES HIGHWAYSPRINGVALE,3171Australia -> 294 springvale rdSPRINGVALE,3171Australia -> 785 PRINCES HWYSPRINGVALE,3171Australia -> 28 GUNTHER AVENUESPRINGVALE,3171Australia -> 10 JONATHAN COURTNOBLE PARK,3174Australia -> 7 Upwey AveSPRINGVALE,3171Australia -> Unit 2 / 6 Bowmore RoadNOBLE PARK,3174Australia -> 9 Douglas StNOBLE PARK,3174Australia -> 64 Pound road West Dandenong South, Australia
['========== Original Cluster ', '1', 'results ==================================']
Total distance: 12 miles

Route:

64 Pound road West Dandenong South, Australia -> 224 BRANDON PARK DRIVEWHEELERS HILL,3150Australia -> 3 Whalley DriveWHEELERS HILL,3150Australia -> 10 belinda crescentWHEELERS HILL,3150Australia -> UNIT 97/45 Gilby RoadMT WAVERLEY,3149Australia -> 47 MYRTLE STREETGLEN WAVERLEY,3150Australia -> Shop-2355, 1341 Dandenong RoadCHADSTONE CENTRE,3148Australia -> 43 George StreetOAKLEIGH,3166Australia -> 1341 DANDENONG ROADCHADSTONE,3148Australia -> Chadstone S/CentreCHADSTONE,3148Australia -> 1341 Dandenong RoadMALVERN EAST,3145Australia -> Chadstone S/CentreCHADSTONE,3148Australia -> 134 DANEDENONG ROADCHADSTONE,3148Australia -> 1 3 Crana CourtCHADSTONE,3148Australia -> 97 Huntingdale RoadASHWOOD,3147Australia -> 29B AVONDALE GROVEMT WAVERLEY,3149Australia -> UNIT 1/ 340 HIGHBURY ROADMT WAVERLEY,3149Australia -> Mt Waverly Display HomesMT WAVERLEY,3149Australia -> 23 Almray PlaceGLEN WAVERLEY,3150Australia -> 72 Glen Tow er DriveGLEN WAVERLEY,3150Australia -> VIEWMOUNT RDGLEN WAVERLEY,3150Australia -> 64 Pound road West Dandenong South, Australia
['========== Original Cluster ', '2', 'results ==================================']
Total distance: 785 miles

Route:

64 Pound road West Dandenong South, Australia -> 69 Outlook LnGISBORNE,3437Australia -> 14 REES RDSUNBURY,3429Australia -> 96 High StreetTRENTHAM,3458Australia -> 7 CAMPBELL COURTBROOKFIELD,3338Australia -> 5 SECOND MEWSMADDINGLEY,3340Australia -> 5 Karr i Cour tBROOKFIELD,3338Australia -> Shop 12/248 MAIN RDLACKWOOD,3458Australia -> 161 HIGH STREETMELTON,3337Australia -> 2051 Wester n HighwayROCKBANK,3335Australia -> 5 Parr is Av eMELTON WEST,3337Australia -> 12 CLOWES STREETTYLDEN,3444Australia -> 8 Hilda StreetDARLEY,3340Australia -> 59 DARLEY DRIVEDARLEY,3340Australia -> 10 Hopbush AvenueSUNBURY,3429Australia -> 3 Macs PlaceELTON SOUTH,3338Australia -> 230 PEARSONS ROADTRENTHAM EAST,3458Australia -> 11 Grifth StMADDINGLEY,3340Australia -> UNIT 5 2 RESERVE ROADMELTON,3337Australia -> 189 MAIN STBACCHUS MARSH,3340Australia -> 3 SCARCROFT TERRACEMELTON WEST,3337Australia -> 1 aubisque closePLUMPTON,3335Australia -> 64 Pound road West Dandenong South, Australia
['========== Original Cluster ', '3', 'results ==================================']
Total distance: 3 miles

Route:

64 Pound road West Dandenong South, Australia -> 1/196 clayton roadCLAYTON,3168Australia -> 28 Haughton RoadOAKLEIGH,3166Australia -> 1/2A COORA RDOAKLEIGH SOUTH,3167Australia -> 27 Clarinda RoadOAKLEIGH SOUTH,3167Australia -> 1090 Centre RdOAKLEIGH SOUTH,3167Australia -> UNIT 36/632 CLAYTON ROADCLAYTON,3168Australia -> 81-83 Fairbank RdCLAYTON SOUTH,3169Australia -> 31-35 Bendix DriveCLAYTON SOUTH,3169Australia -> 1418A CENTRE RDCLAYTON,3168Australia -> 1860 DANDENONG ROADCLAYTON,3168Australia -> 74-86 GARDEN ROADCLAYTON,3168Australia -> 4/ 20 Duerdin StCLAYTON,3168Australia -> 224 FERNTREE GULLYNOTTING HILL,3168Australia -> Monash University Clayton CampCLAYTON,3168Australia -> CSIRO ENQUIRIES, Gate 3 , Nor manby RoadCLAYTON,3168Australia -> 16/45 Normanby RoadNOTTING HILL,3168Australia -> Unit13 18-20 Edward StreetOAKLEIGH,3166Australia -> 101 Atkinson St,OAKLEIGH,3166Australia -> 6 EAT ON MALLOAKLEIGH,3166Australia -> 6/27 Ross StreetHUNTINGDALE,3166Australia -> 64 Pound road West Dandenong South, Australia
['========== Original Cluster ', '4', 'results ==================================']
Total distance: 108 miles

Route:

64 Pound road West Dandenong South, Australia -> 22 Groveton StreetCRAIGIEBURN,3064Australia -> 1 Yandoit CourtMEADOW HTS,3048Australia -> 8 GRANDVIEW CLOSERIDDELLS CREEK,3431Australia -> 27 Golfview DveCRAIGIEBURN,3064Australia -> 19 Tollkeepers ParadeATTWOOD,3049Australia -> 4 Lanter n Cour tWALLAN,3756Australia -> 12 WATERBURY TURNCRAIGIEBURN,3064Australia -> 9 PICCADILLY COURTGREENVALE,3059Australia -> 18 Sanctuary CctBEVERIDGE,3753Australia -> 43 AFFLECK STWANDONG,3758Australia -> 40 Dillon CourtDIGGERS REST,3427Australia -> 10 queensferr y placeGREENVALE,3059Australia -> 20 Cowes StreetCRAIGIEBURN,3064Australia -> 12 TREEVIOLET LANEALLAN,3756Australia -> 93 FRONTIER AVENUEGREENVALE,3059Australia -> 153 Markham RdIDDELLS CREEK,3431Australia -> 86-88 MAIN ROADRIDDELLS CREEK,3431Australia -> 15 SOUTHBOURNE ROADRIDDELLS CREEK,3431Australia -> 5 MCCARTHY CRTWALLAN,3756Australia -> 2 Tina CourtCLARINDA,3169Australia -> 58 Raglan StWALLAN,3756Australia -> 4 WARREN AVEWALLAN,3756Australia -> 78 Hutchinsons LaneROMSEY,3434Australia -> 64 Pound road West Dandenong South, Australia
```
The distance traveeled in each route speaks iteself that DBSCAN is better to use for geographical clsutering and optimal routing for courier company delivery.
# How to use


