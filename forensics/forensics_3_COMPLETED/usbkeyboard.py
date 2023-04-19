#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#More symbols in https://www.fileformat.info/search/google.htm?q=capslock+symbol&domains=www.fileformat.info&sitesearch=www.fileformat.info&client=pub-6975096118196151&forid=1&channel=1657057343&ie=UTF-8&oe=UTF-8&cof=GALT%3A%23008000%3BGL%3A1%3BDIV%3A%23336699%3BVLC%3A663399%3BAH%3Acenter%3BBGC%3AFFFFFF%3BLBGC%3A336699%3BALC%3A0000FF%3BLC%3A0000FF%3BT%3A000000%3BGFNT%3A0000FF%3BGIMP%3A0000FF%3BFORID%3A11&hl=en
KEY_CODES = {
    0x04:['a', 'A'],
    0x05:['b', 'B'],
    0x06:['c', 'C'],
    0x07:['d', 'D'],
    0x08:['e', 'E'],
    0x09:['f', 'F'],
    0x0A:['g', 'G'],
    0x0B:['h', 'H'],
    0x0C:['i', 'I'],
    0x0D:['j', 'J'],
    0x0E:['k', 'K'],
    0x0F:['l', 'L'],
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
    0x29:['␛','␛'],
    0x2a:['⌫', '⌫'],
    0x2b:['\t','\t'],
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
    0x39:['⇪','⇪'],
    0x4f:[u'→',u'→'],
    0x50:[u'←',u'←'],
    0x51:[u'↓',u'↓'],
    0x52:[u'↑',u'↑']
}


#tshark -r ./usb.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keyboards.txt
def read_use(file):
    with open(file, 'r') as f:
        datas = f.readlines()
    
    datas = [d.strip() for d in datas if d] 
    cursor_x = 0
    cursor_y = 0
    lines = []
    output = ''
    skip_next = False
    lines.append("")
    
    for data in datas:
        shift = int(data.split(':')[0], 16) # 0x2 is left shift 0x20 is right shift
        key = int(data.split(':')[2], 16)

        if skip_next:
            skip_next = False
            continue
        
        if key == 0 or int(data.split(':')[3], 16) > 0:
            continue
        
        #If you don't like output get a more verbose output here (maybe you need to map new rekeys or remap some of them)
        if not key in KEY_CODES:
            #print("Not found: "+str(key))
            continue
        
        if shift != 0:
            shift=1
            skip_next = True

        if KEY_CODES[key][shift] == u'↑':
            lines[cursor_y] += output
            output = ''
            cursor_y -= 1
        
        elif KEY_CODES[key][shift] == u'↓':
            lines[cursor_y] += output
            output = ''
            cursor_y += 1

        elif KEY_CODES[key][shift] == u'→':
            cursor_x += 1

        elif KEY_CODES[key][shift] == u'←':
            cursor_x -= 1

        elif KEY_CODES[key][shift] == '\n':
            lines.append("")
            lines[cursor_y] += output
            cursor_x = 0
            cursor_y += 1
            output = ''

        elif KEY_CODES[key][shift] == '[BACKSPACE]':
            output = output[:cursor_x-1] + output[cursor_x:]
            cursor_x -= 1
        
        else:
            output = output[:cursor_x] + KEY_CODES[key][shift] + output[cursor_x:]
            cursor_x += 1
    
    if lines == [""]:
        lines[0] = output
    
    if output != '' and output not in lines:
        lines[cursor_y] += output
    
    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing file to read...')
        exit(-1)
    sys.stdout.write(read_use(sys.argv[1]))
