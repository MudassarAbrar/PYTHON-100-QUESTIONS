'''
Question 90
By using list comprehension, please write a program generate a 358 3D array whose each element is 0.

Hints: Use list comprehension to make an array.

'''

#to create a 3d array all the 3 dimmensions must be there so i assumed the remaining two myself
array_3d = [
            [
              [0 for _ in range(8)] 
                 for _ in range(5)]
                  for _ in range(358)]

print("3D array of shape (358, 5, 8):")
print(array_3d)
