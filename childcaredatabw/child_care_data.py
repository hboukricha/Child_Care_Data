# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Copyright (c) 2018 The Python Packaging Authority

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ---------------------------------------------------------------------------------
# @Author: hana.boukricha
# @Date:   2021-03-06 22:12:41
# @Last Modified by:   hana.boukricha
# @Last Modified time: 2021-03-25 22:53:34

""" This module provides an integrable api library to retrieve data on child 
care numbers in Baden Wuertemberg """

import re as regex
import pandas as pd


def read_data(file_name, file_format):
    """ read the file data from str file_name with str file_format and return a data structure. 
    Currently supported file_format is csv. """

    if file_format == "csv":
        data = __read_data_csv(file_name)
    else:
        # if file_format not supported set data object to None (null)
        data = None
        raise Exception("function child_care_data.read_data: Specified file_format", file_format, 
        "is not supported, please look at the api user manual for supported formats!")

    return data


def get_data_year(year, data_structure):
    """ read data_structure and return data_year including data for str year. Read data_structure 
    with respect to str data_format. """
    
    try:
        data_year = data_structure[year]
    except Exception as error:
        print(error)
    else:
        print(data_year)
        return data_year


def get_data_year_location(year, location, data_structure):
    """ read data_structure and return data_year_location including data for str year and str location. 
    Read data_structure with respect to str data_format. """
    
    try:
        data_year_location = data_structure[year][location]
    except Exception as error:
        print(error)
    else:
        print(data_year_location)
        return data_year_location


def get_data_year_location_age(year, location, age, data_structure):
    """ read data_structure and return data_year_age including data for str year and str age. Read data_structure 
    with respect to str data_format. """
    
    try:
        data_year_location_age = data_structure[year][location][age]
    except Exception as error:
        print(error)
    else:
        print(data_year_location_age)
        return data_year_location_age


def __read_data_csv(file_name):
    """ read csv formatted data from str file_name and returns a pandas dataframe csv_data. """
    try:
        csv_data = pd.read_csv(file_name, delimiter=";", skiprows=2, header=None)

    except Exception as error:
        print(error)
    else:
        # restructure / organize csv_data to easily define filters and query data from dataframe
        # new structure is 'year/age' (rows) x 'location' (columns)
        # please note that every 'element' in the rows except 'year' is called 'age' in this implementation
        num_rows = len(csv_data)
        num_columns = len(csv_data.columns)
        data_dict = {}
        # going through all rows and columns of the dataframe
        for i in range(num_rows):
            for j in range(num_columns):
                element = csv_data.iloc[i, j]
                # regular expression matching any year within dataframe
                year_exp = "20[0,1,2]"
                if not pd.isna(element):
                    result = regex.match(year_exp, element)
                    if result:
                        data_dict[csv_data.iloc[i, j]] = {}
                        data_dict[csv_data.iloc[i, j]]['Tageseinrichtung'] = {}
                        data_dict[csv_data.iloc[i, j]]['Tagespflege'] = {}
                        data_dict[csv_data.iloc[i, j]]['Insgesamt'] = {}

                        data_dict[csv_data.iloc[i, j]]['Tageseinrichtung'][csv_data.iloc[i+1, j].strip()] = csv_data.iloc[i+1, j+1]
                        data_dict[csv_data.iloc[i, j]]['Tageseinrichtung'][csv_data.iloc[i+3, j].strip()] = csv_data.iloc[i+3, j+1]
                        data_dict[csv_data.iloc[i, j]]['Tageseinrichtung'][csv_data.iloc[i+4, j].strip()] = csv_data.iloc[i+4, j+1]
                        data_dict[csv_data.iloc[i, j]]['Tageseinrichtung'][csv_data.iloc[i+5, j].strip()] = csv_data.iloc[i+5, j+1]
                        data_dict[csv_data.iloc[i, j]]['Tageseinrichtung'][csv_data.iloc[i+6, j].strip()] = csv_data.iloc[i+6, j+1]

                        data_dict[csv_data.iloc[i, j]]['Tagespflege'][csv_data.iloc[i+1, j].strip()] = csv_data.iloc[i+1, j+2]
                        data_dict[csv_data.iloc[i, j]]['Tagespflege'][csv_data.iloc[i+3, j].strip()] = csv_data.iloc[i+3, j+2]
                        data_dict[csv_data.iloc[i, j]]['Tagespflege'][csv_data.iloc[i+4, j].strip()] = csv_data.iloc[i+4, j+2]
                        data_dict[csv_data.iloc[i, j]]['Tagespflege'][csv_data.iloc[i+5, j].strip()] = csv_data.iloc[i+5, j+2]
                        data_dict[csv_data.iloc[i, j]]['Tagespflege'][csv_data.iloc[i+6, j].strip()] = csv_data.iloc[i+6, j+2]

                        data_dict[csv_data.iloc[i, j]]['Insgesamt'][csv_data.iloc[i+1, j].strip()] = csv_data.iloc[i+1, j+3]
                        data_dict[csv_data.iloc[i, j]]['Insgesamt'][csv_data.iloc[i+3, j].strip()] = csv_data.iloc[i+3, j+3]
                        data_dict[csv_data.iloc[i, j]]['Insgesamt'][csv_data.iloc[i+4, j].strip()] = csv_data.iloc[i+4, j+3]
                        data_dict[csv_data.iloc[i, j]]['Insgesamt'][csv_data.iloc[i+5, j].strip()] = csv_data.iloc[i+5, j+3]
                        data_dict[csv_data.iloc[i, j]]['Insgesamt'][csv_data.iloc[i+6, j].strip()] = csv_data.iloc[i+6, j+3]
        return data_dict

