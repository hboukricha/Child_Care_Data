# childcaredatabw
childcaredatabw is an integrable Python api by which data can be queried from a given csv file with child care numbers within Baden Wuertemberg, e.g., by year, location, and age.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install childcaredatabw. 

```bash
python3 -m pip install -i https://test.pypi.org/simple/ childcaredatabw==0.0.5
```

## Usage

```python
import childcaredatabw.child_care_data

child_care_data.read_data('file_name', 'file_format') # returns 'data', e.g., pandas DataFrame if file_format == csv
child_care_data.get_data_year('year') # returns 'data', e.g., pandas DataFrame if file_format == csv, for a given year
child_care_data.get_data_year_location('year', 'location') # returns 'data', e.g., pandas DataFrame if file_format == csv, for a given year and location
child_care_data.get_data_year_age('year', 'age') # returns 'data', e.g., pandas DataFrame if file_format == csv, for a given year and age
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)