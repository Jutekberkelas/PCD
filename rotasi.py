import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
  radian_deg = np.radians(degree)
  cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
  height, width = image.shape[:2]
  max_dim = int(np.sqrt(height**2 + width**2))
  outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)
  centery, centerX = max_dim//2, max_dim//2
  for y in range(-height//2, height//2):
    for x in range(-width//2, width//2):
      newX = int(cos_deg * x - sin_deg * y) + centerX
      newY = int(sin_deg * x + cos_deg * y) + centery
      if 0 <= newX < max_dim and 0 <= newY < max_dim:
        outputImage[newY, newX] = image[y + height//2, x + width//2]
  return outputImage

image = img.imread("C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\cat image.png")
rotated_image = rotateImage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)

plt.show()