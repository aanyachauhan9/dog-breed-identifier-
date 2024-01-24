#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: aanya chauhan
# DATE CREATED: 3rd novemeber                               

from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    for filename in listdir(image_dir):
        if not filename.startswith('.'):
            pet_name = ' '.join(word.lower() for word in filename.split('_') if word.isalpha())
            results_dic[filename] = [pet_name]
    return results_dic
