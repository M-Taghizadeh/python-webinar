import re
txt = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, ipsum quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint ipsum occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit Lorem 
"""

token_list = re.findall(" [a-z]+ ", txt)
print(token_list)


# search() : returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned
x = re.search(" i.{4} ", txt)
print(x)