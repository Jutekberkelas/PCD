import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

image = img.imread("C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\anggrek.jpg")

if len(image.shape) == 3:
    image = np.mean(image, axis=2).astype(np.uint8)

sobelX = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobelY = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

imgpad = np.pad(image, pad_width=1, mode='constant', constant_values=0)

Gx = np.zeros_like(image, dtype=np.float32)
Gy = np.zeros_like(image, dtype=np.float32)

for y in range(1, imgpad.shape[0] - 1):
    for x in range(1, imgpad.shape[1] - 1):
        region = imgpad[y - 1:y + 2, x - 1:x + 2]
        Gx[y - 1, x - 1] = (region * sobelX).sum()
        Gy[y - 1, x - 1] = (region * sobelY).sum()

G = np.sqrt(Gx**2 + Gy**2)
G = (G / G.max()) * 255 
G = np.clip(G, 0, 255).astype(np.uint8)

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(2, 2, 2)
plt.title("Sobel X")
plt.imshow(Gx, cmap='gray')

plt.subplot(2, 2, 3)
plt.title("Sobel Y")
plt.imshow(Gy, cmap='gray')

plt.subplot(2, 2, 4)
plt.title("Gradient Magnitude")
plt.imshow(G, cmap='gray')

plt.tight_layout()
plt.show()
