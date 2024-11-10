import imageio as img
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


image = img.imread ("C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\hagia.jpg")

if len(image.shape) == 3:
    grayscale_image = np.dot(image[..., :3], [0.299, 0.587, 0.114])
else:
    grayscale_image = image

rotated_image = ndimage.rotate(grayscale_image, 45, reshape=True)

sobel_x = ndimage.sobel(grayscale_image, axis=0)  
sobel_y = ndimage.sobel(grayscale_image, axis=1) 
edge_image = np.hypot(sobel_x, sobel_y) 

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Grayscale Image")
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Rotated Image (45 degrees)")
plt.imshow(rotated_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Edge Detection (Sobel)")
plt.imshow(edge_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
