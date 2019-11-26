This datasetcontains time-series data from the US since 2000 till 2010. How much US$ have been lost every year in tax evasion. Also, includes the Tax Revenue Percentage per country and the current tax rate per country for corporate, and average income. 

## Data
The data is sourced from 
* https://en.wikipedia.org/wiki/List_of_countries_by_tax_rates
* https://en.wikipedia.org/wiki/List_of_countries_by_tax_revenue_to_GDP_ratio
* https://en.wikipedia.org/wiki/Tax_evasion_in_the_United_States

The data is measured in Percentage ("%") and in US$ Billion. The tables further explanation on the headers.
If data is "0", it means there no data on it.

--------------------------------------------------------------------------------------------------------------------------------

## Preparation

Inside the "Process directory", there is a file called ```process.py``` which will scrape 3 tables from 3 different sources and clean it up to concrete values and put it into 3 csv files.

##### Requires:
1. Python
2. Visualstudio / Jupyter notebook / or any platform that works with python.

##### Necessary python modules for this: 
* bs4
* csv
* requests

##### Instructions:
* Download "requirements.txt".
* Go to your terminal and use the following command ```pip install requirements.txt```
* Copy process.py script
* Open in jupyter notebook, python shell, VS code, or any preferred platform.
* Paste and run the code
* 3 CSV´s file will be saved in document where your terminal is at the moment.


----------------------------------------------------------------------------------------------------------------------------------------

## Licence
This Data Package is made available under the Public Domain Dedication and License v1.0 

