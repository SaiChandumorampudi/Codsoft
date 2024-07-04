import random
digits="0123456789"
lowercase="abcdefghijklmnopqrstuvwyz"
UPPERCASE="ABCDEFGHIJKLMNOPQRSTUVWYZ"
symbols='{}[],.<>/?!@#$%^&*()_-=+;:'"\|"
join=UPPERCASE+lowercase+digits+symbols
length=9 
passcode="".join(random.sample(join,length))
print("the password is:",passcode)