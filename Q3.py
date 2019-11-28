def error():
    try:
        a = int(input('Enter a number'))
    except Exception as e:
        print(type(e).__name__, e)
    except KeyboardInterrupt as e:
        print('\n',type(e).__name__)

if __name__=="__main__":
    error()