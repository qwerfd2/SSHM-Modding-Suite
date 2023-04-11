# SSHM-Pak-Extractor

These are two scripts that can extract/convert the content of .pak files for The Secret Society - Hidden Mystery.

---

extract.py: Extract .pak file(s).

 - Extract every .pak file under the same directory: ```python script.py all output_dir```

 - Extract a single .pak file under the same directory: ```python script.py pack.pak output_dir```

Files will be extracted to "output_dir" folder.

---

decode.py: Convert .jpg and associated mask file to .png.

 - Convert all .jpg files under a directory: ```python decode.py input_dir```
 
.jpg files will be removed once the converted .png is saved. Might take a long time due to the pixel-by-pixel conversion.

---
 
Dependencies:

 - script.py: ```python 3```
 
 - decode.py: ```python 3``` ```pillow``` ```tqdm```
