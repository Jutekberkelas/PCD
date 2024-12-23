import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from skimage.color import rgb2gray

# Fungsi untuk deteksi tepi dengan operator Sobel
def sobel_edge_detection(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    gx = convolve(image, kernel_x)
    gy = convolve(image, kernel_y)

    edge_sobel = np.sqrt(gx ** 2 + gy ** 2)
    edge_sobel = (edge_sobel / edge_sobel.max()) * 255
    return edge_sobel.astype(np.uint8)

# Segmentasi dengan thresholding dasar
def basic_thresholding(image, threshold):
    binary_image = np.zeros_like(image)
    binary_image[image > threshold] = 255
    return binary_image

def load_image_as_grayscale(path):
    image = imageio.imread(path)
    if len(image.shape) == 3: 
        image = rgb2gray(image)
    return (image * 255).astype(np.uint8)

image_path = "C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\image2.jpg"

try:
    image = load_image_as_grayscale(image_path)
    edge_sobel = sobel_edge_detection(image)
    # Segmentasi citra hasil deteksi edge dengan thresholding
    threshold = 128  
    segmented_image = basic_thresholding(edge_sobel, threshold)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Gambar Asli')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(edge_sobel, cmap='gray')
    plt.title('Deteksi Tepi Sobel')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(segmented_image, cmap='gray')
    plt.title('Segmentasi dengan Thresholding')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Gambar tidak ditemukan di path: {image_path}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
