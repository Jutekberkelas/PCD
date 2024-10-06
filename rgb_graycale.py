import numpy as np
import imageio.v3 as img
import os

def convert_to_grayscale(image_path, output_name):
    image = img.imread(image_path)

    if len(image.shape) < 3 or image.shape[2] != 3:
        print(f"Format gambar {image_path} harus RGB")
        return

    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]

    grayscale = 0.299 * red + 0.587 * green + 0.114 * blue

    image_gray = np.zeros_like(image)
    image_gray[:, :, 0] = grayscale
    image_gray[:, :, 1] = grayscale
    image_gray[:, :, 2] = grayscale

    output_path = f"{output_name}_grayscale.jpeg"
    img.imwrite(output_path, image_gray.astype(np.uint8))
    print(f"Gambar grayscale untuk {output_name} berhasil disimpan sebagai {output_path}")

images = {
    "Daun Singkong": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun singkong.rgb",
    "Daun Pepaya": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daun pepaya.rgb",
    "Daun Kenikir": r"C:\\Users\\Lenovo\\Documents\\OneDrive\\Pictures\\daunkenikir.rgb"
}

for name, path in images.items():
    if os.path.exists(path):
        convert_to_grayscale(path, name.replace(" ", "_").lower())
    else:
        print(f"File gambar {path} tidak ditemukan.")
