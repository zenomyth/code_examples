#!/usr/bin/env python

import binascii

def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

def CRC32_from_file_nes(filename):
    f = open(filename,'rb')
    f.seek(0)
    buf = f.read()
    f.close()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

crc = CRC32_from_file_nes("C:\\Work\\Data\\x\\Teenage Mutant Ninja Turtles II - The Arcade Game (U) [!].nes")
print(crc)