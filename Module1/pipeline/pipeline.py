import sys
import pandas as pd

month = int(sys.argv[1]) ## argumento 0 é o nome do script, argumento 1 é o mês

df = pd.DataFrame({"day": [1, 2], "num_passangers": [3, 4]})
df['month'] = month

print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f'Hello pipeline, month = {month}')