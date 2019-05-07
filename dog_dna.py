#!/usr/bin/env python3

'''
Dog DNA
'''

# time -f '%e' ./dog_dna.py > dog_dna.txt
# ./dog_dna.py > dog_dna.txt


import pandas as pd


pd.options.display.max_rows = None
pd.options.display.max_columns = None
pd.set_option('display.width', 1000)

FILE_RAW = 'dog_dna_raw.csv'
FILE_MUNGED= 'dog_dna_munged.csv'
USECOLS = ['Dog 1 A', 'Dog 1 G', 'Dog 2 A', 'Dog 2 G']
df = pd.read_csv(FILE_RAW, usecols=USECOLS)


labels = df.columns
df['Dog1'] = df['Dog 1 A'] + df['Dog 1 G']
df['Dog2'] = df['Dog 2 A'] + df['Dog 2 G']
df = df.drop(columns=labels)
df.to_csv(FILE_MUNGED)


print(pd.crosstab(df['Dog1'], df['Dog2']), '\n')
print(pd.crosstab(df['Dog1'], df['Dog2'],
      margins=True,
      margins_name='Total',
      dropna=True), '\n')
print(pd.crosstab(df['Dog1'], df['Dog2'],
      margins=True,
      margins_name='Total',
      dropna=True,
      normalize=True,).round(4)*100)
