#!/usr/bin/env python3

'''
Dog DNA
'''

# time -f '%e' ./dog_dna.py > dog_dna.txt
# ./dog_dna.py > dog_dna.txt


from datetime import datetime
start_time = datetime.now()


import pandas as pd


FILE_RAW = 'dog_dna.csv'


df = pd.read_csv(FILE_RAW)


end_time = datetime.now()
(end_time - start_time).total_seconds()
