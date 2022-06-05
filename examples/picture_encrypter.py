import sys
sys.path.append('../')

from xor import XOR
filename = 'file.jpg'

a = XOR(filename, dec_filename="target.jpg")
a.encrypt(150)
