import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def localThres(image, block_size, c):
    if len(image.shape) == 3: 
        image = np.mean(image, axis=-1) 

    pad_size = block_size // 2
    imgpad = np.pad(image, pad_width=pad_size, mode='constant', constant_values=0)
    threshold = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgpad[i:i+block_size, j:j+block_size]
            local_mean = np.mean(local_area)
            threshold[i, j] = 255 if image[i, j] > (local_mean - c) else 0
    return threshold.astype(np.uint8)

def basicThres(image, level):
    threshold = np.where(image > level, 255, 0)
    return threshold.astype(np.uint8)

image_path = "C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\hagia.jpg"
image = img.imread(image_path).astype(np.float32)

if len(image.shape) == 3:
    image = np.mean(image, axis=-1) 
image_normalized = image / 255.0 

block_size = 4
c = 8

local_threshold_image = localThres(image, block_size, c)

plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_normalized, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Local Thresholding")
plt.imshow(local_threshold_image, cmap='gray')

plt.show()
