import struct


f = 12.508239423942167

f_byte = list(struct.pack("d", f))
print(f_byte)

f_bytearray = bytearray(f_byte)
print(f_bytearray)

f_float = list(struct.unpack("d", f_bytearray))
print(f_float)