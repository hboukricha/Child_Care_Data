from childcaredatabw import child_care_data # The code to test

def test_child_care_data (data_regression): 
    
    # read the data from csv file
    data_current = child_care_data.read_data("./tests/child_care_data.csv", "csv")
    
    # check regression of provided data
    data_regression.check(data_current)