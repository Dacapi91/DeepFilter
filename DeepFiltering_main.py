# -*- coding: utf-8 -*-

#============================================================
#
#  Deep Learning BLW Filtering
#  Main
#
#  author: Francisco Perdigon Romero
#  email: fperdigon88@gmail.com
#  github id: fperdigon
#
#===========================================================

import _pickle as pickle

from utils.metrics import MAD, SSD, PRD
from utils import visualization as vs
from utils import data_preparation as dp

from digitalFilters.dfilters import FIR_test_Dataset
from deepFilter.dl_pipeline import train_dl, test_dl

if __name__ == "__main__":

    Dataset = dp.Data_Preparation()

    # dl_experiments = ['Vanilla Linear',
    #                   'Vanilla Non Linear',
    #                   'Inception-like Linear',
    #                   'Inception-like Non Linear',
    #                   'Inception-like Linear and Non Linear',
    #                   'Inception-like Linear and Non Linear Dilated'
    #                   ]

    dl_experiments = ['Vanilla L',
                      'Vanilla NL',
                      'Inception-like L',
                      'Inception-like NL',
                      'Inception-like LANL',
                      'Inception-like LANLD'
                      ]


    for experiment in range(len(dl_experiments)):

        train_dl(Dataset, experiment)

        [X_test, y_test, y_pred] = test_dl(Dataset, experiment)

        test_results = [X_test, y_test, y_pred]

        # Save Results
        with open('test_results_exp_' + str(experiment) +'.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(test_results, output)
        print('Results from experiment ' + str(experiment) + ' saved')


    [X_test_f, y_test_f, y_filter] = FIR_test_Dataset(Dataset)

    test_results_FIR = [X_test_f, y_test_f, y_filter]

    # Save FIR filter results
    with open('test_results_exp_FIR.pkl', 'wb') as output:  # Overwrites any existing file.
        pickle.dump(test_results_FIR, output)
    print('Results from experiment FIR filter saved')


    # Load Results Exp 0
    with open('test_results_exp_0.pkl', 'rb') as input:
        test_exp_0 = pickle.load(input)

    # Load Results Exp 1
    with open('test_results_exp_1.pkl', 'rb') as input:
        test_exp_1 = pickle.load(input)

    # Load Results Exp 2
    with open('test_results_exp_2.pkl', 'rb') as input:
        test_exp_2 = pickle.load(input)

    # Load Results Exp 3
    with open('test_results_exp_3.pkl', 'rb') as input:
        test_exp_3 = pickle.load(input)

    # Load Results Exp 4
    with open('test_results_exp_4.pkl', 'rb') as input:
        test_exp_4 = pickle.load(input)

    # Load Results Exp 5
    with open('test_results_exp_5.pkl', 'rb') as input:
        test_exp_5 = pickle.load(input)


    # Load Result FIR Filter
    with open('test_results_exp_FIR.pkl', 'rb') as input:
        test_exp_FIR = pickle.load(input)



    # DL Metrics

    # Exp 0

    [X_test, y_test, y_pred] = test_exp_0

    SSD_values_DL_exp_0 = SSD(y_test, y_pred)

    MAD_values_DL_exp_0 = MAD(y_test, y_pred)

    PRD_values_DL_exp_0 = PRD(y_test, y_pred)


    # Exp 1

    [X_test, y_test, y_pred] = test_exp_1

    SSD_values_DL_exp_1 = SSD(y_test, y_pred)

    MAD_values_DL_exp_1 = MAD(y_test, y_pred)

    PRD_values_DL_exp_1 = PRD(y_test, y_pred)


    # Exp 2

    [X_test, y_test, y_pred] = test_exp_2

    SSD_values_DL_exp_2 = SSD(y_test, y_pred)

    MAD_values_DL_exp_2 = MAD(y_test, y_pred)

    PRD_values_DL_exp_2 = PRD(y_test, y_pred)


    # Exp 3

    [X_test, y_test, y_pred] = test_exp_3

    SSD_values_DL_exp_3 = SSD(y_test, y_pred)

    MAD_values_DL_exp_3 = MAD(y_test, y_pred)

    PRD_values_DL_exp_3 = PRD(y_test, y_pred)


    # Exp 4

    [X_test, y_test, y_pred] = test_exp_4

    SSD_values_DL_exp_4 = SSD(y_test, y_pred)

    MAD_values_DL_exp_4 = MAD(y_test, y_pred)

    PRD_values_DL_exp_4 = PRD(y_test, y_pred)


    # Exp 5

    [X_test, y_test, y_pred] = test_exp_5

    SSD_values_DL_exp_5 = SSD(y_test, y_pred)

    MAD_values_DL_exp_5 = MAD(y_test, y_pred)

    PRD_values_DL_exp_5 = PRD(y_test, y_pred)


    # Digital Filtering
    # FIR Filtering Metrics
    [X_test, y_test, y_filter] = test_exp_FIR

    SSD_values_FIR = SSD(y_test, y_filter)

    MAD_values_FIR = MAD(y_test, y_filter)

    PRD_values_FIR = PRD(y_test, y_filter)



    # Results Visualization

    SSD_all = [SSD_values_DL_exp_0,
               SSD_values_DL_exp_1,
               SSD_values_DL_exp_2,
               SSD_values_DL_exp_3,
               SSD_values_DL_exp_4,
               SSD_values_DL_exp_5,
               SSD_values_FIR
               ]

    MAD_all = [MAD_values_DL_exp_0,
               MAD_values_DL_exp_1,
               MAD_values_DL_exp_2,
               MAD_values_DL_exp_3,
               MAD_values_DL_exp_4,
               MAD_values_DL_exp_5,
               MAD_values_FIR
               ]

    PRD_all = [PRD_values_DL_exp_0,
               PRD_values_DL_exp_1,
               PRD_values_DL_exp_2,
               PRD_values_DL_exp_3,
               PRD_values_DL_exp_4,
               PRD_values_DL_exp_5,
               PRD_values_FIR]



    Exp_all = dl_experiments + ['FIR Filter']

    #generate_violinplots(SSD_all, Exp_all, 'SSD (au)', log=False)
    #generate_barplot(SSD_all, Exp_all, 'SSD (au)', log=False)
    #generate_boxplot(SSD_all, Exp_all, 'SSD (au)', log=True)
    vs.generate_hboxplot(SSD_all, Exp_all, 'SSD (au)', log=False, set_x_axis_size=(0,41))

    #generate_violinplots(MAD_all, Exp_all, 'MAD (au)', log=False)
    #generate_barplot(MAD_all, Exp_all, 'MAD (au)', log=False)
    #generate_boxplot(MAD_all, Exp_all, 'MAD (au)', log=True)
    vs.generate_hboxplot(MAD_all, Exp_all, 'MAD (au)', log=False)

    #generate_violinplots(PRD_all, Exp_all, 'PRD (au)', log=False)
    #generate_barplot(PRD_all, Exp_all, 'PRD (au)', log=False)
    #generate_boxplot(PRD_all, Exp_all, 'PRD (au)', log=True)
    vs.generate_hboxplot(PRD_all, Exp_all, 'PRD (au)', log=False)


