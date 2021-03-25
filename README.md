# childcaredatabw
childcaredatabw is an integrable python api by which data can be queried from a given csv file 
with child care numbers within Baden-Wurtemberg, e.g., by year, location, and age.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install childcaredatabw and its dependencies.

```bash
python3 -m pip install pandas
python3 -m pip install -i https://test.pypi.org/simple/ childcaredatabw==0.0.5
```

## Usage

```python
from childcaredatabw import child_care_data

data = child_care_data.read_data(file_name="test.csv", file_format="csv") # returns dictionary of data for file_format csv
print (child_care_data.get_data_year(year='2016', data_structure=data) # returns dictionary of data within a given year
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)