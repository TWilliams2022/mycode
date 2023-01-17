#!/usr/bin/env python3

import requests

API = "https://fantasy.premierleague.com/api/bootstrap-static/"

def main():
    
    response = requests.get(f"{API}teams")

    new = response.json().keys()

    main()
