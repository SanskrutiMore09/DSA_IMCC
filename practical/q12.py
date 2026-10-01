#12. Find longest and shortest words: Write a program to accept a sentence and find the longest and shortest word in a sentence.  

sentence = input("enter a sentence : ")
words = sentence.split()
if words :

    shortest = words[0]
    longest = words[0]

    for word in words:
        if (len(word)<len(shortest)) :
            shortest = word 
        if (len(word)>len(longest)) :
            longest = word
        

    print("smallest : ",shortest)
    print("largest : ",longest)
else:
    print("no words entered ")
