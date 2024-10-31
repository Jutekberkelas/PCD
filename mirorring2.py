import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = "C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\cat image.png"
image = img.imread(path)
height, width = image.shape[:2]

# Membuat array untuk menyimpan hasil mirroring
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)

# Melakukan mirroring horizontal dan vertikal secara bersamaan
for y in range(height):
  for x in range(width):
    horizontal[y, x] = image[y, width - 1 - x]
    vertical[y, x] = image[height - 1 - y, x]

# Menampilkan hasil mirroring
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.subplot(1, 3, 2)
plt.imshow(horizontal)
plt.subplot(1, 3, 3)
plt.imshow(vertical)
plt.show()