import sys

def unset_rightmost_one(value):
	return value & (value - 1)

def set_rightmost_zero(value):
	return value | (value + 1)

def unset_trailing_ones(value):
	return value & (value + 1)

def set_trailing_zeroes(value):
	return value | (value - 1)

def rotate_left(value, distance, width=32):
	mask = 2**width - 1
	_value = value & mask
	left_value = _value << distance % width
	right_value = _value >> (width - distance % width)
	return (left_value | right_value) & mask

def rotate_right(value, distance, width=32):
	mask = 2**width - 1
	_value = value & mask
	left_value = _value  << (width - distance % width)
	right_value = _value >> distance % width
	return (left_value | right_value) & mask

if __name__ == '__main__':
	print 'unset_rightmost_one'
	print 'from: {:08b} to: {:08b}'.format(3,unset_rightmost_one(3))
	print 'from: {:08b} to: {:08b}'.format(6,unset_rightmost_one(6))
	print 'from: {:08b} to: {:08b}'.format(10,unset_rightmost_one(10))
	print 'from: {:08b} to: {:08b}'.format(3,unset_rightmost_one(3))
	print 'set_rightmost_zero'
	print 'from: {:08b} to: {:08b}'.format(5,set_rightmost_zero(5))
	print 'from: {:08b} to: {:08b}'.format(4,set_rightmost_zero(4))
	print 'from: {:08b} to: {:08b}'.format(11,set_rightmost_zero(11))
	print 'from: {:08b} to: {:08b}'.format(3,set_rightmost_zero(3))
	print 'unset_trailing_ones'
	print 'from: {:08b} to: {:08b}'.format(0x2f, unset_trailing_ones(0x2f))
	print 'from: {:08b} to: {:08b}'.format(0xc, unset_trailing_ones(0xc))
	print 'from: {:08b} to: {:08b}'.format(0xa, unset_trailing_ones(0xa))
	print 'from: {:08b} to: {:08b}'.format(0xff, unset_trailing_ones(0xff))
	print 'set_trailing_zeroes'
	print 'from: {:08b} to: {:08b}'.format(8, set_trailing_zeroes(8))
	print 'from: {:08b} to: {:08b}'.format(10, set_trailing_zeroes(10))
	print 'from: {:08b} to: {:08b}'.format(9, set_trailing_zeroes(9))
	print 'from: {:08b} to: {:08b}'.format(0, set_trailing_zeroes(0))
	print 'type 0 ?: {}'.format(type(0))
	print 'sizeof 0?: {}'.format(sys.getsizeof(0))
	print 'type -1 ?: {}'.format(type(-1))
	print 'sizeof -1?: {}'.format(sys.getsizeof(-1))
	print '__sizeof__ -1?: {}'.format(int(-1).__sizeof__())
	print '-1 & 0x2? {}'.format(bool(-1 & 0x2))
	print 'masked: {:08b}'.format(-1 & 0xff)
	print 'rotate_left'
	print 'from {:032b} to {:032b}'.format(0xf, rotate_left(0xf, 4))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_left(0xf, 16))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_left(0xf, 30))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_left(0xf, 33))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_left(0xf, 1))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_left(0xf, 31))
	print 'from {:032b} to {:032b}'.format(-16, rotate_left(-16, 4))
	print 'from {:032b} to {:032b}'.format(4294967280, rotate_left(4294967280, 4))
	print 'rotate_right'
	print 'from {:032b} to {:032b}'.format(0xf, rotate_right(0xf, 4))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_right(0xf, 16))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_right(0xf, 30))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_right(0xf, 33))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_right(0xf, 1))
	print 'from {:032b} to {:032b}'.format(0xf, rotate_right(0xf, 31))
	print 'from {:032b} to {:032b}'.format(-16, rotate_right(-16, 4))
	print 'from {:032b} to {:032b}'.format(4294967280, rotate_right(4294967280, 4))
