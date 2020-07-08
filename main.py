val_list = ['0', '1', 'true', 'false']
func_list = {'and': lambda val_1, val_2: int(val_1 and val_2),
             'nand': lambda val_1, val_2: int(not(val_1 and val_2)),
             'or': lambda val_1, val_2: int(val_1 or val_2),
             'nor': lambda val_1, val_2: int(not (val_1 or val_2)),
             'xor': lambda val_1, val_2: 1 if val_1 != val_2 else 0,
             'xnor': lambda val_1, val_2: 1 if val_1 == val_2 else 0,
             'inv': lambda val_1: 1 if val_1 == 0 else 0,
             'buf': lambda val_1: int(val_1),
             'error': "error"
             }
func_names = []


def getFuncName(innerStr):
    func = innerStr.lower().split('(')[0].strip()
    if (func in func_list.keys()):
        return (func)
    else:
        return ('error')


def getValues(innerStr):
    if (getFuncName(innerStr) == 'and' or getFuncName(innerStr) == 'or' or
        getFuncName(innerStr) == 'nand' or getFuncName(innerStr) == 'nor' or
            getFuncName(innerStr) == 'xnor' or getFuncName(innerStr) == 'xor'):
        func_names.append(getFuncName(innerStr))
        if (len(innerStr.lower().split('(')[1].split(',')) > 2):
            return (func_list.get(getFuncName('error')))
        elif ((innerStr.lower().split('(')[1].split(',')[0].strip() not in val_list) or
                innerStr.lower().split('(')[1].split(',')[1].split(')')[0].strip() not in val_list):
            return (func_list.get(getFuncName('error')))
        else:
            if (innerStr.lower().split('(')[1].split(',')[0].strip() == '1' or
                    innerStr.lower().split('(')[1].split(',')[0].strip() == 'true'):
                val_1 = 1
            else:
                val_1 = 0
            if (innerStr.lower().split('(')[1].split(',')[1].split(')')[0].strip() == '1' or
                    innerStr.lower().split('(')[1].split(',')[1].split(')')[0].strip() == 'true'):
                val_2 = 1
            else:
                val_2 = 0
            res = func_list.get(getFuncName(innerStr))(val_1, val_2)
            return (('%(func)s(%(val_1)s %(val_2)s) = %(res)s.' % {"func": getFuncName(innerStr), "val_1":  val_1, "val_2": val_2, "res": res}))
    elif(getFuncName(innerStr) == 'buf' or getFuncName(innerStr) == 'inv'):
        func_names.append(getFuncName(innerStr))
        if(len(innerStr.lower().split('(')[1].split(',')) > 1):
            return (func_list.get(getFuncName('error')))
        elif(innerStr.lower().split('(')[1].split(')')[0].strip() not in val_list):
            return (func_list.get(getFuncName('error')))
        else:
            if (innerStr.lower().split('(')[1].split(')')[0].strip() == '1' or
                    innerStr.lower().split('(')[1].split(')')[0].strip() == 'true'):
                val = 1
            else:
                val = 0
            res = func_list.get(getFuncName(innerStr))(val)
            return (('%(func)s(%(val)s) = %(res)s.' % {"func": getFuncName(innerStr), "val":  val, "res": res}))
    else:
        return 'ooops...'


def main():
    try:
        f = open('file.txt', 'r')
        inner = (f.read().split('\n'))
        f.close()
        for i in inner:
            print(getValues(i))
        print(('\nFull elems list %(func)s' % {"func": set(func_names)}))
    except FileNotFoundError:
        print("can't open file")


main()
