'''
Main module of experiment for running different parameter of algorithm
Date : 2017/11/5
'''
import sys
import time
import logging as log
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

from data import anime, ibm
from fqits.apriori import Apriori
from fqits.fp_growth import FPgrowth
C_MS = np.linspace(0.01, 0.2, 39)
C_MS2 = np.linspace(0.04, 0.09, 11)
C_S = np.linspace(1000, 12000, 12)
C_S2 = np.linspace(5, 30, 6)
C_L = np.linspace(0.05, 0.2, 4)

MIN_SUP = C_MS2
SIZE = C_S2
LEN = C_L
T = 10
I = 4


def ibm_size_test(min_sup):
    '''
    Args:
        data(tuple(tuple)):Transaction data to be tested
    Returns:
        atime(list): Time result(sec) of Apriori in vary SIZE
        ftime(list): Time result(sec) of FP-growth in vary SIZE
    '''
    atime = list()
    ftime = list()
    for size in SIZE:
        num = int(size)
        print('Data_size {} begin ...'.format(num))
        data = ibm.open_data(T, I, num)
        apriori = Apriori(data, min_sup)

        print('Apriori begin ...')
        time1 = time.time()
        apriori.run()
        end1 = time.time() - time1
        print('Apriori finish ... Time:{}'.format(end1))

        fpg = FPgrowth(data, min_sup)

        print('FP-growth begin ...')
        time2 = time.time()
        fpg.run()
        end2 = time.time() - time2
        print('FP-growth finish ... Time:{}'.format(end2))

        atime.append(end1)
        ftime.append(end2)

    # Plot
    X = SIZE
    Y1 = atime
    Y2 = ftime

    plt.plot(X, Y1, '-ro', label='Apriori')
    plt.plot(X, Y2, '-bo', label='FP-growth')
    plt.legend()
    plt.ylim(0, max(atime) + 1)
    plt.xlabel("Data Size(thousand)")
    plt.ylabel("time(sec.)")

    plt.show()

    return atime, ftime


def size_test(data):
    '''
    Args:
        data(tuple(tuple)):Transaction data to be tested
    Returns:
        atime(list): Time result(sec) of Apriori in vary SIZE
        ftime(list): Time result(sec) of FP-growth in vary SIZE
    '''
    atime = list()
    ftime = list()
    for size in SIZE:
        num = int(size)
        print('Data_size {} begin ...'.format(num))
        apriori = Apriori(data[:num], 0.05)

        print('Apriori begin ...')
        time1 = time.time()
        apriori.run()
        end1 = time.time() - time1
        print('Apriori finish ... Time:{}'.format(end1))

        fpg = FPgrowth(data[:num], 0.05)

        print('FP-growth begin ...')
        time2 = time.time()
        fpg.run()
        end2 = time.time() - time2
        print('FP-growth finish ... Time:{}'.format(end2))

        atime.append(end1)
        ftime.append(end2)

    # Plot
    X = SIZE
    Y1 = atime
    Y2 = ftime

    plt.plot(X, Y1, '-ro', label='Apriori')
    plt.plot(X, Y2, '-bo', label='FP-growth')
    plt.legend()
    plt.ylim(0, max(atime) + 1)
    plt.xlabel("Data Size(transaction)")
    plt.ylabel("time(sec.)")

    plt.show()

    return atime, ftime


def minsup_test(data):
    '''
    Args:
        data(tuple(tuple)):Transaction data to be tested
    Returns:
        atime(list): Time result(sec) of Apriori in vary MIN_SUP
        ftime(list): Time result(sec) of FP-growth in vary MIN_SUP
    '''
    atime = list()
    ftime = list()
    for sup in MIN_SUP:
        print('Min_sup {:.4f} begin ...'.format(sup))
        apriori = Apriori(data, sup)

        print('Apriori begin ...')
        time1 = time.time()
        apriori.run()
        end1 = time.time() - time1
        print('Apriori finish ... Time:{}'.format(end1))

        fpg = FPgrowth(data, sup)

        print('FP-growth begin ...')
        time2 = time.time()
        fpg.run()
        end2 = time.time() - time2
        print('FP-growth finish ... Time:{}'.format(end2))

        atime.append(end1)
        ftime.append(end2)

    # Plot
    X = MIN_SUP * 100
    Y1 = atime
    Y2 = ftime

    plt.plot(X, Y1, '-ro', label='Apriori')
    plt.plot(X, Y2, '-bo', label='FP-growth')
    plt.legend()
    plt.ylim(0, max(atime))
    plt.xlabel("Minimum Support(%)")
    plt.ylabel("time(sec.)")

    plt.show()

    return atime, ftime


def len_test(data):
    '''
    Args:
        data(tuple(tuple)):Transaction data to be tested
    Returns:
        r_count({int:counter}): Return dict contain counters reference by the min_sup
    '''
    r_dict = dict()
    _, ax = plt.subplots()
    for min_sup in LEN:
        fpg = FPgrowth(data, min_sup)
        result = fpg.run()
        c_lis = list(map(len, result.keys()))
        counter = Counter(c_lis)
        sort = sorted(counter.items(), key=lambda x: x[0])
        r_dict.update({min_sup: sort})

        x = [0] + [i[0] for i in sort] + [len(counter) + 1]
        y = [0] + [i[1] for i in sort] + [0]
        ax.bar(x, y, label=min_sup, zorder=10)

    plt.ylim(0, 150)
    plt.xlabel("Lenght of frequent pattern")
    plt.ylabel("Number of frequent pattern")
    plt.legend()
    plt.show()

    return r_dict


if __name__ == '__main__':
    log.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=log.INFO)
    if sys.argv[1] == 'anime':
        DATA = anime.open_data(anime.zscore)
    elif sys.argv[1] == 'ibm':
        DATA = ibm.open_data(int(sys.argv[4]), int(
            sys.argv[5]), int(sys.argv[6]))

    if sys.argv[3] == 'fp':
        RESULT = FPgrowth(DATA, float(sys.argv[2])).run()
    elif sys.argv[3] == 'apriori':
        RESULT = Apriori(DATA, float(sys.argv[2])).run()

    with open('output.txt', 'w') as file:
        for key, value in sorted(RESULT.items(), key=lambda x: -RESULT[x[0]]):
            STR = "{} {} {}".format(
                list(key), value, (value / len(DATA)) * 100)
            print(STR)
            file.writelines(STR + '\n')

    # AT, FT = ibm_size_test(0.05)
    # for support, at, ft in zip(LEN, AT, FT):
    #     print('{:.3f} {:-3.3f} {:-3.3f}'.format(support, at, ft))

    # r_dict = len_test(DATA)
    # for support, count in r_dict.items():
    #     print('{:.3f} {}'.format(support, str(count)))
