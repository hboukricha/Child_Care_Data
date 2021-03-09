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
# @Date:   2021-03-06 22:12:41
# @Last Modified by:   hana.boukricha
# @Last Modified time: 2021-03-09 15:34:55

""" This module provides an api to retrieve data on child care numbers in Baden Wuertemberg """

from childcaredatabw import child_care_data_csv

def read_data(file_name, file_format):
    """ read the file data from str file_name with str file_format and returns a data structure. Currently supported file_format is csv. """
    if file_format == "csv":
        data = child_care_data_csv.read_data_csv(file_name)
    else:
        data = None
        print("Specified file_format is not supported, please look at the api user manual for supported formats!")

    if data is None: 
        raise Exception("data object is of type None!")
    
    return data


def get_data_year(year, data_structure):
    """provides available data for a given year"""
    child_care_data_csv.get_data_year_csv(year, data_structure)

def get_data_year_location(year, location, data_structure):
    """provides available data for a given year and a given location"""
    child_care_data_csv.get_data_year_location_csv(year, location, data_structure)

def get_data_year_age(year, age, data_structure):
    """provides available data for a given year and a given age"""
    child_care_data_csv.get_data_year_age_csv(year, age, data_structure)

#First tests of functions: include this in unittests!
#read_data("/home/hana/develop/projects/my_api_projects/Child_Care_Data/tests/child_care_data.csv", "csv")
#read_data("data", "csv")
#read_data("/home/hana/develop/projects/my_api_projects/Child_Care_Data/tests/child_care_data_corrupted.csv", "csv")