#!/usr/bin/env python3

class College(object):
    
    def __init__(self, collegename):
        self.collegename = collegename
        
    def professor(self, profname, profsurname):
        self.profname = profname
        self.profsurname = profsurname
    
    def student(self, studname, studsurname):
        self.studname = studname
        self.studsurname = studsurname

    def get_college_name(self):
        print(self.collegename)
    
    def get_professor(self):
        print(self.profsurname, self.profname)

    def get_student(self):
        print(self.studsurname, self.studname)
        

a = College('Cambridge')
a.get_college_name()
a.professor('Evgeny','Shmarnev')
a.get_professor()
a.student('Lucie','Jablonska')
a.get_student()


