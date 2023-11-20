import os
import subprocess
import pandas as pd

file = 'list.txt'

if os.path.exists(file):
    os.remove(file)
    os.system('gdrive files list >> list.txt')
else:
    os.system('gdrive files list >> list.txt')


df = pd.read_csv('list.txt', sep=' ', header=0)

cols = df.columns

for col in cols:
    if col.startswith('Unnamed'):
        df.drop(col, axis=1, inplace=True)

ids = df['Id'].tolist()

for fileid in ids:
    command = f'cd /home/anderdam/gdrive_downloads; gdrive files download --recursive {fileid}'
    subprocess.run(command, shell=True)

