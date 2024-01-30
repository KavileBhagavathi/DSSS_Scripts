#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:40:27 2024

@author: fo55pahy
"""
from multiprocessing import Pool
from multiprocessing import cpu_count
import numpy as np
from skimage import data, color
from skimage.transform import resize
imgs = np.uint8(data.lfw_subset()*255)
new_size = (imgs[1].shape[0]//2, imgs[1].shape[1]//2)
res_im = []
def res_skimage(imgs):
    iterand = [im for im in imgs]
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(imresize,iterand)
    #global res_im
    return np.asarray(result)

def imresize(im):
    #print("resizing image. Input shape: "+str(im.shape)+" resize shape: "+str(new_size))
    #res_im.append(resize(im, new_size, anti_aliasing=True))
    return resize(im, new_size, anti_aliasing=True)
def res_skimage1(imgs):
    new_size = (imgs[1].shape[0]//2, imgs[1].shape[1]//2)
    res_im = []
    for im in imgs:
        image_resized = resize(im, new_size, anti_aliasing=True)
        res_im.append(image_resized)
    return np.asarray(res_im)
