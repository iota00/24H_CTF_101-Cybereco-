
key = 0x46e60223adc175f149400b9b56bf9af7345fc2f19832140608aab04dfd
xor_result = 0x3bd56412c19e40c016323be3098cecc75800f7c0c740247e73edf101bb

result = key ^ xor_result

flag = bytes.fromhex(str(hex(result))[2:]).decode()[::-1]
print(flag)

with open('flag.txt', 'w') as f:
	f.write(flag)
