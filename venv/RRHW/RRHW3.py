# my_list = ['a', 'b', [1,2,3],'d']
# print(my_list[2])
# x = my_list[2]
# print(f'{x[0]}, {x[1]}, {x[2]}')
# print(f'{my_list[2][0]}, {my_list[2][1]}, {my_list[2][2]}')

# l1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = [i+=i for i in l1 if isinstance(i,int)]
# sum = 0
# for i in l1:
#     if isinstance(i, int):
#         sum += i
# print(f'the sum is: ', sum)
# l2 = [l2.append(x) for x in l1 if isinstance(x, str) if 'a' in x]
# l2 = []
# for x in l1:
#     if isinstance(x,str):
#         if 'a' in x:
#             l2.append(x)
# print(l2)

# l = ['cat','dog', 'horse', 'cow']
# print(tuple(l))

fam1 = input('Please enter name: ').split()
fam2 = input('Please enter name: ').split()
if len(fam1) > len(fam2):
    print(f'Family 1 is bigger.')
elif len(fam1) < len(fam2):
    print(f'Family 2 is bigger.')
else:
    print(f'Equal')

# film = {'title': 'Mumu', 'director': "Tolstoy", 'year': 2000, 'budget': 1000000,}
# print(film.keys())
# print(film.values())
# print(film)
# print(film.items())

# my_dict = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum = 0
# for i in my_dict.values():
#     sum += i
# print(sum)

# l = [1,2,3,4,5,3,2,1]
# a = set(l)
# print(a)
