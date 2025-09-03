# # # list = ["red","yellow","green","purple","pink"]

# # # print(list[:4])
# # # list[1] = ["maroon"]
# # # print(list)
# # # # ----------------------

# # color = ['yellow', 'black', 'red', 'purple']
# # # print(color[::-1])
# # # print(color[1:3])
# # print(color[1][::-1])
# # print(color[-1])

# lst = ['black','brown','yellow']
# print(lst.pop())
# print(lst)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)