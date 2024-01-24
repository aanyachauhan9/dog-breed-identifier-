#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:  Aanya chauhan 
# DATE CREATED: 3rd november'23                                

def calculates_results_stats(results_dic):
 
    num_images = len(results_dic)
    num_correct_dogs = 0
    num_dog_images = 0
    num_correct_non_dogs = 0
    num_non_dog_images = 0
    num_correct_breed = 0
    num_label_matches = 0

    for key in results_dic:
        is_dog = results_dic[key][3] == 1
        is_correct_dog = is_dog and results_dic[key][4] == 1
        is_non_dog = results_dic[key][3] == 0
        is_correct_non_dog = is_non_dog and results_dic[key][4] == 0
        is_correct_breed = is_dog and results_dic[key][2] == 1
        is_label_match = results_dic[key][2] == 1

        num_correct_dogs += is_correct_dog
        num_dog_images += is_dog
        num_correct_non_dogs += is_correct_non_dog
        num_non_dog_images += is_non_dog
        num_correct_breed += is_correct_breed
        num_label_matches += is_label_match

    pct_correct_dogs = (num_correct_dogs / num_dog_images) * 100 if num_dog_images > 0 else 0
    pct_correct_non_dogs = (num_correct_non_dogs / num_non_dog_images) * 100 if num_non_dog_images > 0 else 0
    pct_correct_breed = (num_correct_breed / num_dog_images) * 100 if num_dog_images > 0 else 0
    pct_match = (num_label_matches / num_images) * 100 if num_images > 0 else 0

    results_stats_dic = {
        'n_images': num_images,
        'n_dogs_img': num_dog_images,
        'n_notdogs_img': num_non_dog_images,
        'n_correct_dogs': num_correct_dogs,
        'n_correct_notdogs': num_correct_non_dogs,
        'n_correct_breed': num_correct_breed,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_notdogs': pct_correct_non_dogs,
        'pct_correct_breed': pct_correct_breed,
        'pct_match': pct_match
    }
    return results_stats_dic
