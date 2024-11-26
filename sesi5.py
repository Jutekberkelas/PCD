
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Menerapkan filter
def apply_filters(image, filter_type):
    kernel = None
    if filter_type == "low-pass":
        kernel = np.ones((5, 5), np.float32) / 25 
    elif filter_type == "high-pass":
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])  # edge detection
    elif filter_type == "high-boost":
        k = 1.5
        low_pass = np.ones((5, 5), np.float32) / 25
        high_boost_kernel = (k * np.eye(5)) - low_pass
        kernel = high_boost_kernel

    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

color_image = cv2.imread("C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\anggrek.jpg") 
grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

filters = ["low-pass", "high-pass", "high-boost"]

results = {}

for f in filters:
    results[f] = {
        "color": apply_filters(color_image, f),
        "grayscale": apply_filters(grayscale_image, f),
    }

fig, axs = plt.subplots(3, 2, figsize=(12, 12))
for i, f in enumerate(filters):
    axs[i, 0].imshow(cv2.cvtColor(results[f]["color"], cv2.COLOR_BGR2RGB))
    axs[i, 0].set_title(f"{f.capitalize()} - Berwarna")
    axs[i, 0].axis("off")
    
    axs[i, 1].imshow(results[f]["grayscale"], cmap="gray")
    axs[i, 1].set_title(f"{f.capitalize()} - Grayscale")
    axs[i, 1].axis("off")

plt.tight_layout()
plt.show()
