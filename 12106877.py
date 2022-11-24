'''Write a python program to split a list every Nth element.
sample list:['a','b','c','d','e','f','g','h','i','j','k','l','m','n'].
Excepted output:[['a','d','g','j','m']['b','e','h','k','n']['c','f','i','l']]'''

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
new_list = []
n = 3
for i in range(n):
    new_list.append(list[i::n])
    print(new_list)
