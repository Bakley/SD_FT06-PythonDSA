
x = []



def reverse(x):
    
    # loop thru the arry in half
    for element in range(len(x)// 2):
        right_pointer = len(x) - 1 - element
        x[element], x[right_pointer] = x[right_pointer], x[element]

    return x








print(reverse([2,3,45,78,68,90,56]))