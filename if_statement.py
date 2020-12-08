x = 65

if x > 75:
    print("wombat")
    print("quokka")
elif x > 50:  # else if
    print("wallaby")
    print("kookaburra")
    if x > 60:
        print("crocodile")
else:
    print("platypus")
    print("kangaroo")

print("All done")

# X is FALSE if
# X == 0
# len(X) == 0
# X is None or False

# otherwise, TRUE

#  True, False


#   if then else
#   A ?B    :C

#  B if A else C

condition = 4

color = 'green' if condition == 5 else 'red'
print(color)

#   == != > < >= <=

#  if (name == user_name) and (balance < 10):
#     print('blah blah')

#   and or

#   T and T -> T
#   T and F -> F
#   F and T -> F
#   F and F -> F

#   T or T -> T
#   T or F -> T
#   F or T -> T
#   F or F -> F


default = 50
input_value = ""

value = input_value or default

print(int(value))









#  not    flips boolean value T->F  F->T

