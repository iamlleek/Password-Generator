import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789" 
symbols = "(){}[],;:.-_/\\ ?+*# "

all =uppercase_letters + lowercase_letters + digits + symbols
length = 9
password = "".join(random.sample(all,length))
print(" The Password You Generated is :",password)