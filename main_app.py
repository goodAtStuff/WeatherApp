#!/usr/bin/python3
import http.client
import urllib.parse
import json

USER_AGENT = ("goodAtStuff_CLI_Weather_App")

def WeatherQuery(query_path):
    """Generic function for sending requests to the various endpoints of the weather.gov api
       This function takes care of the low-level packing of the HTTPS response
            query_path:   string containing the URL path to the endpoints

            return:       https response object
    """
    headers = { "user-agent" : str(USER_AGENT[0]),
                "accept"     : "json"}
                
    assert(isinstance(query_path, str))

    conn = http.client.HTTPSConnection("api.weather.gov")
    conn.request("GET", query_path, headers=headers)
    response = conn.getresponse()
    payload = response.read()
    
    if not responseGood(response):
        raise QueryException("Query failed", response)
    
    return payload

    
def responseGood(response):
    """Validate that the HTTP(S) response is good and contains data
       TODO: Expand validation to be more robust or consider removing fucntion
    """
    assert(isinstance(response, http.client.HTTPResponse))
    
    if response.status == 200:
        return True
    else:
        return False

    
class QueryException(Exception):
    def __init__(self, text, response):
        super().__init__(text)
        self.response = response

print(WeatherQuery("/points/39.7456,-97.0892"))