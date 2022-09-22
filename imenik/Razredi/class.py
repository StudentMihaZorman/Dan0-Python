from ast import Return


predmeti = {'KMS':,'KDR':,''}:,

class Student(object):
    def __init__(self,ocena,vpisna_st,ime,primek):
        self.ocena = ocena
        self.vpisna_st = vpisna_st
        self.primek = primek

    def napreduje(self):
        if self.ocena > 5:
            return True
        else: 
            return False




class Student(object):
    def __init__(self,spisek_studentov):