import unittest   # The test framework
from pandas._testing import assert_frame_equal
from childcaredatabw import child_care_data # The code to test
from childcaredatabw import child_care_data_csv # The code to test

# Testing read data functions
class Test_Read_Data(unittest.TestCase):
    
    def test_data_frames(self):
        # test should succeed by giving the following file_name and file_format as input
        file_name = "/home/hana/develop/projects/my_api_projects/Child_Care_Data/tests/child_care_data.csv"
        file_format = "csv"

        # test should fail by giving the following file_name as input
        #file_name = "/home/hana/develop/projects/my_api_projects/Child_Care_Data/tests/child_care_data_corrupted.csv"
        #file_name = "data"
        
        # test should fail by giving the following file_format as input
        #file_format = "txt"

        data = child_care_data.read_data(file_name, file_format)
        data_csv = child_care_data_csv.read_data_csv(file_name) 
        assert_frame_equal(data, data_csv)

if __name__ == '__main__':
    unittest.main()