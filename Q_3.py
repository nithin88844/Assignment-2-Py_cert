# # A regular expression is a sequence of characters that define a search pattern. 
# It is mainly used for string pattern matching.




Regex_Pattern = r'hackerrank'
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match)) 

