
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
 
#check for string case
upper_case = user_range.isupper() * alphabet.upper()
lower_case = user_range.islower() * alphabet.lower() 
check_case = upper_case + lower_case

#identify location of the start and end of the range
firstlocation = check_case.index(user_range[0])
lastlocation = check_case.index(user_range[-1])

#get range of the characters
result_string = check_case[firstlocation:lastlocation + 1]


#Print Result string
print(result_string)
     