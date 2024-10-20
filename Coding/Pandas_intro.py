# %%
#basic function about using pandas
import pandas as pd


# %%
#create a dataframe
#df = pd.DataFrame(listname, columns = ['col1','col2'])
df = pd.DataFrame({'col1': [1,2,3,4], 'col2': ['A','B','C','D']})
print(df)
#get size of dataframe
print(df.shape)

#extract first 3 rows data/other examples
print(df.head(3))
#iloc is using the index and support slicing
print(df.iloc[:3])

#select some data, basic filter
#note if we have only one column, and we only use one bracket [], it will not
#return a dataframe but a series. If we use another bracket outside, it will a dataframe.
print(df[df['col1'].isin([1,2])][['col2']])

#create a new column
df['col3'] = df['col1'] + 3
print(df.head())
df['col4'] = [2,2,3,4]

# %%
# manipulate the data
# drop duplicate by default, inplace = False, we can also remove duplicate by one column
df.drop_duplicates(subset=['col4'], keep='first', inplace=True)
print(df)

# drop missing values
df['col5'] = ['Y',None,'Y']
df = df.dropna(subset=['col5'])
print(df)

# rename the column
df = df.rename(columns = {
    'col1': 'First_col',
    'col2': 'Second_col'
})
print(df)

df = df.astype({
    'col3': str
})
print(df['col3'].dtype)
print(df.dtypes)

# fill value for null cells
df['col6'] = [None, None]
df['col6'] = df['col6'].fillna(0)
print(df)

# sort values
df.sort_values(by = ['col3'], ascending = False, inplace = True)
print(df)

# %%
# reshape the data structure

# concatenate two tables
df1 = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': ['A','B','C','D']
})
df2 = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': ['A','B','C','D']
})

df3 = pd.concat([df1, df2], axis = 0)
print(df3)

df4 = pd.concat([df1, df2], axis = 1)
print(df4)
df4.columns = ['col1','col2','col3','col4']
print(df4)

# pivot the table
df5 = pd.DataFrame({
    'City': ['A','A','A','B','B','B'],
    'Month': ['Jan','Feb','Mar','Jan','Feb','Mar'],
    'Number': [1,2,3,4,5,6]
})
print(df5)

df6 = df5.pivot(index = 'Month', columns = 'City', values = 'Number').reset_index()
print(df6)

# revert df6 to back long format
df7 = df6.melt(id_vars = 'Month', value_vars = ['A','B'], var_name = 'City', value_name = 'Number')
print(df7.head(6))
# %%

print(df4['col1'])



# %%
