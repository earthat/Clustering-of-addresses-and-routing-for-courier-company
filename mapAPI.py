"""Class defined for gogle Map Plotting url generation"""



MAX_SIZE = 640                                       # Max size of the map in pixels
SCALE = 2                                            # 1 or 2 (free plan), see Google Static Maps API docs
MAPTYPE = 'roadmap'                                  # Default map type
API_KEY = 'XXXXXXXXX'                                # Put your API key here, see https://console.developers.google.com
BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'

cache = {}                                           # Caching queries to limit API calls / speed them up

class GoogleStaticMapsAPI:
    @classmethod
    def urlConstruct(  # construct the url for google map API
            cls,center=None, zoom=None, size=(MAX_SIZE, MAX_SIZE), scale=SCALE,
            maptype=MAPTYPE, file_format='png32', markers=None, path=None):
        """GET query on the Google Static Maps API to retrieve a static image.
        :param object center: (required if markers not present) defines the center of the map, equidistant from edges.
            This parameter takes a location as either
                * a tuple of floats (latitude, longitude)
                * or a string address (e.g. "city hall, new york, ny") identifying a unique location
        :param int zoom: (required if markers not present) defines the zoom level of the map:
            *  1: World
            *  5: Landmass/continent
            * 10: City
            * 15: Streets
            * 20: Buildings
        :param (int, int) size: (required) defines the rectangular dimensions (pixels) of the map image.
            Max size for each dimension is 640 (free account).
        :param int scale: (optional), 1 or 2 (free plan). Affects the number of pixels that are returned.
            scale=2 returns twice as many pixels as scale=1 while retaining the same coverage area and level of detail
            (i.e. the contents of the map don't change).
        :param string maptype: (optional) defines the type of map to construct. Several possible values, including
            * roadmap (default): specifies a standard roadmap image, as is normally shown on the Google Maps.
            * satellite: specifies a satellite image.
            * terrain: specifies a physical relief map image, showing terrain and vegetation.
            * hybrid:  specifies a hybrid of the satellite and roadmap image, showing a transparent layer of
                major streets and place names on the satellite image.
        :param string file_format: image format
            * png8 or png (default) specifies the 8-bit PNG format.
            * png32 specifies the 32-bit PNG format.
            * gif specifies the GIF format.
            * jpg specifies the JPEG compression format.
            * jpg-baseline
        :param {string: object} markers: points to be marked on the map, under the form of a dict with keys
            * 'color': (optional) 24-bit (0xFFFFCC) or predefined from
                {black, brown, green, purple, yellow, blue, gray, orange, red, white}
            * 'size': (optional) {tiny, mid, small}
            * 'label': (optional) specifies a single uppercase alphanumeric character from the set {A-Z, 0-9}.
                Only compatible with <mid> size markers
            * 'coordinates': list of tuples (lat, long) for which the options are common.
        :return: url
        """
        # For now, caching only if no markers are given
        should_cache = markers is None

        url = BASE_URL
        if center:
            url += 'center={},{}&'.format(*center) if isinstance(center, tuple) else 'center={}&'.format(center)
        if zoom:
            url += 'zoom={}&'.format(zoom)

        markers = markers if markers else []
        for marker in markers:
            if 'lat' in marker and 'long' in marker:
                url += 'markers='
                #for key in ['label']:
                if 'color' in marker:
                    url+='color:'
                    url += '{}%7C'.format(marker['color'])
                url += '{},{}%7C'.format(marker['lat'], marker['long'])
                url += '&'

        path = path if path else[]
        url += 'path=color:0x0000ff%7Cweight:5%7Cfillcolor:0xFFFF0033%7C'

        for pt in path:
            if 'lat' in pt and 'long' in pt:
                url += '{},{}%7C'.format(pt['lat'], pt['long'])

        url += 'scale={}&'.format(scale)
        url += 'size={}x{}&'.format(*tuple(min(el, MAX_SIZE) for el in size))
        url += 'maptype={}&'.format(maptype)
        url += 'format={}&'.format(file_format)
        url += 'key={}'.format(API_KEY)

        if url in cache:
            return cache[url]
        return url

