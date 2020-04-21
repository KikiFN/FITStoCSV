# FitsToCsv

The code takes as input a FITS file so constructed:

Galaxy ID | Redshift | Value 1 | Error value 1 | Value 2 | Error value 2 | ... | Value M | Error value M
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
ID 1 | redshift 1 | record ID 1 value 1 | record ID 1 error 1 | record ID 1 value 2 | record ID 1 error 2 | ... | record ID 2 value M | record ID 2 error M 
ID 2 | redshift 2 | record ID 2 value 1 | record ID 2 error 1 | record ID 2 value 2 | record ID 2 error 2 | ... | record ID 2 value M | record ID 2 error M 
... | ... | ... | ... | ... | ... | ... | ... | ...
ID N | redshift N | record ID N value 1 | record ID N error 1 | record ID N value 2 | record ID N error 2 | ... | record ID N value M | record ID N error M 


Then does a ratio between the value and its error.
In the end it returns a CSV file so constructed (redshift, as in column 1, is discarded):

Galaxy ID | Ratio value 1 | Ratio value 2 | ... | Ratio value J
------------ | ------------- | ------------- | ------------- | -------------
ID 1 | record ID 1 ratio 1 | record ID 1 ratio 2 | ... | record ID 1 ratio J
ID 2 | record ID 2 ratio 1 | record ID 2 ratio 2 | ... | record ID 2 ratio J
... | ... | ... | ... | ...
ID N | record ID N ratio 1 | record ID N ratio 2 | ... | record ID N ratio J

CSV file has comma as delimiter and "" as text highlighters.