from multipledispatch import dispatch
class Parent(object):
    @dispatch(str,int,str)
    def __init__(self,name,age,gender):
        self.pname= name
        self.page=age
        self.pgender=gender
        print(self.pname,self.pgender,self.page)
    @dispatch(str,int,str,str)
    def __init__(self,name,age,gender,parent):
        self.cname=name
        self.cage=age
        self.cgender=gender
        self.parent=parent
        print(self.cname,self.cage,self.cgender,self.parent)
obj=Parent('neelu',25,'female','dad')
obj=Parent('vani',45,'female')
