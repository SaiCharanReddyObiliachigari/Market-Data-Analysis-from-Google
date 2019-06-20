# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from lib.google_search_results import GoogleSearchResults
from itertools import product
import json
import config

params = dict(zipcodes = list(), key_words= list(), modifiers = [], device_types= ['desktop','mobile'])

@@ -10,17 +11,20 @@ def start():
    # combinations
    search_list = _create_search_list(params)
    # loop combines all the possible combinations of key_word & modifier
    for (zipcode,key_word,modifier,device_type) in search_list:
    # TODO: delete [:1] after code is ready
    for zipcode,key_word,modifier,device_type in search_list[:1]:
        serp_params = {
            "q" : key_word + " " + modifier,
            "device" : device_type,
            "location" : "{}, New York, United States".format(str(zipcode)),
            "hl" : "en",
            "gl" : "us",
            "google_domain" : "google.com",
            "google_domain" : "google.com"
        }

        query = GoogleSearchResults(serp_params)
        query.BACKEND = 'http://serpapi.com/search'
        query.SERP_API_KEY = config.API_KEY
        dictionary_results = query.get_dictionary()
        # this will concentrate only on out 4 requirments
        results.append(dictionary_results)
@@ -38,8 +42,8 @@ def _create_search_list(params: params):
    params: its a dict of search list
    """
    # results = []
    prod = product(params.zipcodes, params.key_words, params.modifiers, params.device_types)
    return [prod] 
    prod = product(params["zipcodes"], params["key_words"], params["modifiers"], params["device_types"])
    return [i for i in prod]

# testing how the prodict results shows up
# list(product([1,2,3], [4,5,6], ['as', 'ds', 're','sd'], ['a', 'b']))