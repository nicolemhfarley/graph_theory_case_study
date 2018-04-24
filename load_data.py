# Import libraries
import pandas as pd

# Read in the provider data: df_provider
df_provider = pd.read_csv('physicians.csv')

# Read in the procedure data: df_procedure
df_procedure = pd.read_csv('procedures.csv')

# Merge the dataframes on id and physician_id: df_merged
df_merged = pd.merge(df_provider, df_procedure, left_on='id', right_on='physician_id')

# Drop the duplicate id column and set 'id' as index
df_merged.drop(columns='physician_id', inplace=True)

# Save to csv: 'df_merged.csv'
df_merged.to_csv('df_merged.csv')
print('Dataframes merged. New csv file created')
