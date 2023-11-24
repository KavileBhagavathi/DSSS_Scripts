# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:57:57 2023

@author: arjun
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    csv_data = pd.read_csv(file_path)
    return csv_data

file_path = "census_income_dataset.csv"
data = load_csv(file_path)

df = data.copy()

df = df[~df["AGE"].isnull()]
df = df[~df["RELATIONSHIP"].isnull()]
df = df[~df["EDUCATION"].isnull()]

age_distri = df["AGE"].value_counts().sort_values()
age_bins = [35,40,50,55,60,65,70,75,80,85,90]
age_ranges = pd.cut(age_distri.index, bins=age_bins, right=False)
age_range_distri = age_distri.groupby(age_ranges).sum()

df_age = pd.DataFrame({'Age_Range': age_range_distri.index, 'Frequency': age_range_distri.values})
ax = df_age.plot(x='Age_Range', y='Frequency', kind='bar', color='skyblue', edgecolor='black')
ax.grid(axis='both', alpha=0.5)
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.title('Age Distribution by Range')