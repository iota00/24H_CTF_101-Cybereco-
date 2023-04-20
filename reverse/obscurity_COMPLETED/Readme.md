# Obscurity

## Challenge Description

* The goal of the `Obscurity` challenge is to guess the flag by providing a single input.
* Using `Ghidra` to decompile the `main` function:

```c
undefined8 main(void)

{
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined4 local_80;
  undefined local_7c;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined4 local_60;
  undefined local_5c;
  byte local_58 [76];
  int local_c;
  
  local_78 = 0x32140608aab04dfd;
  local_70 = 0xbf9af7345fc2f198;
  local_68 = 0xc175f149400b9b56;
  local_60 = 0xe60223ad;
  local_5c = 0x46;
  local_98 = 0x40247e73edf101bb;
  local_90 = 0x8cecc75800f7c0c7;
  local_88 = 0x9e40c016323be309;
  local_80 = 0xd56412c1;
  local_7c = 0x3b;
  puts("I bet you\'ll never guess the flag.");
  puts("But just for fun I\'ll give you one try.");
  fgets((char *)local_58,0x40,stdin);
  local_c = 0;
  while( true ) {
    if (0x1c < local_c) {
      puts("Wait you actually guessed it? Well done...");
      return 0;
    }
    if ((*(byte *)((long)&local_78 + (long)local_c) ^ local_58[local_c]) !=
        *(byte *)((long)&local_98 + (long)local_c)) break;
    local_c = local_c + 1;
  }
  puts("I knew you couldn\'t do it :)");
  return 1;
}

```

* The program reads user input, performs a XOR operation with a predefined key, and compares the result with a predefined XOR result. If the comparison succeeds, it prints the flag.

## The Solving Process

* To obtain the flag, we need to reverse the XOR operation performed on the user input by the program. Specifically, we need to perform a XOR operation between the predefined key and the predefined XOR result to obtain the flag.

* To do this in Python, we can first define the key and XOR result variables as follows:

```python

key = 0x46e60223adc175f149400b9b56bf9af7345fc2f19832140608aab04dfd
xor_result = 0x3bd56412c19e40c016323be3098cecc75800f7c0c740247e73edf101bb
```

* We can then perform the XOR operation between the key and XOR result using the XOR operator (^), and store the result in a variable named result:

```python

result = key ^ xor_result
```

* Next, we need to convert the resulting hex string to bytes and reverse it, since the byte order is little-endian. We can do this using the fromhex and decode functions, along with the [::-1] slicing syntax:

```python

flag = bytes.fromhex(str(hex(result))[2:]).decode()[::-1]
```

* Finally, we can print the flag and save it to a file named flag.txt:

```python

print(flag)

with open('flag.txt', 'w') as f:
    f.write(flag)
```

* Running the script should output the flag: `FLAG{x0r_15_l0v3_x0r_15_l1f3}`