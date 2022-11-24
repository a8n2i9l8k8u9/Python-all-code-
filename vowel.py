my_list=['RAM','ROM','PROM','RAM','ROM']
print("List Before",my_list)
temp_list= []
for i in my_list:
    if i not in temp_list:
        temp_list.append(i)
my_list=temp_list
del temp_list
print("List After removing duplicates",my_list)
