import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
print(df)
print(df.describe())

print()
#Reading in a CSV file
surveys_df = pd.read_csv("/home/tinigam/FOP1005/Lecture/Lecture 9 Codes/Lecture 9 Codes/2-Structured data/surveys.csv")
# print(surveys_df)
# print()
# print(type(surveys_df))
# print()
# print(surveys_df.dtypes)
# print()
# print(surveys_df.columns)
# print()
# print(surveys_df.shape)
# print()
# print(surveys_df.head())
# print()
# print(surveys_df.head(15))
# print()
# print(surveys_df.tail())
# print()
# print(surveys_df.columns.values)
# print()
# print(pd.unique(surveys_df['species_id']))
# print()
# print(surveys_df['weight'].describe())
# print()
# print(surveys_df['weight'].min())
# print(surveys_df['weight'].max())
# print(surveys_df['weight'].mean())
# print(surveys_df['weight'].std())
# print(surveys_df['weight'].count())
# print()

# sorted_data = surveys_df.groupby('sex')
# print(sorted_data.describe())
# print()
# print(sorted_data.mean())

# print()
# species_counts = surveys_df.groupby('species_id')['record_id'].count()
# print(species_counts)

# print()
# do_df = surveys_df.groupby('species_id')['record_id'].count()['DO']
# print(do_df)

# print()
# print(surveys_df['weight'] * 2.2)

# #plotting
# print(species_counts)
# species_counts.plot(kind='bar')
# plt.show()

# #Slicing
# # select rows 0, 1, 2 (row 3 is not selected)
# print(surveys_df[0:3])
# # select the first 5 rows (rows 0, 1, 2, 3, 4)
# print(surveys_df[:5])
# # select the last element in the list
# print(surveys_df[-1:])


# # iloc[row slicing, column slicing]
# print(surveys_df.iloc[0:3, 1:4])
# # select all columns for rows of index values 0 and 10
# print(surveys_df.loc[[0, 10], :])
# # select three columns for row 0
# print(surveys_df.loc[0, ['species_id', 'plot_id', 'weight']])
# # All columns for rows, 0, 10
# print(surveys_df.loc[[0, 10], :])

# print()
# print(surveys_df[surveys_df.year == 2002])
# print()
# print(surveys_df[surveys_df.year != 2002])
# print()
# print(surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)])

# print()
# #Copy uses the dataframe’s copy() method
# true_copy_surveys_df = surveys_df.copy()
# #A Reference is created using the = operator
# ref_surveys_df = surveys_df
