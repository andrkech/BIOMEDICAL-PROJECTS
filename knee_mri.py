# -*- coding: utf-8 -*-
"""knee_MRI_class.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UOeYBuokEQmssJB4YmZKJD3sgnp9erpP

This notebook is based on the [kneeMRI dataset](https://www.kaggle.com/datasets/sohaibanwaar1203/kneemridataset). The data were collected in the Clinical Hospital Centre Rijeka, Croatia. More information can be found in the respective paper:

I. Štajduhar, M. Mamula, D. Miletić, G. Unal, Semi-automated detection of anterior cruciate ligament injury from MRI, Computer Methods and Programs in Biomedicine, Volume 140, 2017, Pages 151–164.
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import pickle
import cv2 as cv
import matplotlib.pyplot as plt

import kagglehub

# Download latest version
dataset_path = kagglehub.dataset_download("sohaibanwaar1203/kneemridataset")

print("Path to dataset files:", dataset_path)
os.listdir(dataset_path)

metadata_df = pd.read_csv(os.path.join(dataset_path, 'metadata.csv'))
print(metadata_df.head)

def analyze_inj(metadata_df):
    # Lateralization Analysis
    left_knee_count = len(metadata_df[metadata_df['kneeLR'] == 0])
    right_knee_count = len(metadata_df[metadata_df['kneeLR'] == 1])

    print(f"Left knee scans: {left_knee_count} ({left_knee_count / len(metadata_df) * 100:.2f}%) \
            \nRight knee scans: {right_knee_count} ({right_knee_count / len(metadata_df) * 100:.2f}%) \
            \nTotal scans: {len(metadata_df)}")

    # Injury Analysis
    inj_mask = metadata_df['aclDiagnosis'].isin([1, 2])
    inj_counts = metadata_df[inj_mask].groupby('kneeLR')['aclDiagnosis'].count()
    inj_percent = len(metadata_df[inj_mask]) / len(metadata_df) * 100

    print(f"\nLeft knee injuries: {inj_counts[0]} \
            \nRight knee injuries: {inj_counts[1]} \
            \nTotal knee injuries: {inj_counts.sum()} ({inj_percent:.2f}%)")

    # Complete Tears Analysis
    rupture_mask = metadata_df['aclDiagnosis'] == 2
    rupture_counts = metadata_df[rupture_mask].groupby('kneeLR')['aclDiagnosis'].count()

    L_rup_percent = len(metadata_df[metadata_df['kneeLR'] == 0][rupture_mask]) / len(metadata_df) * 100
    R_rup_percent = len(metadata_df[metadata_df['kneeLR'] == 1][rupture_mask]) / len(metadata_df) * 100

    L_rup_percent_of_inj = rupture_counts[0] / inj_counts.sum() * 100
    R_rup_percent_of_inj = rupture_counts[1] / inj_counts.sum() * 100

    print(f"\nLeft knee complete tears: {rupture_counts[0]} ({L_rup_percent:.2f}%) ({L_rup_percent_of_inj:.2f}% of total injuries) \
            \nRight knee complete tears: {rupture_counts[1]} ({R_rup_percent:.2f}%) ({R_rup_percent_of_inj:.2f}% of total injuries) \
            \nTotal ACL complete tears: {rupture_counts.sum()} ({rupture_counts.sum()/len(metadata_df)*100:.2f}%)")

    return inj_counts, rupture_counts, left_knee_count, right_knee_count

def visualize_inj(metadata_df):
    # ANALYSIS
    inj_counts, rupture_counts, left_knee_count, right_knee_count = analyze_inj(metadata_df)

    # VISUALIZATION
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Bar plot for injury counts
    inj_counts.plot(kind='bar', ax=axes[0, 0])
    axes[0, 0].set_title('Frequency of ACL Injuries by Knee Lateralization')
    axes[0, 0].set_xlabel('Knee (0: Left, 1: Right)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_xticks([0, 1])
    axes[0, 0].set_xticklabels(['Left', 'Right'])

    # Pie chart for knee lateralization
    labels = ['Left Knee', 'Right Knee']
    sizes = [left_knee_count, right_knee_count]
    axes[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    axes[0, 1].axis('equal')
    axes[0, 1].set_title('Distribution of Knee Lateralization')

    # Bar plot for rupture counts
    rupture_counts.plot(kind='bar', ax=axes[1, 0], color='orange')
    axes[1, 0].set_title('Frequency of Complete ACL Tears by Knee Lateralization')
    axes[1, 0].set_xlabel('Knee (0: Left, 1: Right)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_xticks([0, 1])
    axes[1, 0].set_xticklabels(['Left', 'Right'])

    # Stacked bar plot for injury severity
    acl_diagnosis_counts = metadata_df.groupby('kneeLR')['aclDiagnosis'].value_counts().unstack(fill_value=0)
    acl_diagnosis_counts.plot(kind='bar', stacked=True, ax=axes[1, 1])
    axes[1, 1].set_title('ACL Injury Severity by Knee Lateralization')
    axes[1, 1].set_xlabel('Knee (0: Left, 1: Right)')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_xticks([0, 1])
    axes[1, 1].set_xticklabels(['Left', 'Right'])
    axes[1, 1].legend(title='ACL Diagnosis (0: None, 1: Partial, 2: Complete)')

    plt.tight_layout()
    plt.show()

analyze_inj(metadata_df)
visualize_inj(metadata_df)

def predict_tear_inj(metadata_df):
    features = metadata_df[['kneeLR']]
    target = metadata_df['aclDiagnosis'].apply(lambda x: 1 if x == 'tear' else 0)