#!/usr/bin/env python3

'''
Dog DNA
'''

# time -f '%e' ./dog_dna.py > dog_dna.txt
# ./dog_dna.py > dog_dna.txt


import pandas as pd


FILE_RAW = 'dog_dna.csv'
df = pd.read_csv(FILE_RAW)

print(pd.crosstab(df['Dog 1 A'], df['Dog 1 G']), '\n')
print(pd.crosstab(df['Dog 1 A'], df['Dog 1 G'],
      margins=True,
      margins_name='Total',
      dropna=True), '\n')
print(pd.crosstab(df['Dog 1 A'], df['Dog 1 G'],
      margins=True,
      margins_name='Total',
      dropna=True,
      normalize=True,).round(4)*100)

