# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:25:14 2019

@author: Sai Charan Reddy
"""

import itertools
import json
import config
import time
import csv
import logging
from lib.google_search_results import GoogleSearchResults

logger = logging.getLogger(__name__)
params = dict(zipcodes=list(), key_words=list(), modifiers=[],
              device_types=['desktop', 'mobile'])


def company_data(companies: list):
    company_results = []

    with open('data/raw_companies.json', 'w') as outfile:
        outfile.write('[')
        for company in companies:
            company_serp_params = {
                "q": company.lower(),
                "location": "New York, United States",
                "hl": "en",
                "gl": "us",
                "google_domain": "google.com"
            }

            company_query = GoogleSearchResults(company_serp_params)
            company_query.BACKEND = 'https://serpapi.com/search'
            company_query.SERP_API_KEY = config.API_KEY
            dictionary_results = company_query.get_dictionary()
            company_results.append(dictionary_results)
            print('completed for {}'.format(company))
            time.sleep(5)
            json.dump(dictionary_results, outfile)
            outfile.write(',')
        outfile.write(']')
    return company_results


def keywords_data():
    """ gets keywords data from google search results api based on params. """
    results = []
    # combinations
    search_list = _create_search_list(params)

    # check if the current data has the data.
    existing_data_list = []
    with open('data/raw_keywords.json', 'r') as infile:
        data_list = json.load(infile)
        for existing_data in data_list:
            try:
                existing_data_list.append(existing_data['search_parameters'])
            except Exception:
                pass
    logger.info("existing data count: {}".format(len(existing_data_list)))

    # build non-searched list
    new_search_list = []
    for search_list_item in search_list:
        # build search object
        zipcode, key_word, modifier, device_type = search_list_item
        serp_params = {
            "q": f"{key_word} {modifier}".rstrip(),
            "device": device_type,
            "location_requested": "{}, New York, United States".format(str(zipcode)),
            "location_used": "{},New York,United States".format(str(zipcode)),
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com"
        }

        # check object in the list
        if serp_params not in existing_data_list:
            new_search_list.append(search_list_item)
    logger.info("new search data count: {}".format(len(new_search_list)))

    # loop combines all the possible combinations of key_word & modifier
    for index, search_list_item in enumerate(new_search_list):
        zipcode, key_word, modifier, device_type = search_list_item
        serp_params = {
            "q": f"{key_word} {modifier}".rstrip(),
            "device": device_type,
            "location": "{}, New York, United States".format(str(zipcode)),
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com"
        }

        dictionary_results = _get_serpapi_results(serp_params)
        if dictionary_results is not None:
            # this will concentrate only on out 4 requirments
            results.append(dictionary_results)
            logger.info(f"results collected. {index + 1} of {len(new_search_list)}. current search item : {zipcode}, {key_word}, {modifier}, {device_type}")
        else:
            with open('data/failed_keywords.csv', 'a') as f:
                csv_out = csv.writer(f)
                csv_out.writerow(
                    (index, zipcode, key_word, modifier, device_type))
            search_list.append(search_list_item)
            logger.info(f"results failed in {index + 1} of {len(new_search_list)}. current search item : {search_list_item}")

    # results list need to be saved into a file
    results = existing_data_list + results
    logger.info("final data count: {}".format(len(results)))
    with open('data/raw_keywords.json', 'w') as outfile:
        json.dump(results, outfile)

    return results


def _create_search_list(params: params):
    """ takes all the parameters in the params and returns a list
    params: its a dict of search list
    """
    # results = []
    prod1 = itertools.product(params["zipcodes"], params["key_words"],
                    params["modifiers"], params["device_types"])
    prod_list = list(prod1)

    with open('data/company_list.txt', 'w') as f:
        csv_out = csv.writer(f)
        csv_out.writerows(prod_list)

    return prod_list


def _get_serpapi_results(params):
    try:
        query = GoogleSearchResults(params)
        # query.BACKEND = 'http://serpapi.com/search'
        query.SERP_API_KEY = config.API_KEY
        dictionary_results = query.get_dictionary()

        return dictionary_results
    except Exception as ex:
        with open('data/serpapi_logs.log', 'a') as f:
            f.writelines(ex)
        return None