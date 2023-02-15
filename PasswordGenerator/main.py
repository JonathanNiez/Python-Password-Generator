import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._"
length = 16

all = lower + upper + numbers + symbols
password = "".join(random.sample(all,length))

print(password)