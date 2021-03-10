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
# @Last Modified time: 2021-03-10 15:39:27

""" This module provides an integrable api library to retrieve data on child care numbers in Baden Wuertemberg """

from childcaredatabw import child_care_data_csv

def read_data(file_name, file_format):
    """ read the file data from str file_name with str file_format and return a data structure. Currently supported file_format is csv. """
    if file_name == "" or file_format == "":
        # if file_name or file_format are empty raise exception and stop execution
        raise Exception("function child_care_data.read_data: file_name or file_format are empty!")

    if file_format == "csv":
        data = child_care_data_csv.read_data_csv(file_name)
    else:
        # if file_format not supported set data object to None (null)
        data = None
        print("function child_care_data.read_data: Specified file_format is not supported, please look at the api user manual for supported formats!")

    if data is None:
        # if data object is None (null) raise exception and stop execution
        raise Exception("function child_care_data.read_data: data object is of type None!")
    
    return data


def get_data_year(year, data_structure, data_format):
    """ read data_structure and return data_year including data for str year. Read data_structure with respect to str data_format. """
    if year == "" or data_format == "":
        # if year or data_format are empty raise exception and stop execution
        raise Exception("function child_care_data.get_data_year: year or data_format are empty!")

    if data_format == "csv":
        data_year = child_care_data_csv.get_data_year_csv(year, data_structure)
    else:
        # if data_format not supported set data object to None (null)
        data_year = None
        print("function child_care_data.get_data_year: Specified data_format is not supported, please look at the api user manual for supported formats!")
    
    if data_year is None:
        # if data object is None (null) raise exception and stop execution
        raise Exception("function child_care_data.get_data_year: data object is of type None!")
    
    return data_year


def get_data_year_location(year, location, data_structure, data_format):
    """ read data_structure and return data_year_location including data for str year and str location. Read data_structure with respect to str data_format. """
    if year == "" or location == "" or data_format == "":
        # if year or location or data_format are empty raise exception and stop execution
        raise Exception("function child_care_data.get_data_year_location: year or location or data_format are empty!")
    
    if data_format == "csv":
        data_year_location = child_care_data_csv.get_data_year_location_csv(year, location, data_structure)
    else:
        # if data_format not supported set data object to None (null)
        data_year_location = None
        print("function child_care_data.get_data_year_location: Specified data_format is not supported, please look at the api user manual for supported formats!")
    
    if data_year_location is None:
        # if data object is None (null) raise exception and stop execution
        raise Exception("function child_care_data.get_data_year_location: data object is of type None!") 
    
    return data_year_location


def get_data_year_age(year, age, data_structure, data_format):
    """ read data_structure and return data_year_age including data for str year and str age. Read data_structure with respect to str data_format. """
    if year == "" or age == "" or data_format == "":
        # if year or age or data_format are empty raise exception and stop execution
        raise Exception("function child_care_data.get_data_year_age: year or age or data_format are empty!")
    
    if data_format == "csv":
        data_year_age = child_care_data_csv.get_data_year_age_csv(year, age, data_structure)
    else:
        # if data_format not supported set data object to None (null)
        data_year_age = None
        print("function child_care_data.get_data_year_age: Specified data_format is not supported, please look at the api user manual for supported formats!")
    
    if data_year_age is None:
        # if data object is None (null) raise exception and stop execution
        raise Exception("function child_care_data.get_data_year_age: data object is of type None!") 
    
    return data_year_age