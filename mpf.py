data=[2,3,5,7,4,9,6]

# def even(self):
#     for i in data:
#         if i%2==0:
#             print(i) 

# even(data)     

even=list(filter(lambda n : n%2 == 0, data))
print(even)



