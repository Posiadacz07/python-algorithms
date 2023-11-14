# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

length = len(test_str)

digits = len([chr for chr in test_str if chr.isdigit()])

punctation = len([chr for chr in test_str if chr in string.punctuation])

unique_letters = "".join({chr for chr in test_str if chr.isalpha()})

unique_count = len(unique_letters)

# print the data
str_data = { "Length" : length, 
             "Digits" : digits,
             "Punctation" : punctation,
             "Unique Letters" : unique_letters,
             "Unique Count" : unique_count
}
pprint.pp(str_data)