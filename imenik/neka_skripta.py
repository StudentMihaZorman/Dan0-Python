import copy


def vhodnaF():
    """test = 1
    l1 = [1,'Miha',True,0.004,test,[1,0.4]]
    print(l1[1])

    d1 = {'ABC':123,17:'nekaj'}
    print(d1['ABC'])

    t1 = (1,7,4,)

    l1[2]= False
    print(l1)

    l1.append(1111)
    print(l1)

    l1.pop()
    print(l1)

    l1.insert(3,'novo')
    l1.remove(1)
    print(l1)
    print(l1.index('novo'))

    d1['nekaj']= 827373  """

    l1 = [1,2,4]
    l2 = copy.deepcopy(l1)

    l2.append(7)

    print(l1)
    print(l2)









if __name__ == "__main__":
    vhodnaF()