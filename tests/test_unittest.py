import unittest   # The test framework
from pandas._testing import assert_frame_equal

from childcaredatabw import child_care_data # The code to test
from childcaredatabw import child_care_data_csv # The code to test

# Testing read and filter data functions
class Test_Read_Filter_Data(unittest.TestCase):
    
    def test_data_frames(self):
        # test should succeed by giving the following example file_name, file_format, year, location, and age as input
        file_name = "/home/hana/develop/projects/my_api_projects/Child_Care_Data/tests/child_care_data.csv"
        file_format = "csv"
        year = "2007" # possible values from '2007' to '2020'. Note that possible test optimization: iterate through all year values!
        location = "Insgesamt" # possible values 'Tageseinrichtung', 'Tagespflege', 'Insgesamt'. Note that possible test optimization: iterate through all location values!
        age = "unter 3" # possible values 'unter 3', '3 bis unter 6', '6 bis unter 14'. Note that possible test optimization: iterate through all age values!

        # test should fail by giving the following file_name as input
        # corresponding exception is catched by implemented code
        #file_name = "/home/hana/develop/projects/my_api_projects/Child_Care_Data/tests/child_care_data_corrupted.csv"
        #file_name = "data"
        #file_name = ""
        
        # test should fail by giving the following file_format as input
        # corresponding exception is catched by implemented code
        #file_format = "txt"
        #file_format = ""

        # test should fail by giving the following year as input
        # corresponding exception is catched by implemented code
        #year = "2021" # year not included within data
        #year = ""

        # test should fail by giving the following location as input
        # corresponding exception is catched by implemented code
        #location = "any" # location not included within data
        #location = ""

        # test should fail by giving the following age as input
        # corresponding exception is catched by implemented code
        #age = "any" # age not included within data
        #age = ""

        # tesing read data frames
        data = child_care_data.read_data(file_name, file_format)
        data_csv = child_care_data_csv.read_data_csv(file_name) 
        assert_frame_equal(data, data_csv)
       
        # tesing get_data_year data frames
        data_year = child_care_data.get_data_year(year, data, file_format)
        data_year_csv = child_care_data_csv.get_data_year_csv(year, data)
        assert_frame_equal(data_year, data_year_csv)

        # testing get_data_year_location data frames
        data_year_location = child_care_data.get_data_year_location(year, location, data, file_format)
        data_year_location_csv = child_care_data_csv.get_data_year_location_csv(year, location, data)
        assert_frame_equal(data_year_location, data_year_location_csv)

        # testing get_data_year_age data frames
        data_year_age = child_care_data.get_data_year_age(year, age, data, file_format)
        data_year_age_csv = child_care_data_csv.get_data_year_age_csv(year, age, data)
        assert_frame_equal(data_year_age, data_year_age_csv)

if __name__ == '__main__':
    unittest.main()