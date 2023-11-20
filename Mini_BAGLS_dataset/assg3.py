# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:36:18 2023

@author: arjun
"""

import os
import json
import random 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def load_baglsfolder():
    """Function to return the list with all files inside the directory"""
    BAGLS_PATH = r"""Mini_BAGLS_dataset/"""
    files = os.listdir(BAGLS_PATH)
    return files

def file_seg(files):
    meta = []
    png = []
    seg = []
    for file in files:
        if file[-4:] == 'meta':
            meta.append(file)
        elif file[-3:] == 'png':
            if file[-7:] == 'seg.png':
                seg.append(file)
            else:
                png.append(file)
        else:
            pass
    return meta, png, seg

def choose_random_png(png):
    rand_png = random.choice(png)
    return rand_png

def retrieve_seg_meta(rand_png,seg,meta):
    for segfile in seg:
        if rand_png[0:rand_png.index('.')] == segfile[0:segfile.index('_')]:
            return_seg = segfile
    for metafile in meta:
        if rand_png[0:rand_png.index('.')] == metafile[0:metafile.index('.')]:
            return_meta = metafile
    return return_seg,return_meta
file_list = load_baglsfolder()
meta,png,seg = file_seg(file_list)
rand_png = choose_random_png(png)
rand_seg, rand_meta = retrieve_seg_meta(rand_png, seg, meta)

num_of_images = 4
chosen_images = {}
for i in range(num_of_images):
    rand_png = choose_random_png(png)
    rand_seg, rand_meta = retrieve_seg_meta(rand_png, seg, meta)
    chosen_images.update({i:{"png":rand_png,"seg":rand_seg,"meta":rand_meta}})

def load_png_file(file_name):
    image = mpimg.imread(f"Mini_BAGLS_dataset/{file_name}")
    return image
def load_meta_file(file_name):
    metadata = open(f"Mini_BAGLS_dataset/{file_name}")
    return metadata