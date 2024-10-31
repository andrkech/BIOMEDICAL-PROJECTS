#KNEE MRI PROJECT

This repository deals with analyzing and classifying knee MRI images from the kneeMRIdataset available on Kaggle. The script performs exploratory data analysis (EDA) on the metadata, visualizes key insights, and implements a basic machine learning model for predicting ACL tears.

Features:

Data Loading and Preprocessing: Loads MRI images from .pck files, resizes them, and converts them to grayscale.
Metadata Analysis: Analyzes the metadata.csv file to extract insights about injury frequencies, rupture percentages, and knee lateralization.
Visualization: Generates informative plots, including:
Bar plots for injury counts and rupture frequencies.
Pie chart for knee lateralization distribution.
Stacked bar plot for injury severity by knee lateralization.
Sample images for each ACL injury severity category.
Machine Learning: Trains a Logistic Regression model to predict ACL tears based on knee lateralization.