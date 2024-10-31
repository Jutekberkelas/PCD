import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2))
    outputImage = np.zeros((max_dim,max_dim,3), dtype=image.dtype)

    # Melakukan rotasi dengan pivot di titik (0,0)
    for y in range(height):
        for x in range(width):
            newX = int(cos_deg * x - sin_deg * y)
            newY = int(sin_deg * x + cos_deg * y)
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y, x]

    return outputImage

# Membaca gambar
image = img.imread("C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\cat image.png")

# Melakukan rotasi gambar 45 derajat
rotated_image = rotateImage(image, 45)

# Menampilkan gambar asli dan gambar yang telah diputar
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.show()