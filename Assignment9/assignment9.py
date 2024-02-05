# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:39:58 2024

@author: arjun
"""

import time
from multiprocessing import Pool, cpu_count

# def parallelized_code(nums):
#     start_time = time.time()
#     with Pool(processes=cpu_count()) as pool:
#         x = pool.map(approximate_pi, nums)
#     print("The program took: "+str(time.time()-start_time)+ " secs")

def approximate_pi(n):
    start_time = time.time()
    pi_2 = 1
    nom, den = 2.0, 1.0
    for i in range(n):
        pi_2 *= nom / den
        if i % 2:
            nom += 2
        else:
            den += 2
    print(f"It took {time.time()-start_time} secs for {n} iterations")
    return 2*pi_2

nums = [1_822_725, 22_059_421, 32_374_695, 88_754_320, 97_162_66, 200_745_654]

if __name__ == '__main__':
    start_time = time.time()
    with Pool(processes=cpu_count()) as pool:
        x = pool.map(approximate_pi, nums)
    print("The program took: "+str(time.time()-start_time)+ " secs")
