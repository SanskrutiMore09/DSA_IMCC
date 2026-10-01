#11. Reverse Words: Write a program to accept a sentence and display by reversing words in a sentence. Ex. “the sky is blue” => “eht yks si eulb” 

string = input("enter a sentence : ")
print("original sentence : ",string)
print("reversed sentence : " ,string[: : -1])