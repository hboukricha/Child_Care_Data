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

#---------------------------------------------------------------------------------
# @Author: hana.boukricha
# @Date:   2021-03-08 09:49:19
# @Last Modified by:   hana.boukricha
# @Last Modified time: 2021-03-09 23:01:07

""" This module implements api to retrieve csv formatted data on child care numbers in Baden Wuertemberg """

import re as regex
import pandas as pd


def read_data_csv(file_name):
    """ read csv formatted data from str file_name and returns a pandas dataframe csv_data. """
    try: 
        csv_data = pd.read_csv(file_name, delimiter=";", skiprows=2, header=None) 
    except Exception as error:
        print(error)
    else:
        # restructure / organize csv_data to easily define filters and query data from data frame
        # new structure is year followed by the locations on the same row
        num_rows = len(csv_data)
        num_columns = len(csv_data.columns)
        # going through all rows and columns of the DataFrame 
        for i in range(num_rows) :
            for j in range (num_columns) :
                element = csv_data.iloc[i, j]
                # regular exprssion matching any year within DataFrame
                year_exp = "20[0,1,2]"
                if not pd.isna(element) :
                    result = regex.match(year_exp, element)
                    if result:
                        # replace NaN columns after year with correct location
                        csv_data.iloc[i, j+1] = "Tageseinrichtung"
                        csv_data.iloc[i, j+2] = "Tagespflege"
                        csv_data.iloc[i, j+3] = "Insgesamt"
        return csv_data
   

def get_data_year_csv(year, dataframe):
    """ filters data per str year from pandas dataframe and returns a new sliced pandas csv_data_year including all the data for str year. """
    if dataframe is None:
        raise Exception("function child_care_data_csv.get_data_year_csv: data object is of type None!")
    try:  
        num_rows = len(dataframe)
        num_columns = len(dataframe.columns)
        # initialize csv_data_year as empty DataFrame
        csv_data_year = pd.DataFrame()
        # going through all rows and columns of the DataFrame 
        for i in range(num_rows) :
            for j in range (num_columns) :
                element = dataframe.iloc[i, j] 
                if(element == year):
                    # include all elements related to a given year within new DataFrame csv_data_year 
                    csv_data_year = dataframe.iloc[i: i+7]
        if csv_data_year.empty:
            raise Exception("function child_care_data_csv.get_data_year_csv: data frame is empty. Possible reason: Input year is not found.")
        if csv_data_year is None:
            raise Exception("function child_care_data_csv.get_data_year_csv: data object is of type None!")            
    except Exception as error:
        print(error)
    else:
        return csv_data_year


def get_data_year_location_csv(year, location, dataframe):
    """ filters data per str year and str location from pandas dataframe and returns a new sliced pandas csv_data_year_location including all the data for str year and str location. """
    if dataframe is None:
        raise Exception("function child_care_data_csv.get_data_year_location_csv: data object is of type None!")
    try:  
        num_rows = len(dataframe)
        num_columns = len(dataframe.columns)
        # initialize csv_data_year_location as empty DataFrame
        csv_data_year_location = pd.DataFrame()
        # going through all rows and columns of the DataFrame 
        for i in range(num_rows) :
            for j in range (num_columns) :
                el_year = dataframe.iloc[i, j] 
                if(el_year == year):
                    # going through columns within a year
                    for k in range (num_columns):
                        el_location = dataframe.iloc[i, k]
                        if (el_location == location):
                            # include all elements related to a given year and location within new DataFrame csv_data_year_location 
                            csv_data_year_location = dataframe.iloc[i:i+7, [0, k]]
        if csv_data_year_location.empty:
            raise Exception("function child_care_data_csv.get_data_year_location_csv: data frame is empty. Possible reason: Input year or location is not found.")
        if csv_data_year_location is None:
            raise Exception("function child_care_data_csv.get_data_year_location_csv: data object is of type None!")            
    except Exception as error:
        print(error)
    else:
        return csv_data_year_location
    

def get_data_year_age_csv(year, age, dataframe):
    pass