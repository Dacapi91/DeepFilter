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

from utils.metrics import MAD, SSD, PRD, COS_SIM
from utils import visualization as vs
from utils import data_preparation as dp

from digitalFilters.dfilters import FIR_test_Dataset, IIR_test_Dataset
from deepFilter.dl_pipeline import train_dl, test_dl

if __name__ == "__main__":

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

    Dataset = dp.Data_Preparation()

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

    [X_test_f, y_test_f, y_filter] = IIR_test_Dataset(Dataset)

    test_results_IIR = [X_test_f, y_test_f, y_filter]

    # Save FIR filter results
    with open('test_results_exp_IIR.pkl', 'wb') as output:  # Overwrites any existing file.
        pickle.dump(test_results_IIR, output)
    print('Results from experiment IIR filter saved')


    ####### LOAD EXPERIMENTS #######

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

    # Load Result IIR Filter
    with open('test_results_exp_IIR.pkl', 'rb') as input:
        test_exp_IIR = pickle.load(input)

    ####### Calculate Metrics #######

    signals_id = [110, 210, 410, 810, 1610, 3210, 6410, 12810]

    ecg_signals2plot = []
    ecgbl_signals2plot = []
    dl_signals2plot = []
    fil_signals2plot = []

    # DL Metrics

    # Exp 0

    [X_test, y_test, y_pred] = test_exp_0

    SSD_values_DL_exp_0 = SSD(y_test, y_pred)

    MAD_values_DL_exp_0 = MAD(y_test, y_pred)

    PRD_values_DL_exp_0 = PRD(y_test, y_pred)

    COS_SIM_values_DL_exp_0 = COS_SIM(y_test, y_pred)

    # Exp 1

    [X_test, y_test, y_pred] = test_exp_1

    SSD_values_DL_exp_1 = SSD(y_test, y_pred)

    MAD_values_DL_exp_1 = MAD(y_test, y_pred)

    PRD_values_DL_exp_1 = PRD(y_test, y_pred)

    COS_SIM_values_DL_exp_1 = COS_SIM(y_test, y_pred)

    # Exp 2

    [X_test, y_test, y_pred] = test_exp_2

    SSD_values_DL_exp_2 = SSD(y_test, y_pred)

    MAD_values_DL_exp_2 = MAD(y_test, y_pred)

    PRD_values_DL_exp_2 = PRD(y_test, y_pred)

    COS_SIM_values_DL_exp_2 = COS_SIM(y_test, y_pred)

    # Exp 3

    [X_test, y_test, y_pred] = test_exp_3

    SSD_values_DL_exp_3 = SSD(y_test, y_pred)

    MAD_values_DL_exp_3 = MAD(y_test, y_pred)

    PRD_values_DL_exp_3 = PRD(y_test, y_pred)

    COS_SIM_values_DL_exp_3 = COS_SIM(y_test, y_pred)

    # Exp 4

    [X_test, y_test, y_pred] = test_exp_4

    SSD_values_DL_exp_4 = SSD(y_test, y_pred)

    MAD_values_DL_exp_4 = MAD(y_test, y_pred)

    PRD_values_DL_exp_4 = PRD(y_test, y_pred)

    COS_SIM_values_DL_exp_4 = COS_SIM(y_test, y_pred)

    # Exp 5 (Best)

    [X_test, y_test, y_pred] = test_exp_5

    SSD_values_DL_exp_5 = SSD(y_test, y_pred)

    MAD_values_DL_exp_5 = MAD(y_test, y_pred)

    PRD_values_DL_exp_5 = PRD(y_test, y_pred)

    COS_SIM_values_DL_exp_5 = COS_SIM(y_test, y_pred)

    for id in signals_id:
        ecgbl_signals2plot.append(X_test[id])
        ecg_signals2plot.append(y_test[id])
        dl_signals2plot.append(y_pred[id])

    # Digital Filtering

    # FIR Filtering Metrics
    [X_test, y_test, y_filter] = test_exp_FIR

    SSD_values_FIR = SSD(y_test, y_filter)

    MAD_values_FIR = MAD(y_test, y_filter)

    PRD_values_FIR = PRD(y_test, y_filter)

    COS_SIM_values_FIR = COS_SIM(y_test, y_filter)

    # IIR Filtering Metrics (Best)
    [X_test, y_test, y_filter] = test_exp_IIR

    SSD_values_IIR = SSD(y_test, y_filter)

    MAD_values_IIR = MAD(y_test, y_filter)

    PRD_values_IIR = PRD(y_test, y_filter)

    COS_SIM_values_IIR = COS_SIM(y_test, y_filter)

    for id in signals_id:
        fil_signals2plot.append(y_filter[id])

    ####### Results Visualization #######

    SSD_all = [SSD_values_FIR,
               SSD_values_IIR,
               SSD_values_DL_exp_0,
               SSD_values_DL_exp_1,
               SSD_values_DL_exp_2,
               SSD_values_DL_exp_3,
               SSD_values_DL_exp_4,
               SSD_values_DL_exp_5
               ]

    MAD_all = [MAD_values_FIR,
               MAD_values_IIR,
               MAD_values_DL_exp_0,
               MAD_values_DL_exp_1,
               MAD_values_DL_exp_2,
               MAD_values_DL_exp_3,
               MAD_values_DL_exp_4,
               MAD_values_DL_exp_5
               ]

    PRD_all = [PRD_values_FIR,
               PRD_values_IIR,
               PRD_values_DL_exp_0,
               PRD_values_DL_exp_1,
               PRD_values_DL_exp_2,
               PRD_values_DL_exp_3,
               PRD_values_DL_exp_4,
               PRD_values_DL_exp_5
               ]

    CORR_all = [COS_SIM_values_FIR,
                COS_SIM_values_IIR,
                COS_SIM_values_DL_exp_0,
                COS_SIM_values_DL_exp_1,
                COS_SIM_values_DL_exp_2,
                COS_SIM_values_DL_exp_3,
                COS_SIM_values_DL_exp_4,
                COS_SIM_values_DL_exp_5
                ]

    Exp_all = ['FIR Filter', 'IIR Filter'] + dl_experiments

    vs.generate_hboxplot(SSD_all, Exp_all, 'SSD (au)', log=False, set_x_axis_size=(0, 41))

    vs.generate_hboxplot(MAD_all, Exp_all, 'MAD (au)', log=False)

    vs.generate_hboxplot(PRD_all, Exp_all, 'PRD (au)', log=False)

    vs.generate_hboxplot(CORR_all, Exp_all, 'Cosine Similarity (0-1)', log=False)

    vs.generate_table(SSD_all, Exp_all, title='SSD results table')
    vs.generate_table(MAD_all, Exp_all, title='MAD results table')
    vs.generate_table(PRD_all, Exp_all, title='PRD results table')
    vs.generate_table(CORR_all, Exp_all, title='COS SIM results table')

    for i in range(len(signals_id)):
        vs.ecg_view(ecg=ecg_signals2plot[i],
                    ecg_blw=ecgbl_signals2plot[i],
                    ecg_dl=dl_signals2plot[i],
                    ecg_f=fil_signals2plot[i],
                    signal_name=None,
                    beat_no=None)

        vs.ecg_view_diff(ecg=ecg_signals2plot[i],
                         ecg_blw=ecgbl_signals2plot[i],
                         ecg_dl=dl_signals2plot[i],
                         ecg_f=fil_signals2plot[i],
                         signal_name=None,
                         beat_no=None)





