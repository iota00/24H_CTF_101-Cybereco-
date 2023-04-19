from scapy.all import *

packets = rdpcap('capture.pcapng')

KEY_CODES = {
    0x4:['a', 'A'],
    0x5:['b', 'B'],
    0x6:['c', 'C'],
    0x7:['d', 'D'],
    0x8:['e', 'E'],
    0x9:['f', 'F'],
    0xA:['g', 'G'],
    0xB:['h', 'H'],
    0xC:['i', 'I'],
    0xD:['j', 'J'],
    0xE:['k', 'K'],
    0xF:['l', 'L'],
    0x10:['m', 'M'],
    0x11:['n', 'N'],
    0x12:['o', 'O'],
    0x13:['p', 'P'],
    0x14:['q', 'Q'],
    0x15:['r', 'R'],
    0x16:['s', 'S'],
    0x17:['t', 'T'],
    0x18:['u', 'U'],
    0x19:['v', 'V'],
    0x1A:['w', 'W'],
    0x1B:['x', 'X'],
    0x1C:['y', 'Y'],
    0x1D:['z', 'Z'],
    0x1E:['1', '!'],
    0x1F:['2', '@'],
    0x20:['3', '#'],
    0x21:['4', '$'],
    0x22:['5', '%'],
    0x23:['6', '^'],
    0x24:['7', '&'],
    0x25:['8', '*'],
    0x26:['9', '('],
    0x27:['0', ')'],
    0x28:['\n','\n'],
    0x29:['[ESC]','[ESC]'],
    0x2a:['[BACKSPACE]', '[BACKSPACE]'],
    0x2C:[' ', ' '],
    0x2D:['-', '_'],
    0x2E:['=', '+'],
    0x2F:['[', '{'],
    0x30:[']', '}'],
    0x32:['#','~'],
    0x33:[';', ':'],
    0x34:['\'', '"'],
    0x36:[',', '<'],
    0x37:['.', '>'],
    0x38:['/', '?'],
    0x39:['[CAPSLOCK]','[CAPSLOCK]'],
    0x2b:['\t','\t'],
    0x4f:[u'→',u'→'],
    0x50:[u'←',u'←'],
    0x51:[u'↓',u'↓'],
    0x52:[u'↑',u'↑']
}
out_1=""
out_2=""
for p in packets:
    try:
        a = hex(p.load[-6])

        # print(a, KEY_CODES[int(a, 16)])
        out_1 += KEY_CODES[int(a, 16)][0]
        out_2 += KEY_CODES[int(a, 16)][1]
    except:
        continue

print(out_1)
print()
print(out_2)