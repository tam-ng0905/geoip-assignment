# from utils import input_args
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json


def geo_lookup(address):
    '''
            Summary line.
            Fetch the data for the ip

            Parameters
            ----------
            address : ip address
            The ip address that we want to fetch

            Returns
            -------
            Return all the geo data for that ip
            '''

    lookup_url = "https://freegeoip.app/json/{}".format(address)
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    response = session.get(lookup_url, headers=headers)

    if response.status_code == 200:
        query = json.loads(response.content.decode('utf-8'))
        print(query)
        return query
    else:
        print("An error has occurred: {} - {}".format(response.status_code, response.content))
        return None


if __name__ == "__main__":
    geo_lookup("5.5.5.5")
