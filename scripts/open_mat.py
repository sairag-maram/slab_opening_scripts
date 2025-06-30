from src.io import load_mat_file
from src.plotting import plot_mat_trace

filepath = "path/to/your/file.mat"

# Replace with your actual key, e.g., 'time_trace'
key = 'time_trace'

data = load_mat_file(filepath)
plot_mat_trace(data, key, column=0)
