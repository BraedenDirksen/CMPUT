def test():
    li = []
    if len(li) == 0:
        raise Exception('list is empty')
    else:
        return li.pop()

try:
    test()
except Exception as error:
    print(error.args)


    
input()