data = [(1, 'David'), (2, 'Charlie'), (7, 'Alice'), (4, 'Brian'), (5, 'Ouma'), (6, 'Stanley'),(3, 'Willy')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)


num = [2.3,6,8,2,6,3,66,8]

sqtr_num = list(map(lambda x: x**2, num))
print(sqtr_num)
