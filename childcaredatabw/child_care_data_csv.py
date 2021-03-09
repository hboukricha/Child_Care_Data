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
# @Last Modified time: 2021-03-09 13:24:50

""" This module implements api to retrieve csv formatted data on child care numbers in Baden Wuertemberg """

import re as regex
import pandas as pd


def read_data_csv(file_name):
    """ read csv formatted data from str file_name and returns a pandas DataFrame csv_data. """
    try: 
        csv_data = pd.read_csv(file_name, delimiter=";", skiprows=2, header=None) 
    except Exception as error:
        print(error)
    else:
        return csv_data
   

def get_data_year_csv(year, dataframe):
    pass

def get_data_year_location_csv(year, location, dataframe):
    pass

def get_data_year_age_csv(year, age, dataframe):
    pass