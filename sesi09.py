
import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

def roberts_edge_detection(image):
    roberts_x = np.array([[1, 0], [0, -1]])
    roberts_y = np.array([[0, 1], [-1, 0]])
    
    gx = np.zeros_like(image)
    gy = np.zeros_like(image)
    
    for y in range(image.shape[0] - 1):
        for x in range(image.shape[1] - 1):
            region = image[y:y+2, x:x+2]
            gx[y, x] = np.sum(region * roberts_x)
            gy[y, x] = np.sum(region * roberts_y)
    
    return np.sqrt(gx**2 + gy**2)

def sobel_edge_detection(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    gx = np.zeros_like(image)
    gy = np.zeros_like(image)
    
    padded_image = np.pad(image, ((1, 1), (1, 1)), mode='constant', constant_values=0)
    
    for y in range(1, image.shape[0] + 1):
        for x in range(1, image.shape[1] + 1):
            region = padded_image[y-1:y+2, x-1:x+2]
            gx[y-1, x-1] = np.sum(region * sobel_x)
            gy[y-1, x-1] = np.sum(region * sobel_y)
    
    return np.sqrt(gx**2 + gy**2)

image = iio.imread("C:\\Users\\Lenovo\\Downloads\\kakatua.jpg")

if len(image.shape) == 3:
    image = np.mean(image, axis=2).astype(np.uint8)

edges_roberts = roberts_edge_detection(image)

edges_sobel = sobel_edge_detection(image)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Robert Edge Detection")
plt.imshow(edges_roberts, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Sobel Edge Detection")
plt.imshow(edges_sobel, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
