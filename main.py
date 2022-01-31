import os
from lookups import geo_lookup
from lookups import rdap_lookup
from extract import extract
from tqdm import tqdm
from utils import utils
import redis
import json


def main(file_name="ips.txt"):
    '''
    Summary line.
    Main function to check if the ip's data is already cached or not, if not, fetch it

    Parameters
    ----------
    file_name : str
    This is the filename of the text file.

    Returns
    -------
    None
    Description of return value
    '''

    # fetch current working directory
    current_dir = os.getcwd()
    # joins together string absolute path with string filename
    file_name = os.path.join(current_dir, file_name)

    # set up redis connection
    redis_client = redis.Redis(host='localhost', port=6379, db=0)

    # extract ip from the text
    ips = extract.extract(file_name)

    # get the length of ips
    length_of_list = len(ips)

    # iterates through each ip address, gathering geo and rdap information for each ip address.
    # Also shows the progress of the database being populated.
    for i in tqdm(range(length_of_list)):

        # check if the ip is already cached
        ip = ips[i]
        isGeoCached = redis_client.get(ip + "geo")
        isRDAPCached = redis_client.get(ip + "rdap")

        # if the ip is already cached, print it out
        # otherwise fetch it
        if isGeoCached is not None:
            print(isGeoCached)
        else:
            geo_info = geo_lookup.geo_lookup(ip)
            redis_client.mset({ip + "geo": json.dumps(geo_info)})
            print(geo_info)

        if isRDAPCached is not None:
            print(isRDAPCached)
        else:
            rdap_info = rdap_lookup.rdap_lookup(ip)
            redis_client.mset({ip + "rdap": json.dumps(rdap_info)})
            print(rdap_info)


# execute main program.
if __name__ == "__main__":
    args = utils.input_args()
    main(args.filename)
