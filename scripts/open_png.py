from src.io import load_png_file
from src.plotting import plot_image

filepath = "path/to/your/image.png"

image = load_png_file(filepath)
plot_image(image)
