# Python API Filter
This is a Python helper script that can locate the usage of a function/api invocation within the input file. Given inputs in the form of the path to the Python file and the name of the function/API, this script will locate and print the line number of the corresponding function/API invocation within the given file.

## Usages
```
python api_filter.py FILENAME FUNCTION_NAME
```

## Requirements
- Python 3

## Examples
test.py:
![test.py code](https://github.com/StefanusAgus/python_api_filter/blob/master/test_py.PNG?raw=true)

Run command:
```
python api_filter.py test.py KMeans
```

Output:
```
Searching for: 'KMeans' API invocation in:
test.py file...

Found API invocation in line: 18
Found API invocation in line: 21
Found API invocation in line: 28
```
