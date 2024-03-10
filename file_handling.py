import pandas as pd
import time
import numpy as np

filename = "BindingDB_All_202402.tsv"
t0 = time.time

dataframe = pd.read_csv(filename, sep="\t", engine="python", on_bad_lines="skip")

print(dataframe.head())

size = len(dataframe)
print(f"File size: {size}.")

n_splits = 10

splitted_df = np.array_split(dataframe, n_splits)

for i, df in enumerate(splitted_df):
    print(f"DataFrame {i+1} has {len(df)} rows.")
    new_filename = f"split_{i+1}.csv"
    df.to_csv(new_filename, index=False)
    print(f"Saved to {filename}.")

t1 = time.time()
rt = t1 - t0
print(f"Runtime (min): {rt/60}")
# Check where to split
# Split up into 10 files
