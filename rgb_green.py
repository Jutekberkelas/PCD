import numpy as np
import imageio.v3 as img
import os

# Fungsi untuk mengekstrak channel biru (B) dari gambar
def extract_blue_channel(image_path, output_name):
    # Membaca gambar RGB
    image = img.imread(image_path)

    # Memastikan gambar memiliki format RGB
    if len(image.shape) < 3 or image.shape[2] != 3:
        print(f"Format gambar {image_path} harus RGB")
        return
    
    # Memisahkan channel warna (Blue)
    green = image[:, :, 1]

    # Membuat gambar hanya dengan komponen warna biru
    image_green = np.zeros_like(image)
    image_green[:, :, 1] = green

    # Menyimpan gambar hasil channel biru
    output_path = f"{output_name}_green.jpeg"
    img.imwrite(output_path, image_green)
    print(f"Gambar channel green untuk {output_name} berhasil disimpan sebagai {output_path}")

# Daftar gambar dan nama output yang sesuai
images = {
    "Daun Singkong": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun singkong.rgb",
    "Daun Pepaya": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun pepaya.rgb",
    "Daun Kenikir": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daunkenikir.rgb"
}

# Memproses setiap gambar untuk channel warna biru
for name, path in images.items():
    if os.path.exists(path):
        extract_blue_channel(path, name.replace(" ", "_").lower())
    else:
        print(f"File gambar {path} tidak ditemukan.")
