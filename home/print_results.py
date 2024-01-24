#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: aanya chauhan
# DATE CREATED: 5th november 

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):

    print("\nSummary for Model: {}\n".format(model))

    print("Total Images: {}".format(results_stats_dic['n_images']))
    print("Dog Images: {}".format(results_stats_dic['n_dogs_img']))
    print("Not-a-Dog Images: {}".format(results_stats_dic['n_notdogs_img']))
    print("% Correct Dogs: {:.2f}%".format(results_stats_dic['pct_correct_dogs']))
    print("% Correct Breed: {:.2f}%".format(results_stats_dic['pct_correct_breed']))
    print("% Match: {:.2f}%".format(results_stats_dic['pct_match']))
    if print_incorrect_dogs and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nIncorrectly Classified Dogs:")
        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print("{} - Actual: {}, Classifier: {}".format(key, results_dic[key][0], results_dic[key][1]))

    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nIncorrectly Classified Dog Breeds:")
        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][2] == 0:
                print("{} - Actual Breed: {}, Classifier Breed: {}".format(key, results_dic[key][0], results_dic[key][1]))

