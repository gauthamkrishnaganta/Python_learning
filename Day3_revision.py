'''
blocks > procedures -> functions(def)
functions -> reusable block of code (A block of statements which perform specific tasks)

syntax:

def <funcname> (parameters): #func defining
    """DOC String"""
    statements(s)....
    ................     #body of function
    return value(s)
fname(args) #func call

def add(a,b):
    """ Addition function"""
    ans = a+" "+b
    return ans

def add(a,b):
    """ Addition function"""
    ans = a+" "+b
    return ans
a,b = map(str,input("Enter the two words: ").split(","))
print(add(a,b))

# VARIABLE LENGTH ARGUMENTS -> *args we can pass any number of positional
#arguments->  data will be stored in tuple

def sample(*a):
    """demo of variable length arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,3,4)
sample('gautha',1,2,3,"krishna")
marks = [12,20,30,40]
sample(marks)
sample(*marks)

a,*b,c = "gautham", 1,2,3 ,"krishna"
print(a)
print(b)
print(c)

def add(*G):
    #perform addition on given input values
    ans = 0
    for i in G:
        if type(i) == int or type(i) == float:
            ans = ans + i
    return ans
print(add(2,3,4.5))
print(add(2,3,4,"gautham"))
keyword arguments -> we can pass the name for the arguments

def batch(name,age,place="hyd"):
# def batch(name="gautham",age,place="hyd"): error -> non default always follows default argument
    """keyword arguments usage"""
    print(f'{name} {age} {place}')
batch("gautham",23,"vizag")
batch(place="vizag",name="gautham",age = 21)
batch(name="gautham",age=21)
#keyword variable length arguments(**kwargs) -> Any number of positional
#keyword Arguments, data is tored in dictionary

def batch(**a):
    """keyword variable length argument usage"""
    print(a)
    print(type(a))
batch()
batch(name = "gautham",age = 21,place = "hyd")
data = {'names':['gautham','krishna'],
        'place':["vizag","hyd"]
        }
data.update({'batch':"PFS-005"})
batch(**data)
'''
def driving_li(*a,**b):
    if a









