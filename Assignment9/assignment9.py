#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:40:27 2024

@author: fo55pahy
"""
import time
from multiprocessing import Pool
from multiprocessing import cpu_count
import numpy as np
from skimage import data, color
from skimage.transform import resize
from numba import njit
from numba.typed import List
imgs = np.uint8(data.lfw_subset()*255)
new_size = (imgs[1].shape[0]//2, imgs[1].shape[1]//2)
res_im = []
def res_skimage(imgs):
    start_time = time.time()
    iterand = [im for im in imgs]
    with Pool() as pool:
        result = pool.imap(imresize,iterand)
    #global res_im
    print("The program took: "+str(time.time()-start_time)+ " secs")
    return np.asarray(result)

def imresize(im):
    #print("resizing image. Input shape: "+str(im.shape)+" resize shape: "+str(new_size))
    #res_im.append(resize(im, new_size, anti_aliasing=True))
    return resize(im, new_size, anti_aliasing=True)
def res_skimage1(imgs):
    start_time = time.time()
    new_size = (imgs[1].shape[0]//2, imgs[1].shape[1]//2)
    res_im = []
    for im in imgs:
        image_resized = resize(im, new_size, anti_aliasing=True)
        res_im.append(image_resized)
    print("The program took: "+str(time.time()-start_time)+ " secs")
    return np.asarray(res_im)
def parallelized_code(nums):
    start_time = time.time()
    with Pool(processes=cpu_count()) as pool:
        x = pool.map(approximate_pi, nums)
    print("The program took: "+str(time.time()-start_time)+ " secs")

def approximate_pi(n):
    pi_2 = 1
    nom, den = 2.0, 1.0
    for i in range(n):
        pi_2 *= nom / den
        if i % 2:
            nom += 2
        else:
            den += 2
    return 2*pi_2



def serial_execcution(nums):
    pi_list = []
    for num in nums:
        pi = approximate_pi(num)
        pi_list.append(pi)
    return pi_list
############For Task 3 and 4############################
import time
from numba import njit
from numba.typed import List

@njit
def serial_execcution_numba(nums):
    pi_2 = 1
    pi_list = []
    nom, den = 2.0, 1.0
    for num in nums:
        for i in range(num):
            pi_2 *= nom / den
            if i % 2:
                nom += 2
            else:
                den += 2
        pi_2 = 2*pi_2
        pi_list.append(pi_2)
    return pi_list
start_time = time.time()
nums = [1_822_725, 22_059_421, 32_374_695,
88_754_320, 97_162_66, 200_745_654]
nums_list_for_numba = List()
[nums_list_for_numba.append(a) for a in nums]
pi_list = serial_execcution_numba(nums_list_for_numba)
print(f"The program took {time.time()-start_time} secs")


