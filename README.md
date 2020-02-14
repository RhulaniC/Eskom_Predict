# Eskom_Predict Package
Python functions used to analyse and calctulate data from Eskom. These functions process both numerical and text data.

## What you will need
This project runs on the latest version of Python. Before you can start, ensure that the latest version of python is intalled.  

## Intalling the project package from GitHub
 issue this command to install from GitHub:
 pip install git+https://github.com/Xenaschke/Eskom_Predict.git
 
 if you need to install the latest version of this package, use:
 pip install --upgrade git+https://github.com/Xenaschke/Eskom_Predict.git
 
##Running the codes
Once the package is installed into python the following fucntions can be used to get the metrics:

###Fuction 1

###Fuction 2
For this function, you have to first import numpy. The function five_num_summary(items) takes in a list of integers and returns a dictionary of the five number summary. 
####Example
An argument items = [3,5,6,78,8,9,9,6,4,6.8,7,8,9,1] will return {'max': 78.0, 'median': 6.9, 'min': 1.0, 'q1': 5.25, 'q3': 8.75}

###Function 3
This function date_parser(list_dates) takes in a list of datetime strings, extracts the dates of each item in the list, and returns the date in 'yyyy-mm-dd' format.
####Example 
An argument list_dates = ['2019-11-29 12:50:54','2019-11-29 12:46:53''2019-11-29 12:46:10'] will return ['2019-11-29', '2019-11-29', '2019-11-29'].
###Function 4

                 ,
                        
