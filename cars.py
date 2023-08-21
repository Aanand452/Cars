import numpy as np
import pandas as pd


def cars():

    cars_df = pd.read_csv("/Users/anandkumar/Downloads/Data/cars.csv")

    print(cars_df)

    # Befor analyzing the data check the whole data set

    # it shows the number of rows in the whole data set
    print(cars_df.head())

    # it shows the number of columns in the data set
    print(cars_df.columns)

    # it shows the number of rows in the data set
    print(cars_df.index)

    # it shows the datytype of each column in the data set
    print(cars_df.dtypes)

    # it shows the number unique values in each coulmn and whole dataframe as well
    print(cars_df.nunique())

    # find all the null values in the dataset,if there any value in the coulmn, then fill it with the mean of the coulmn.
    print(cars_df.isnull())
    print(cars_df.isnull().sum())
    print(cars_df['Cylinders'].fillna(
        cars_df['Cylinders'].mean(), inplace=True))

    # check what are the different types of Make are there in our dataset, And, what is the count(occurrence) of each make in the data?

    print(cars_df['Make'].value_counts())

    # Show all the records where Origin ASIA OR EUROPE

    # First Technique
    print(cars_df[(cars_df['Origin'] == "Asia")
          | (cars_df['Origin'] == "Europe")])

    # Second Technique
    print(cars_df[cars_df['Origin'].isin(['Asia', 'Europe'])])

    # Remove all the records weight above 4000
    print(cars_df[cars_df['Weight'] > 4000])
    print(cars_df[~(cars_df['Weight'] > 4000)])
    print(cars_df.shape)

    # Increase all the values of 'MPG_City' column by 3

    print(cars_df.head(3))

    print(cars_df[cars_df['MPG_City'] ==
          cars_df['MPG_City'].apply(lambda x: x+3)])


cars()
