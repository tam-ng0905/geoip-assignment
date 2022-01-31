# from utils import utils
import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def rdap_lookup(address):
    '''
            Summary line.
            Fetch the data for the ip

            Parameters
            ----------
            address : ip address
            The ip address that we want to fetch

            Returns
            -------
            Return all the rdap data for that ip
            '''

    lookup_url = "https://rdap.arin.net/registry/ip/{}".format(address)
    headers = {
        'accept': "application/json",
        'content-type': 'application/json'
    }
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    response = session.get(lookup_url, headers=headers)

    if response.status_code == 200:
        rdap_query = json.loads(response.content.decode('utf-8'))

        try:
            holder = {}
            holder["startAddress"] = rdap_query["startAddress"]
            holder['endAddress'] = rdap_query["endAddress"]
            entities = rdap_query['entities']
            for entry in entities:
                temp_dictionary = entry['vcardArray']
                # iterate for values to retrieve
                for values in temp_dictionary:
                    for value in values:
                        if "fn" in value:
                            holder["company_name"] = value[3]
                        if "adr" in value:
                            holder["company_address"] = value[1]['label']
            return holder
        except:
            return None

    else:
        print("An error has occurred: {} - {}".format(response.status_code, response.content))
        return None


if __name__ == "__main":
    response = rdap_lookup("9.9.9.9")



