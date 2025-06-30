from scipy.io import loadmat
import pandas as pd
from PIL import Image
import configparser
import tifffile

def load_mat_file(filepath):
    """Load a .mat file and return its contents as a dict."""
    return loadmat(filepath)

def load_txt_file(filepath, delimiter='\t'):
    """Load a .txt or .csv file into a pandas DataFrame."""
    return pd.read_csv(filepath, delimiter=delimiter)

def load_tif_file(filepath):
    """Load a .tif or .tiff image or stack."""
    return tifffile.imread(filepath)

def load_ini_file(filepath):
    """Load an .ini config file as a dictionary."""
    config = configparser.ConfigParser()
    config.read(filepath)
    return {section: dict(config.items(section)) for section in config.sections()}

def load_png_file(filepath):
    """Load a .png image as a PIL Image object."""
    return Image.open(filepath)
