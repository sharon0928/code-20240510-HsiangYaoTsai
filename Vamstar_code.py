#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:11:42 2024

@author: hsiangyao
"""
import pandas as pd
tsv_file = '/Users/hsiangyao/Downloads/interview_analysis_molecule_x_10mg_v1.tsv'
df = pd.read_csv(tsv_file, sep='\t')

# Write the DataFrame to a CSV file
csv_file= 'interview_analysis_molecule_x_10mg_v1.csv'
df.to_csv(csv_file, index=False)

# Load the CSV file into a DataFrame
df_csv = pd.read_csv("/Users/hsiangyao/Downloads/interview_analysis_molecule_x_10mg_v1.csv")


# Drop unnecessary columns. Drop those columns with same data
df.drop(columns=["contract_id", "sku", "atc", "active_ingredient", "pack_strength"], inplace=True)

# Drop columns no meaningful data
df.drop(columns=["outcome", "second_place_outcome","participants","participants_price", "second_place"], inplace=True)


# Convert date columns to datetime type
df["published_date"] = pd.to_datetime(df["published_date"])
df["start_date"] = pd.to_datetime(df["start_date"])
df["end_date_extension"] = pd.to_datetime(df["end_date_extension"])
df["published_date_month"] = pd.to_datetime(df["published_date_month"])


# Extract relevant features from datetime columns
df["published_year"] = df["published_date"].dt.year
df["published_month"] = df["published_date"].dt.month
df["start_year"] = df["start_date"].dt.year
df["start_month"] = df["start_date"].dt.month
df["end_extension_year"] = df["end_date_extension"].dt.year
df["end_extension_month"] = df["end_date_extension"].dt.month

# Drop original datetime columns because datetime cannot be used in ML pipline
df.drop(columns=["published_date", "start_date", "end_date_extension", "published_date_month"], inplace=True)


# Remove rows where winner_price <= 0 or null. Winner price should lower than maximum_price_allowed
df = df[(df["winner_price"] > 0) & (~df["winner_price"].isnull()) & (df["winner_price"]<= df["maximum_price_allowed"])]

# Convert categorical variables into dummy variables
df = pd.get_dummies(df, columns=["buyer", "region", "contract_type","winner"])

df.head()

csv_file= 'interview_analysis_molecule_x_10mg_v2.csv'
df.to_csv(csv_file, index=False)
