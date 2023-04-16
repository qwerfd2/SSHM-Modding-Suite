# SSHM-Modding-Suite

These are two scripts that can extract and convert the content of ```.pak``` files for The Secret Society - Hidden Mystery, and another script that can decrypt the ```player.prf``` save file.

---

**extract.py**: Extract ```.pak``` file(s).

 - Extract every ```.pak``` file under the same directory: ```python extract.py all output_dir```

 - Extract a single ```.pak``` file under the same directory: ```python extract.py pack.pak output_dir```

Files will be extracted to ```output_dir``` folder.

---

**decode.py**: Convert ```.jpg``` and associated mask file to ```.png```.

 - Convert all ```.jpg``` files under a directory: ```python decode.py input_dir```
 
```.jpg``` files will be removed once the converted ```.png``` is saved. Might take a long time due to the pixel-by-pixel conversion.

---

**save.py**: Decrypt or encrypt save file ```player.prf``` under the same directory.

Decrypt ```player.prf```: ```python save.py d```, plaintext save will be saved to ```plaintext.prf```.

Encrypt ```plaintext.prf```: ```python save.py e```, encrypted save will be saved to ```player.prf```.

Encrypt is currently unnecessary as the game accepts plaintext. The first byte and the last two bytes must be deleted for the game to recognize the plaintext savefile.

---
 
Dependencies:

 - script.py: ```python 3```
 
 - decode.py: ```python 3``` ```pillow``` ```tqdm```
 
 - decrypt.py: ```python 3```
