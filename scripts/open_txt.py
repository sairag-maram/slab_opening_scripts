from src.io import load_txt_file
from src.plotting import plot_dataframe

filepath = "path/to/your/file.txt"

df = load_txt_file(filepath)
print(df.head())

plot_dataframe(df, column=df.columns[0])
