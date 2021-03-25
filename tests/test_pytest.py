# @Author: hana.boukricha
# @Date:   2021-03-25 13:06:27
# @Last Modified by:   hana.boukricha
# @Last Modified time: 2021-03-25 22:51:50

from childcaredatabw import child_care_data  # The code to test


def test_child_care_data(data_regression):

    # read the data from csv file
    data_current = child_care_data.read_data("./tests/child_care_data.csv", "csv")

    # check regression of provided data
    data_regression.check(data_current)

    # check input/output of api functions
    assert child_care_data.get_data_year("2007", data_current) == {'Tageseinrichtung': {'Betreute Kinder insgesamt': '379.734', 'unter 3': '26.978', '3 bis unter 6': '281.627', '6 bis unter 14': '71.129', 'Betreute Kinder mit Mittagsverpflegung': '109.388'}, 'Tagespflege': {
        'Betreute Kinder insgesamt': '13.287', 'unter 3': '6.049', '3 bis unter 6': '3.031', '6 bis unter 14': '4.207', 'Betreute Kinder mit Mittagsverpflegung': ' X'}, 'Insgesamt': {'Betreute Kinder insgesamt': '393.021', 'unter 3': '33.027', '3 bis unter 6': '284.658', '6 bis unter 14': '75.336', 'Betreute Kinder mit Mittagsverpflegung': ' X'}}
    
    assert child_care_data.get_data_year_location("2007", "Tageseinrichtung", data_current) == {'Betreute Kinder insgesamt': '379.734', 'unter 3': '26.978', '3 bis unter 6': '281.627',
            '6 bis unter 14': '71.129', 'Betreute Kinder mit Mittagsverpflegung': '109.388'}

    assert child_care_data.get_data_year_location_age("2007", "Tageseinrichtung", "unter 3", data_current) == "26.978"

