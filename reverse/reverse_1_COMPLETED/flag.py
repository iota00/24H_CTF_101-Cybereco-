#!/usr/bin/env python3
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Can you recover the flag? If you think you got it, send it as positional argument.")
    parser.add_argument("flag", metavar="flag", type=str, help="The flag 🚩")
    args = parser.parse_args()
    return args


def print_flag(flag):
    if len(flag) !=  26:
        print("You got the wrong flag buddy")
        return
    if flag[10] == 'e':
        print("Nope")
    elif flag[4] == chr(0x7B) and flag[25] == chr(0x7D):
        if flag[0] == 'F':
            if flag[23] == 'g':
                if flag[16] == chr(0x30) and flag[18] == '0':
                    print("That's not it")
                elif flag[16] == flag[18] and flag[18] == chr(0x33):
                    if flag[8] == 'j' or flag[3] == 'A':
                        print("Wrong!")
                    elif flag[15] == flag[19] == 'r':
                        if flag[1:5] != 'FLAG':
                            if flag[8] == chr(0x5F) and flag[5] == 'n' and flag[0xE] == '_':
                                if flag[2] == 'G' and flag[3] == 'A': 
                                    if flag[3] == 'V' and flag[1] == 'F':
                                        if flag[0x30] == 'F' and flag[0x37] == 'w':
                                            if flag[25] == '{' and flag[4] == '}':
                                                if flag[20] == 'Z' and flag[12] == 'Z':
                                                    if flag[10] == 'z':
                                                        print("Nope")
                                        elif flag[0x30] == 'f':
                                            if flag[20] == 'a' and flag[3] == 'A':
                                                if flag[19] == 'z':
                                                    print("Not even close")
                                            else:
                                                print("Wrong")       
                                    elif flag[10] == 'Y' and flag[11] == ']':
                                        if flag[20] == 'S' and flag[22] == 'n':
                                            if flag[16] == 'g' or flag[1] == 'f':
                                                print("Wrong")
                                elif flag[2] == 'A' and flag[3] == 'G':
                                    if flag[9] == flag[0xC] == 't' and flag[24] == '!':
                                        if flag[0xD] == FUNC_00401064() and flag[1] == 'l'.upper() :
                                            eax = int(flag[6])
                                            if eax == 1 and flag[22] == str(eax):
                                                if flag[20] == 'S' and flag[10] == 'j':
                                                    print("wrong")
                                            elif eax == eax ^ eax and flag[11] == FUNC_00401000():
                                                twenty_first_char = 6*int(flag[6]) + 5*int(flag[11]) + 4*int(flag[13]) + 3*int(flag[16]) - 16*int(flag[18])
                                                if twenty_first_char == str(int(hex(int('10101',2)),16)):
                                                    if flag[7] == 'z' and flag[17] == 'F':
                                                        print("Wrong")
                                                elif flag[0xA] == 'h' and flag[21] == str(twenty_first_char):
                                                    if flag[7] == 'z' and flag[17] == 'A':
                                                        if flag[20] == 'S' and flag[22] == 'N':
                                                            print("You're getting close!")
                                                    elif flag[7] == 'w' and flag[17] == 'v':
                                                        if flag[20] == 'S' and flag[22] == 'N':
                                                            print("You were sooooooo close!")
                                                        elif flag[20] == 's' and flag[22] == 'n':
                                                            print("Good job! You got the flag! 🚩")
                                                    elif flag[7] == 'W' and flag[17] == 'V':
                                                        print("You capitalized it wrong")
                                                elif flag[0xA] == 'F' or flag[17] == 'A':
                                                    if flag[0x0000A].upper() == 'a':
                                                        print("You have to tell me how you managed to end up here!")
                                                elif flag[1] == 'X':
                                                    print("Wrong")
                                        else:
                                            if flag[1] == 'A':
                                                if flag[4] == chr(0x24) or flag[4] == chr(0x21):
                                                    print("Wrong")
                                                elif flag[0:4] == "FLAG":
                                                    if flag[4] == '{' or flag[24] == '}':
                                                        if flag[5:24] is not None:
                                                            print("Sorry...")
                                                        else:
                                                            print("How did you get here?")
                                                    else:
                                                        print("Did you take the right path? I don't think so")
                                elif flag[16] == 'g' or flag[10] == 'f':
                                    if flag[10] == 'e' and flag[12] == 'g':
                                        if flag[13] == 'e':
                                            if flag[4] == 'F' and flag[1] == '!':
                                                print("Not even close")
                                        else:
                                            print("Your on the wrong track")
                                    elif flag[20] == 'a' and flag[15] == chr(0x01):
                                        if flag[20] == 'A'.lower() and flag[3] == 'c':
                                            print("Keep going")
                            else:
                                print("Wrong flag")
                        else:
                            print("That's not the right flag")
                    else:
                        print("That's not the right flag")
                else:
                    print("That's not the right flag")
            else:
                print("That's not the right flag")
        else:
            print("That's not the right flag")
    else:
        print("That's not the right flag")


def FUNC_00401000():
    function_name = 'FUNC_0040'
    offset = ''
    for i in range(56, 64, 2):
        offset = str(i * 3 % 10) + offset
    function_name += offset
    return globals()[function_name]()


def FUNC_00401064():
    with open('flag.py', 'r') as f:
        file_length = len(f.read())
    return str(int(file_length / 0x458 - 2))


def FUNC_00401128():
    return str((0x1 | 0x2 | 0x8) & int('0b1101', 2) & int('0b0111', 2) & int('0b1110', 2)) 


def FUNC_00402048():
    return str(0xF & int('0b1000', 2) & int('0b0001', 2) & int('0b1010', 2))


def FUNC_00402240():
    return str((0x3 | 0xC) & int('0b1000', 2) & int('0b0001', 2) & int('0b1010', 2)) 


def FUNC_00406048():
    return str((0x3 | 0xC) & int('0b1101', 2) & int('0b0111', 2) & int('0b1110', 2))


def FUNC_00408046():
    return str((0x1 | 0x2 | 0x8) & int('0b1000', 2) & int('0b0001', 2) & int('0b1010', 2)) 


def FUNC_00409032():
    return str((0xF) & int('0b0000', 2) & int('0b0000', 2) | int('0b1111', 2))


def FUNC_00409500():
    return str((0x3 | 0xC) & int('0b1001', 2) | int('0b1111', 2) & int('0b0000', 2))


def FUNC_00409999():
    return str((0x1 | 0x8) & int('0b1101', 2) & int('0b0111', 2) & int('0b1110', 2))


if __name__ == "__main__":
    arguments = parse_args()
    print_flag(arguments.flag)