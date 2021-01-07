import requests

from geopy.geocoders import Nominatim
 
class Client():
	"""
		Client class serving as API wrapper for openchargemap api.
	"""

	BASE_URL = "https://api.openchargemap.io/v3/"
	POI_URL = BASE_URL + "poi"
	API_PARAMETERS = ["key", "client", "output", "maxresults", "countrycode", 
						"countryid", "latitude", "longitude", "distance", "distanceunit", "operatorid", 
						"connectiontypeid", "levelid", "minpowerkw", "usagetypeid", "statustypeid", "dataproviderid",
						"modifiedsince", "opendata", "includecomments", "verbose", "compact", "camelcase", "callback",
						"chargepointid"]

	API_PARAMETERS = set(API_PARAMETERS)	

	def __init__(self, key=None):
		"""
		Construct client object
		
		Parameters
		----------
			key: str
				API key for open charge map            
		Returns
		-------
		n/a
		
		Notes
		-----
		n/a
 
		"""

		if key:
			self.POI_URL = self.POI_URL + "?key="+ key
		else:
			self.POI_URL = self.POI_URL + "?"

		self.distanceunit='Miles'


	def _init_session_(self):
		"""
			Initialize session
		
		Parameters
		----------
			n/a
			
		Returns
		-------
			n/a
		
		Notes
		-----
			n/a
 
		"""

		self.session = requests.Session()


	def get_charging_locations(self, **kwargs):
		"""
			Get the charging locations near an address.
		
		Parameters
		----------
			address: string
				String of address of interest to find charging stations near

			distance: float
				Distance from address to look for charging stations

		Returns
		-------
			n/a
		
		Notes
		-----
			n/a
		""" 
		uri = self._construct_uri_(**kwargs)
		print(uri)
		r = requests.get(uri)
		return r
	def _construct_uri_(self, **kwargs):
		"""
			Construct url for api request
		
		Parameters
		----------
			n/a

		Returns
		-------
			n/a
		
		Notes
		-----
			n/a
		""" 
		paramurl = ""
		# Loop through key values & check if valid

		for key in kwargs:
			if key == "address":
				longitude, latitude = self._get_coordinates_(kwargs[key])
				paramurl += "longitude" + "=" +str(longitude) +"&latitude=" + str(latitude) + "&"
				continue 

			if (key in self.API_PARAMETERS):
				paramurl += key + "=" + str(kwargs[key]) +"&"
				print(key, type(key), paramurl )
			else:
				raise Exception("The key value "+ key +  " is not a valid entry for the OCM API. Check spelling")

		return self.POI_URL + "&" + paramurl[:-1]

	def _get_coordinates_(self, address):
		"""
			Get longitude and latitude of passed address
		
		Parameters
		----------
			n/a

		Returns
		-------
			n/a
		
		Notes
		-----
			n/a
		""" 

		geolocator = Nominatim(user_agent="chargingevapp")
		location = geolocator.geocode(address)

		if location is None:
			raise Exception("Location address is not found on OpenStreetMaps. Please check address.")

		return location.longitude, location.latitude









