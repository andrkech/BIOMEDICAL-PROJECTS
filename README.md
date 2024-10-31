#KNEE MRI PROJECT

This repository deals with analyzing and classifying knee MRI images from the  kneeMRI dataset available on [Kaggle](https://www.kaggle.com/datasets/sohaibanwaar1203/kneemridataset). As described by the authors, this dataset was created on a Siemens Avanto 1.5T MR scanner at the Clinical Hospital Centre Rijeka, Croatia, from 2006 until 2014this.  The script performs exploratory data analysis (EDA) on the metadata, visualizes key insights, and implements a basic machine learning model for predicting ACL tears.

Ackowledgement:
[I. Štajduhar, M. Mamula, D. Miletić, G. Unal, Semi-automated detection of anterior cruciate ligament injury from MRI, Computer Methods and Programs in Biomedicine, Volume 140, 2017, Pages 151–164.](https://www.sciencedirect.com/science/article/abs/pii/S0169260716305028)

Features:

Data Loading and Preprocessing: Loads MRI images from .pck files, resizes them, and converts them to grayscale.

Metadata Analysis: Analyzes the metadata.csv file to extract insights about injury frequencies, rupture percentages, and knee lateralization.

Visualization: Generates informative plots, including:

Bar plots for injury counts and rupture frequencies.

Pie chart for knee lateralization distribution.

Stacked bar plot for injury severity by knee lateralization.

Sample images for each ACL injury severity category.

Machine Learning: Trains a Logistic Regression model to predict ACL tears based on knee lateralization.

![image](https://github.com/user-attachments/assets/52055874-a00a-44bc-9418-2a3c2d6d2173)

![image](https://github.com/user-attachments/assets/a4fd4f27-934b-4c19-b3a7-8a317582a35f)
