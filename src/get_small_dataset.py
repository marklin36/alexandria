import pandas as pd
import os
import csv 
import dask

from dask.distributed import progress
import dask.dataframe as dd
from dask.diagnostics import ProgressBar

from dask.distributed import progress

base_path = os.getcwd()
path_file = os.path.join(base_path, 'data/sentiment.csv')
df = dd.read_csv(path_file,  sep='\t', encoding = "ISO-8859-1",na_filter = False,error_bad_lines=False)

with ProgressBar():
    small_df = df.sample(frac=0.01).compute()

small_df.to_csv('sample.csv')
    