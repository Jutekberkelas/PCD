import numpy as np
import imageio.v3 as img
import os

def extract_blue_threshold(image_path, output_name, threshold=100):
    image = img.imread(image_path)

    if len(image.shape) < 3 or image.shape[2] != 3:
        print(f"Format gambar {image_path} harus RGB")
        return

    blue = image[:, :, 2]

    image_bw = np.zeros_like(image)
    image_bw[blue > threshold] = 255
    image_bw[blue <= threshold] = 0

    output_path = f"{output_name}_blue_threshold.jpeg"
    img.imwrite(output_path, image_bw)
    print(f"Gambar biner threshold untuk {output_name} berhasil disimpan sebagai {output_path}")

images = {
    "Daun Singkong": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun singkong.rgb",
    "Daun Pepaya": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun pepaya.rgb",
    "Daun Kenikir": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daunkenikir.rgb"
}

for name, path in images.items():
    if os.path.exists(path):
        extract_blue_threshold(path, name.replace(" ", "_").lower())
    else:
        print(f"File gambar {path} tidak ditemukan.")
