import pytest
from byte_operators import float_to_bits, bits_to_float, floats_to_bits, bits_to_floats

def test_float_to_bits():
    """
    Test the float_to_bits function.
    """
    float_number = 3.14
    bit_list = float_to_bits(float_number)
    expected_bits = [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    assert len(bit_list) == 32
    assert bit_list == expected_bits

def test_bits_to_float():
    """
    Test the bits_to_float function.
    """
    bit_list = [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    float_number = bits_to_float(bit_list)
    expected_float = 3.14
    assert float_number == pytest.approx(expected_float, rel=1e-3)

def test_floats_to_bits():
    """
    Test the floats_to_bits function.
    """
    float_list = [3.14, -2.71]
    bit_list = floats_to_bits(float_list)
    expected_bits = (float_to_bits(3.14) + float_to_bits(-2.71))
    assert bit_list == expected_bits

def test_bits_to_floats():
    """
    Test the bits_to_floats function.
    """
    float_list = [3.14, -2.71]
    bit_list = floats_to_bits(float_list)
    floats_from_bits = bits_to_floats(bit_list)
    assert floats_from_bits == [pytest.approx(f, rel=1e-3) for f in float_list]

# Run the tests
if __name__ == "__main__":
    pytest.main()
