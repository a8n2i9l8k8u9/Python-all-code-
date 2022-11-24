''' Write a python program to find the indices  for which  the  numbers in the list drops.
NOTE: You  can detect multiple drops just by checking if nums[i] < num[i-1]

Input :
[0,-1,3,8,5,9,8,14,2,4,3,-10,10,17,41,22,-4,-4,-15,0]
Output:
[1,4,6,8,10,11,15,16,18]
Input:
[6,5,4,3,2,1]
Output:
[1,2,3,4,5]'''

def anil(list):
   drop_indices = []
   for i in range(1, len(list)):
       if (list[i] < list[i - 1]):
           drop_indices.append(i)
   return drop_indices
list = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
print("Before Indices List :-> ",list,end=" ")
print("\nAfer Indices List :-> ",anil(list),end=" ")
list=[6,5,4,3,2,1]
print("\n\nBefore indices list:-> ",list,end=" ")
print("\nAfter indices list:-> ",anil(list),end=" ")



    
