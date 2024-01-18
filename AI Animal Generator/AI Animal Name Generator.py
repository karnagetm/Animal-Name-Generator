import pandas as pd
import random

# Corrected file paths
sea_animals_path = r'C:\Users\KP\.spyder-py3\Personal Projects\AI Animal Generator\sea_animal_names.csv'
animals_path = r'C:\Users\KP\.spyder-py3\Personal Projects\AI Animal Generator\animal-names.csv'
insects_path = r'C:\Users\KP\.spyder-py3\Personal Projects\AI Animal Generator\insect_names.csv'

# Load the CSV files
sea_animals_df = pd.read_csv(sea_animals_path)
animals_df = pd.read_csv(animals_path)
insects_df = pd.read_csv(insects_path)

# Standardize column names (assuming the first column in each file contains the animal names)
sea_animals_df.columns = ['Name']
animals_df.columns = ['id', 'Name']  # Drop 'id' column if it exists
animals_df = animals_df.drop(columns=['id'], errors='ignore')
insects_df.columns = ['Name']

# Combine all dataframes into one
combined_df = pd.concat([sea_animals_df, animals_df, insects_df])

# Randomly pick two names from the combined dataframe
picked_names = random.sample(list(combined_df['Name']), 2)

# Generate the prompts
prompt1 = f"Make an image of {picked_names[0]} and {picked_names[1]} fighting each other and make it look realistic."
prompt2 = f"Show a crossbreed of a {picked_names[0]} and a {picked_names[1]}, making it muscly, very scary, and realistic looking."

prompt1, prompt2

