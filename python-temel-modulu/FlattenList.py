array = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def FlattenList(array):
    for i in range(0,len(array)):
        if IsList(array[i]):
            FlattenList(array[i])
        else:
            l.append(array[i])
    return l

def IsList(array):
    if type(array) == list:
        return True
    else:
        return False
    
l = []
