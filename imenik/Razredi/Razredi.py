



class Pravokotnik(object):
    def __init__(self,a,b):
        barva = 'Rdeca'
        print('pravokotnik')
        self.a = a
        self.b = b

    def ploscina(self):
        return self.a*self.b
    def obseg(self):
        return 2*self.a+2*self.b

    def __del__(self):
        print('brisem pravokotnik')


prav1 = Pravokotnik(5.0,4.0)
prav2 = Pravokotnik(3.0,4.0)
prav1.ploscina()

#print(prav1.ploscina())
#print(prav1.obseg())

class Kvadrat(Pravokotnik):
    def __init__(self,a):
        super(Kvadrat,self).__init__(a,a)
if __name__ == "__main__":
    kv1 = Kvadrat(4.0)



print(kv1.obseg())
print(kv1.ploscina())
