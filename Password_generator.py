import random
print("Welcome to Password Generator")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*']
numbers=['0','1','2','3','4','5','6','7','8','9']
n_letters=int(input("Enter how many letters you want in your password"))
n_symbols=int(input("Enter how many symbols you want in your password"))
n_numbers=int(input("Enter how many numbers you want in your password"))
password=[]
for i in range(1,n_letters+1):
    password.append(random.choice(letters))
for i in range(1,n_symbols+1):
    password.append(random.choice(symbols))
for i in range(1,n_numbers+1):
    password.append(random.choice(numbers))
random.shuffle(password)
passwordgen=""
for i in password:
    passwordgen+=i
print(passwordgen)

