import pandas as pd
import numpy as np

# Escribir archivo con pandas
x = [i for i in range(10)]
y = [i + 3 for i in range(10)]

df = pd.DataFrame({"x": x, "y": y})
df.to_parquet("data/df_ejemplo.parquet")

# Leer archivo parquet con pandas
df = pd.read_parquet("data/df_ejemplo.parquet")






