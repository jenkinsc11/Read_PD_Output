#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:12:15 2017

@author: jenkinsc11
"""
import csv

filename = input("Enter filename location:")

with open(filename) as file:
    f = open("filtered_protein_data.txt", 'w')
    for line in csv.reader(file, delimiter="\t"):
        f.writelines(line[1] + '\t')
        f.writelines(line[3] + '\t') 
        f.writelines(line[4] + '\t') 
        f.writelines(line[7] + '\t') 
        f.writelines(line[9] + '\t') 
        f.writelines(line[10] + '\t') 
        f.writelines(line[12] + '\t') 
        f.writelines(line[13] + '\t' + '\n')
    f.close

