# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:23:49 2019

@author: Sai Charan Reddy
"""

import logging
from data_builder import keywords_data,params, _create_search_list, company_data

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)-8s - %(levelname)-6s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.FileHandler('data/logs_app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logger.info('started.')

# these are our search parameters
key_words = ["Exterminator", "Pest Control", "Bedbug Control", "Bedbug Inspector", "Bedbug Inspection", "Mice Control", "Roach Control", "Mice Exterminator", "Pest Management"]
modifiers = ["", "Best", "NYC", "Eco-Friendly", "Manhattan", "Brooklyn", "Queens", "Long Island", "Westchester", "Hampton", "Nassau County", "Suffolk County", "Jersey City", "Hoboken", "Hudson County"]
brooklyn_zipcodes = [11201, 11215,11234,11238,11209]
manhattan_zipcodes = [10023,10025,10024,10011,10128,10016,10003,10021,10028,10022]
queens_zipcodes = [11375,11357,11385,11101,11377,11374]
nassau_zipcodes = [11758,11566,11040,11530,11793]
# assigning params
complete_zipcodes = sorted(sorted(brooklyn_zipcodes) + sorted(manhattan_zipcodes) + sorted(queens_zipcodes) + sorted(nassau_zipcodes))
params['zipcodes'] = complete_zipcodes

#params['zipcodes'] = brooklyn_zipcodes[:1]
params["key_words"] = key_words
params["modifiers"] = modifiers
keywords_data()
# len(_create_search_list(params))

# companies
#company_list1 = ["Terminix", "Orkin", "Ehrlich", "vikingpest", "Ecolab", "trulynolen", "Rentokil Steritech", "eco-wise pest management", "NYC PEST CONTROL", "Bell Environmental Services", "A Bell Pest Control", "Green Earth Pest Control", "BHB pest elimination", "Pest Away Inc", "ODIN Bed Bug Exterminator NYC", "organic pest control nyc"]
#company_list2 = ["metropest", "HPC PEST MANAGEMENT"]
#company_list3 = ["MMPC"]
#company_data(company_list3)