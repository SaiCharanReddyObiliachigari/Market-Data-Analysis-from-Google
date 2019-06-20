# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:12:34 2019

@author: Sai Charan Reddy
"""

from data_builder import start,params, _create_search_list
# these are our search parameters
key_words = ["Exterminator", "Pest Control", "Bedbug Control", "Bedbug Inspector", "Bedbug Inspection", "Mice Control", "Roach Control", "Mice Exterminator", "Pest Management"]
modifiers = ["Best", "NYC", "Eco-Friendly", "Manhattan", "Brooklyn", "Queens", "Long Island", "Westchester", "Hampton", "Nassau County", "Suffolk County", "Jersey City", "Hoboken", "Hudson County"]
zipcodes = [10001,10002]
# assigning params
params['zipcodes'] = zipcodes
params["key_words"] = key_words
params["modifiers"] = modifiers
start()
# len(_create_search_list(params)) 