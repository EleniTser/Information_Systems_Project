import pandas as pd

input_filename='/home/user/info_sys/data/medium-data'
output_filename='/home/user/info_sys/data/medium-data-mod.csv'

def modify_field(field):
    if isinstance(field, str):
        parts = field.split('=')
        if len(parts) == 2:
            return parts[1]
    return field

# Read the input CSV file using pandas
df = pd.read_csv(input_filename, header=None)

# Apply the modification function to each cell in the dataframe
df = df.applymap(modify_field)

# Write the modified dataframe back to a CSV file
df.to_csv(output_filename, index=False, header=False)
