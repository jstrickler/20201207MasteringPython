
color = "blue"  #  GLOBAL name (file scope)

def spam():
    band = "Pink Floyd"   # LOCAL name
    print("in spam(), color is", color)


spam()
print("color is", color)

