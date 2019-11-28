def exceptionHandling():
    a = 10
    try:
        a+='string'
    except Exception as e:
        print(e)

    try:
        a.abcd()
    except Exception as e:
        print(e)

    try:
        int('string')
    except Exception as e:
        print(e)

if __name__=="__main__":
    exceptionHandling()