from src.io import load_tif_file
from src.plotting import plot_tif_stack

filepath = "path/to/your/file.tif"

stack = load_tif_file(filepath)
plot_tif_stack(stack, index=0)
