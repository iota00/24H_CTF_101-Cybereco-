# Reverse 2

## Challenge Description

* The flag has been hidden in an image! Fortunately, we were able to recover the program that checks it.

* Tips:

    * To analyze a compiled executable, it is very convenient to use a decompiler, such as Ghidra, to reconstruct the source code from the executable
    * Once you understand how the program works, you can extract the flag with the programming language of your choice

* Links to interesting resources:

    * Ghidra
    * RGBA color model
    * libpng
    * PIL (python package)

## Solution

* This is a reverse engineering challenge where we have to extract the flag from an image by analyzing the given code.
* We are given an image `image.png` and a binary executable that checks for a flag. The program reads in the image file, does some processing, and then checks if the flag entered by the user is correct. Our goal is to extract the correct flag from the image.

* After examining the given code, we can see that the program is reading the given image using `libpng` and storing the pixel data in memory. It then processes the pixel data in some way to obtain the correct flag. The given code is written in C, but we can decompile it using `Ghidra` to obtain the following equivalent code:

```c
// modified - to make it more easier to understand what it does
undefined8 main(int param_1,long param_2)
{
  void **ppvVar1;
  size_t len;
  void *pvVar2;
  undefined8 info_struct;
  undefined8 read_struct;
  byte local_39;
  int img_h;
  undefined4 img_w;
  FILE *img;
  long *h_left_shift_with_3;
  int j;
  int i;

  h_left_shift_with_3 = (long *)0x0;
  if (param_1 < 2) {
    puts("Missing argument");
    exit(1);
  }
  len = strlen(*(char **)(param_2 + 8));
  if (len != 0x26) {
    puts("Invalid length");
    exit(1);
  }
  img = fopen("image.png","rb");
  read_struct = png_create_read_struct("1.6.38",0,0,0);
  info_struct = png_create_info_struct(read_struct);
  png_init_io(read_struct,img);
  png_read_info(read_struct,info_struct);
  img_w = png_get_image_width(read_struct,info_struct);
  img_h = png_get_image_height(read_struct,info_struct);
  png_read_update_info(read_struct,info_struct);
  h_left_shift_with_3 = (long *)malloc((long)img_h << 3);
  for (i = 0; i < img_h; i = i + 1) {
    len = png_get_rowbytes(read_struct,info_struct);
    ppvVar1 = (void **)(h_left_shift_with_3 + i);
    pvVar2 = malloc(len);
    *ppvVar1 = pvVar2;
  }
  png_read_image(read_struct,h_left_shift_with_3);
  j = 0;
  while( true ) {
    if (0x25 < j) {
      fclose(img);
      png_destroy_read_struct(&read_struct,&info_struct

```

* The given C code checks for the flag in the image file image.png. The program checks for two things:

    * The length of the flag should be 38 characters.
    * The XOR of the first and second pixel of each row in the image should match the corresponding byte of the flag.

* To solve this challenge, we can write a Python script that opens the image file and reads the pixel data. We can then perform the XOR operation on the first and second pixel of each row and get the corresponding byte of the flag. We can repeat this process for all 38 rows to get the flag.

* Here's the Python script:

```python

from PIL import Image

im = Image.open("image.png")

pixels = im.load()

flag = ""
for j in range(39):
    byte1 = pixels[j, 1][0] ^ pixels[j, 0][0]
    flag += chr(byte1)

print(flag)
```

* Running this script gives us the flag: `FLAG{4ll_my_h0m1e5_h4t3_s73g4n0gr4phy}`
