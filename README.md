# Implemetation of Finding Frequent Item Set #

Command line usage : 

python3 main.py <-data_set> <-min_sup> <-method> <-tlen> <-items> <-size>

data set : 'anime' / 'ibm'

    anime : anime.csv

    ibm : IBM synthetic data

min_sup : (0,1)

method : 'fp' / 'apriori'

tlen (data set = 'ibm') : 10/20

    Length of each transaction

items (data set = 'ibm') : 2/4

    Maximum pattern length

d (data set = 'ibm') : 5/10/15/20/25/30

    Data size

Not all combination of T/I/D will success, it depends on .data in directory

## Example ##

python3 main.py anime 0.05 fp

python3 main.py ibm 0.05 apriori 10 4 25

## Dependency ##

* Numpy
* Pandas