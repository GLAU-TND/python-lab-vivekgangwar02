def exceptionHandling():
    a = 10
    try:
        a+='string'
    except Exception as e:
        print(type(e).__name__,e)

    try:
        a.abcd()
    except Exception as e:
        print(type(e).__name__,e)

    try:
        int('string')
    except Exception as e:
        print(type(e).__name__,e)

if __name__=="__main__":
    exceptionHandling()