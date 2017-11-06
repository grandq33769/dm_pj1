# Implemetation of Finding Frequent Item Set
============================================
Command line usage : python3 main.py <data_set> <min_sup> <method> <T> <I> <D>

data set : 'anime' / 'ibm'

    anime : anime.csv

    ibm : IBM synthetic data

min_sup : (0,1)

method : 'fp' / 'apriori'

T (data set = 'ibm') : 10/20

I (data set = 'ibm') : 2/4

D (data set = 'ibm') : 5/10/15/20/25/30

    Not all combination of T/I/D will success, it depends on .data in directory

#Dependency#

* Numpy
* Pandas