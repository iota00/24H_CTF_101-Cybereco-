from PIL import Image

im = Image.open("image.png")

pixels = im.load()

flag = ""
for j in range(39):
    byte1 = pixels[j, 1][0] ^ pixels[j, 0][0]
    flag += chr(byte1)

print(flag)

with open('flag.txt', 'w') as f:
    f.write(flag)