import pandas as pd

csvFile = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(csvFile, engine='python', on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print(f"Error reading CSV file: {e}")

    