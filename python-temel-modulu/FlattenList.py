array = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def IsList(array):
    if type(array) == list:
        return True
    else:
        return False
    
def FlattenList(array):
    global l
    l=[]
    length = len(array)
    for i in range(0,length):
        if IsList(array[i]):
            f(array[i])
        else:
            l.append(array[i])
    return l
  
l=[]

print(FlattenList(array))
