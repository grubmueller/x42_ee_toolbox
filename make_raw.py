# Michael Grubmüller
# September, 2024

from glob import glob
import os
import shutil

# Clear /raw folder
raw_list = glob('raw/*.raw')
print(f'Delete {len(raw_list)} old raw files.')
for raw_file in raw_list:
    os.remove(raw_file)

# Make raw files of all .hp42s source files
source_list = glob('**/*.hp42s', recursive=True)
print(f'Translate {len(source_list)} source files.')
for source_file in source_list:
    os.system(f'txt2raw {source_file}')
    
# Move all raw files to /raw directory
os.makedirs('raw', exist_ok=True)
raw_list = glob('**/*.raw', recursive=True)
print(f'Move {len(raw_list)} raw files.')
for raw_file in raw_list:
    shutil.move(raw_file, 'raw')
