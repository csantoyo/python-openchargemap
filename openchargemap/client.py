import requests

from geopy.geocoders import Nominatim
 
class Client():
	"""
		Client class serving as API wrapper for openchargemap api.
	"""

	BASE_URL = "https://api.openchargemap.io/v3/"
	POI_URL = BASE_URL + "poi"

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


	def get_charging_locations(self, address=None, distance=1.0):
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

		geolocator = Nominatim(user_agent="chargingevapp")
		location = geolocator.geocode(address)

		if location is None:
			raise Exception("Location address is not found on OpenStreetMaps. Please check address.")

	def _construct_uri_(self):
       """
        	Construct url for api request
        
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












