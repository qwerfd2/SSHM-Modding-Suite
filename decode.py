from PIL import Image
import os
import sys
from tqdm import tqdm
import traceback

if len(sys.argv) < 2:
    print("Command line invalid.\nUsage: python", sys.argv[0], "dir_name")
    quit()

def convert_jpg_to_png_with_mask(input_path, mask_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        mask = Image.open(mask_path).convert("L")
        rgba_image = Image.new("RGBA", img.size)
        for x in range(img.width):
            for y in range(img.height):
                r, g, b, _ = img.getpixel((x, y))
                alpha = mask.getpixel((x, y))
                alpha /= 255
                rgba = (r, g, b, int(alpha * 255))
                rgba_image.putpixel((x, y), rgba)

    except:
        print(input_path, "process failed, skipping. Traceback:\n", traceback.format_exc())
        return

    try:
        output_file = os.path.join(input_path.replace(".jpg", ".png"))
        rgba_image.save(output_file)
        os.remove(input_path)
        os.remove(mask_path)
    
    except:
        print(input_path, "process success, but file create/delete operation failed. Traceback:\n", traceback.format_exc())

path_name = sys.argv[1]      
num_files = 0
for dirpath, _, filenames in os.walk(path_name):
    for filename in filenames:
        if not filename.endswith("_.jpg") and filename.endswith(".jpg"):
            num_files += 1

progress_bar = tqdm(total=num_files, desc="Converting images", unit="image")
for dirpath, _, filenames in os.walk(path_name):
    for filename in filenames:
        if not filename.endswith("_.jpg") and filename.endswith(".jpg"):
            mask_file = os.path.join(dirpath, filename.replace(".jpg", "_.jpg"))
            if os.path.exists(mask_file):
                jpg_file = os.path.join(dirpath, filename)
                convert_jpg_to_png_with_mask(jpg_file, mask_file)
                progress_bar.update(1)
            else:
                progress_bar.update(1)
    
    progress_bar.close()
