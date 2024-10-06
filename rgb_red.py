import numpy as np
import imageio.v3 as img
import os

def extract_red_channel(image_path, output_name):
    image = img.imread(image_path)

    if len(image.shape) < 3 or image.shape[2] != 3:
        print(f"Format gambar {image_path} harus RGB")
        return
    
    red = image[:, :, 0]

    image_red = np.zeros_like(image)
    image_red[:, :, 0] = red


    output_path = f"{output_name}_red.jpeg"
    img.imwrite(output_path, image_red)
    print(f"Gambar channel merah untuk {output_name} berhasil disimpan sebagai {output_path}")

images = {
    "Daun Singkong": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun singkong.rgb",
    "Daun Pepaya": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun pepaya.rgb",
    "Daun Kenikir": r"C:\Users\Lenovo\Documents\\OneDrive\\Pictures\\daunkenikir.rgb"
}

for name, path in images.items():
    if os.path.exists(path):
        extract_red_channel(path, name.replace(" ", "_").lower())
    else:
        print(f"File gambar {path} tidak ditemukan.")
