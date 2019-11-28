class MyException(Exception):
    def __init__(self,v):
        self.v=v


def xyz():
    a=input('Enter first number\n')
    b=input('Enter second number\n')
    sum = a + b
    if sum < 150:
        raise MyException('Custom Exception Occurred')

if __name__=="__main__":
    xyz()