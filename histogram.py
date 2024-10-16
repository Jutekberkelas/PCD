
import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

image_path = r"C:\\Users\\Lenovo\Documents\\OneDrive\\Pictures\\image.rgb"
image = img.imread(image_path)

if len(image.shape) < 3 or image.shape[2] != 3:
    print("Format gambar harus RGB")
    exit()

# Mengubah gambar menjadi grayscale
grayscale_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])


# Hitung histogram dari gambar grayscale
histogram, bins = np.histogram(grayscale_image.flatten(), bins=256, range=(0, 256))

# Plot histogram
plt.figure(figsize=(10, 6))
plt.bar(bins[:-1], histogram, width=1, edgecolor='black')
plt.xlabel('Nilai Intensitas Piksel')
plt.ylabel('Frekuensi')
plt.title('Histogram image Grayscale')
plt.show()

# Menyimpan gambar grayscale
img.imwrite("image_grayscale.png", grayscale_image.astype(np.uint8))

print("Proses Berhasil")