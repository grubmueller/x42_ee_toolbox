# Michael Grubmüller
# May, 2025

# ATTENTION: currently only working on macOS

from glob import glob
import os

rawconv_dir = 'rawconv-mac'
source_list = glob('**/*.hp42s', recursive=True)
for source_file in source_list:
    os.system(f'{rawconv_dir}/txt2raw {source_file}')
