#9. Count:  Write a program to count vowels, consonants, digits and special characters in a given string. 

string = input("Enter a a string : ")

vowels = 'aAeEiIoOuU'
vowels_count = 0
consonants = 0
digits = '0123456789'
digits_count = 0
sp_char = '!@#$%^&*()_-?/'
sp_char_count = 0
others = 0

for i in string:
    if i in vowels:
        vowels_count+=1
    elif i.isalpha() :
        consonants+=1
    elif i in digits:
        digits_count+=1
    elif i in sp_char :
        sp_char_count+=1        
    else : 
        others += 1
        print("this are not among this criteria")

print("vowels_count : ",vowels_count)
print("consonants : ",consonants)
print("digits : ",digits_count)
print("sp_char : ",sp_char_count)
print("others : ",others)

     



