x = int(input("enter value for x: "))

# 210

if (x < 110) or (x > 100):
# probably meant this instead: if 100 < x < 110:
    print('One')
elif (x >= 200) and (x <= 210):
    print('Two')
else:
    print('Three')
