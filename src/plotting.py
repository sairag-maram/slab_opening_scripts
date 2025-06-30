import matplotlib.pyplot as plt

def plot_mat_trace(mat_data, key, column=0):
    """Plot time trace from .mat dict."""
    data = mat_data.get(key)
    if data is None:
        print(f"Key '{key}' not found.")
        return
    plt.plot(data[:, column])
    plt.title(f"Time Trace: {key}[Column {column}]")
    plt.xlabel('Frame')
    plt.ylabel('Value')
    plt.show()

def plot_dataframe(df, column):
    """Plot specified column from a DataFrame."""
    if column not in df.columns:
        print(f"Column '{column}' not found.")
        return
    plt.plot(df[column])
    plt.title(f"Column: {column}")
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

def plot_image(image, cmap=None):
    """Display a single image (PIL Image or numpy array)."""
    plt.imshow(image, cmap=cmap)
    plt.axis('off')
    plt.show()

def plot_tif_stack(stack, index=0):
    """Plot a single frame from a TIFF stack."""
    if stack.ndim == 3:
        plt.imshow(stack[index], cmap='gray')
        plt.title(f"TIFF Frame {index}")
        plt.axis('off')
        plt.show()
    else:
        plt.imshow(stack, cmap='gray')
        plt.title("TIFF Image")
        plt.axis('off')
        plt.show()
