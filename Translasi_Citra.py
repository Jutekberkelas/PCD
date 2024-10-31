import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shifty):
  imgTranslasi = np.roll(image, shift=shifty, axis=0)  # Geser vertikal
  imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)  # Geser horizontal
  # Mengisi bagian yang kosong dengan warna hitam (0)
  if shifty > 0:
    imgTranslasi[:shifty, :] = 0  # Bagian atas jika geser ke bawah
  elif shifty < 0:
    imgTranslasi[shifty:, :] = 0  # Bagian bawah jika geser ke atas
  if shiftX > 0:
    imgTranslasi[:, :shiftX] = 0  # Bagian kiri jika geser ke kanan
  elif shiftX < 0:
    imgTranslasi[:, shiftX:] = 0  # Bagian kanan jika geser ke kiri
  return imgTranslasi

image = img.imread ("C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\image\\anggrek.jpg")
imgResult = Translasi(image, shiftX=50, shifty=-300)

plt.figure(figsize=(20, 20))
plt.subplot(2, 1, 1)
plt.imshow(image)
plt.subplot(2, 1, 2)
plt.imshow(imgResult)
plt.show()