
w = "wombat"
x = 23.2390239203
y = "Hello"

print(w, x, y)     #   print(str(x), str(y))
print("next line")
print()
print('next line')

print(w, x, y, sep=".")
print(w, x, y, sep="/")
print(w, x, y, sep="")
print(w, x, y, sep=" ==> ")

print("watch this!", end="\n\n")
print("welllll", end=' ')
print("doggies")

print(x, y, sep=' ', end='\n')

print("ok", end='')
print("ok")

print("value is", x)

#               place
#               holder
print("value is {:.2f}".format(x))
print(f"value is {x:.2f}")  # fstring or "formatted string"

person = 'Fred Flintstone'
city = "Bedrock"

print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")

#  .nf   float to n decimal places
#  d     decimal integer
#  s     str (usually not needed)

print(f"{person:>20s} {city:>20s}")
print(f"{person:20s} {city:20s}")
print(f"{person:^20s} {city:^20s}")

bn = 23985029384203984209384209384209384029384029384

print(f"{bn:,d}")

bln = 23_985_143_902

print(bln)


