
s = 'Chris Hemsworth'

s1 = s.upper()
s_len = len(s)

print(s, s1, s_len)

print(s.upper(), s.lower(), s.capitalize(), s.title())
print(s.startswith('Chris'), s.startswith('Liam'))  # also s.endswith()

print(s.count('h'))

print(s.lower().startswith('chris'))

#  method().method().method() ...     method chaining

print("em" in s.lower())   # contains
print("ch" in s.lower())

print(s.lower().count('h'))

s = "  \t  \n    \r  \t       all my exes live in Texas          "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xxyyxxxyyyxyxxxxxxxxxAll my exes live in Texasyyyyyyyyyyyyyyyx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()


s = "fee:fi:fo:fum"
words = s.split(':')
print("words:", words)

s = "Mary had a little      lamb"
words = s.split()
print("more words:", words)


x = "foo'bar'blah"

words = x.split("'")
print("even more words:", words)

