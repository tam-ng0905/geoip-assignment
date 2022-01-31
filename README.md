# geoIp


# Structure
```bash
├── LICENSE
├── README.md
├──list_of_ips.txt
├── lookups
│   ├── geo_ip_lookup.py
│   └── rdap_lookup.py
├── main.py
├── extract
│   ├── __init__.py
│   └── extract.py
├── requirements.txt
├── dump.rdb
└── utils
    ├── __init__.py
    └── utils.py
```

## Installation
1. `activate a virtual env`
2. run `pip install -r requirements.txt`
3. open the redis server
   1. `run redis-server in one terminal`
   2. `open another terminal and run redis-cli`
4. run `python3 main.py`


Notice: it will take a while to finish the first run. Howerver, the second time will be faster since the data
are cached into redis cache database.

