
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

#get user input range
user_range= input("Enter a range of letters (e.g., a-z): ")

alphabet = "abcdefghijklmnopqrstuvwxyz"


#split the user's input
first, last = user_range.split('-')


#identify location of the start and end of the range
firstlocation = alphabet.index(first.lower())
lastlocation = alphabet.index(last.lower())

#get range of the characters
result_string = alphabet[firstlocation:lastlocation + 1]

#identify if user input is upper or lower, if true, it will print accordingly 
#(the false part will return 0 and so only the true part will be printed)
result_string = first.isupper() * result_string.upper() + first.islower() * result_string.lower() 


#Print Result string
print(result_string)
     