# Python is strongly typed (types do not change).

# Integer division
a = 11
b = 2

print(a // 2) # prints 5 (throws away remainder)
print(a / 2) # prints 5.5 (keeps remainder)

# Other math
print(11 % 10) # modulo 10 extracts last digit
print(111 % 100) # modulo 100 extracts last 2 digits
print (a ** b) # power
print (divmod(a, b)) # produce quotient and remainder

# Number literals
import sys
print(f'max int: {sys.maxsize}')
print('float inf: {0}'.format(float('inf')))

base10 = 10
base2 = 0b10
base8 = 0o10
base16 = 0x10

print(base10)
print(base2)
print(base8)
print(base16)

# Type conversion
print(int(True))
print(int(False))
print(int(3.5))
print(int('100'))
print(float('100.05'))
print(float('10e5'))
print(str(10))
print(str(10e4))

# Binary
# Can also use bin() to print binary repr
x = -1
print(f'x: {x:08b}')
print(f'(x<<(2+1): {x<<(2+1):08b}')

y = 1
print(f'y: {y:08b}')
print(f'(y<<6)-1: {(y<<6)-1:08b}')

z = 255
print(f'z: {z:08b}')
print(f'z&(y<<6)-1: {z & ((y<<6)-1):08b}')

print(f'z&(x<<(2+1)): {z & (x<<(2+1)):08b}')

# Decimal
import decimal

print(f'Decimal: {decimal.Decimal("1.33")}')

# Strings are immutable
text = 'Hello\n' + ('World!' * 2)
multi = '''Hello
World Again!''' + text[1] + text[-1]

print(text)
print(len(text))
print(multi)

list = ['c', 'a', 't']

# Slicing
text2 = "abcdefghijklmnopqrstuvwxyz"

print(text2[-1]) # last character (not a list)
print(text2[3:3]) # empty string
print(text2[:]) # entire string
print(text2[5:]) # Postion 5 to the end 
print(text2[-5:]) # 5 from the end to the end
print(text2[5:-5]) # Postion 5 to 5 from the end 
print(text2[:5]) # beginning to position 5
print(text2[0:10:2]) # Skip 2 
print(text2[-1::-1]) # Reverse
print(text2[::-1]) # Reverse

# String functions
print(multi.split(' '))
print(','.join(list))
print(text2.startswith('abc'))
print(text2.endswith('xyz'))
print(text2.find('jkl'))
print(text2.rfind('stu'))
print(text2.count('k'))
print(text2.isalnum())
print(text2.strip('a'))
print(text2.capitalize())
print(text2.title())
print(text2.upper())
print(text2.swapcase())
print(text2.replace('a', 'tmp'))
print(text2.replace('a', 'tmp', 100))

# Formatting
n = 21
f = 7.0
s = 'condesa'

print('{0} {1} {2}'.format(n, f, s))
print('{0:d} {1:f} {2:s}'.format(n, f, s))
print('{0:20d} {1:20f} {2:20s}'.format(n, f, s)) # field width
print('{0:<20d} {1:<20f} {2:<20s}'.format(n, f, s)) # field width, left align
print('{0:^20d} {1:^20.2f} {2:+^20s}'.format(n, f, s)) # field width, centered, with pad
print('{0:{fill}{align}{width}d} '.format(n, fill=' ', align='>', width=10))

# Shortcut
print(f'#Hello World! var: {n} {f} {s}')

ht = {'n': 42, 'f': 7.03, 's': 'cheese'}

print('{0[n]} {0[f]} {0[s]} {1}'.format(ht, 'other')) # format dictionary vals
