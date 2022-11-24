a=[11,12,13,14,"hello",33,66]
try:
    for i in range(10):
        print("Value :",a[i]/2)
except TypeError:
    print("Not a valid value")
except IndexError:
    print("Not a valid range")
print("Bye...")
