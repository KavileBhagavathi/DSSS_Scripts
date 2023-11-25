# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:57:57 2023

@author: arjun
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
def load_csv(file_path):
    csv_data = pd.read_csv(file_path)
    return csv_data

file_path = "census_income_dataset.csv"
data = load_csv(file_path)

df = data.copy()
############# Age Distribution ################################################
df = df.sort_values(by='AGE')
age_counts = df['AGE'].value_counts().sort_index()
age_bins = [17, 25, 35, 45, 55, 65, 75, 85, 95]
age_labels = ['17', '25', '35', '45', '55', '65', '75', '85','95']
# Create a bar plot for age distribution
plt.hist(age_counts.index, bins=age_bins, weights=age_counts.values, color='skyblue', edgecolor='black', align='mid')

# Set custom x-axis tick labels
plt.xticks(age_bins, age_labels)

# Set labels and title
plt.xlabel('Age Range')
plt.ylabel('Number of Respondents')
plt.title('Age Distribution Histogram')
plt.savefig('AgeDistri.svg', format='svg')
plt.show()
###################### Relationship Status ####################################

relationship_counts = df["RELATIONSHIP"].value_counts().sort_index()
colors = plt.cm.Set3.colors
wedges, texts, autotexts = plt.pie(relationship_counts.values,labels=relationship_counts.index,
        autopct='%1.1f%%', startangle=90, colors=colors)

# Equal aspect ratio ensures that the pie chart is circular.
plt.axis('equal')
# Set title
plt.title('Relationship Status Distribution',pad = 20)
plt.savefig('RelationshipStatus.svg', format='svg')
# Show the plot
plt.show()
###################### Educational Level ######################################
df_salary = df[["SALARY","EDUCATION"]]
df_salary["Counter"] = 1
#condition = df_salary["SALARY"] == " >50K"
#df_salary.loc[~condition,"SALARY_GREAT_50"] = 0
grouped_salary_df = df_salary.groupby(["SALARY","EDUCATION"]).sum().reset_index()

education_order = [' Preschool',' 1st-4th', ' 5th-6th', ' 7th-8th',' 9th',
                   ' 10th', ' 11th', ' 12th', ' HS-grad',' Prof-school',' Bachelors',
                   ' Some-college',' Masters',' Assoc-acdm', ' Assoc-voc',
                   ' Doctorate'] 

grouped_salary_df['EDUCATION'] = pd.Categorical(grouped_salary_df['EDUCATION'], 
                                                categories=education_order, 
                                                ordered=True)
pivot_df = grouped_salary_df.pivot(index="EDUCATION", columns='SALARY', 
                                   values='Counter')
ax = pivot_df.plot(kind='barh', stacked=True, color=['skyblue', 'orange'])
# Set labels and title
plt.xlabel('Count')
plt.ylabel('Education Level')
plt.title('Count of People by Salary and Education Level')
ax.xaxis.set_major_locator(MultipleLocator(1000))
#ax.xaxis.set_minor_locator(MultipleLocator(100))
ax.grid(which='both',alpha=0.3)

plt.savefig('SalaryEducation.svg', format='svg')
# Show the plot
plt.show()