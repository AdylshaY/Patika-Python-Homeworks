array = [[1, 2], [3, 4], [5, 6, 7]]
l = []

def IsList(array):
    if type(array) == list:
        return True
    else:
        return False
    
def ReverseList(array):
    for i in array:
        l.append(i[::-1])
    return l[::-1]

print(ReverseList(array))
