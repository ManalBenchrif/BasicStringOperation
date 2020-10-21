#Strings are bits of text. They can be defined as anything between quotes:
sentence="my name is manal,i'm 21 years old ^_^"

 #print lenght of a string
print("the lenght of name is: ",len(sentence))

 #print the location of the first occurrence of the letter "i", this method only recognizes the first.
print("first occurrence of 'i' is: ",sentence.index("i"))  #why 8 not 9? #Python start things at 0 instead of 1. .
  
  #This counts the number of 'm'' in the string.
print("number of 'm' in name is :",sentence.count('m'))

  #prints a part of the string, starting at index 3, and ending at index 6. 
print("new string start at 2 & end at 5 :",sentence[3:6]) #pay attention!!!! it end at index 5 not 6

  #print letter in a specific index
print("letter in index 5:",sentence[5])

   #print a string start at specific index
print("from index 5 to end:",sentence[5:])

   #print a string start at specific index
print("end et  index 20 to end:",sentence[:20])
   
   #You put negative numbers inside the brackets.it's an easy way to start at the end of the string instead of the beginning. 
print("start from end index -3:",sentence[-3:]) #3 means 3rd character from the end".

   #the general form is[start:stop:step]. by default [start:stop:1].
name="manal benchrif"
print("[start:stop:step]:",name[0:8:2]) #manal be
   
   #reverse a string
print("reverse name:",name[::-1]) 

   # all letters converted to uppercase and lowercase for new string
name1="PositiVe"
print("uppercase:",name1.upper())
print("lowercase:",name1.lower())

   # determine if string starts with something or ends with something . it return true or fils
print("is name1 start with 'man? ",name1.startswith("man"))
print("is name1 end with 'iVe? ",name1.endswith("iVe"))

   #This splits the string into a bunch of strings grouped together in a list. difference between items of list is space 
name3="hello everyone ^_^"
print("divide the sentence in a list: ",name3.split())

    
    