import ctypes


def float_to_bits(float_number: float) -> list[int]:
    c_float = ctypes.c_float(float_number)
    cu = ctypes.c_uint32.from_address(ctypes.addressof(c_float))
    bit_list = [(cu.value >> i) & 1 for i in range(32)]
    return bit_list


def bits_to_float(bit_list: list[int]) -> float:
    u_value = 0
    for i in range(32):
        u_value = u_value + bit_list[i] * (2**i)
    cu = ctypes.c_uint(u_value)
    c_float = ctypes.c_float.from_address(ctypes.addressof(cu))
    return c_float.value


def floats_to_bits(float_list: list[float]) -> list[int]:
    bit_list = []

    for f in float_list:
        bit_list = bit_list + float_to_bits(f)

    return bit_list


def bits_to_floats(bit_list: list[int]) -> list[float]:
    bit_size = len(bit_list)
    float_size = int(bit_size / 32)
    float_vector = [0.0] * float_size
    index = 0
    findex = 0

    while index + 32 <= bit_size:
        part = bit_list[index:(index+32)]
        float_vector[findex] = round(bits_to_float(part), 3)
        index = index+32
        findex += 1

    return float_vector
