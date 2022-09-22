
from logging import exception

import time
def main():
    l1 =[1,7,4,6,4,3,3]
    

    for i in l1:
        print(i)

    l2 = [vred for vred in l1 if vred < 5]
    print(l2)

    d1 = {1:'a',2:'b',3:'c',4:'d'}
    for _,v in  d1.items():
        print(v)



    try:
        d0 =1/0
    except Exception as e:
        print("ni slo - "+str(e))

    finally:
        print('zakljuceno')



    try:
        while True:
            print('Nekaj')
            time.sleep(1)
    except KeyboardInterrupt:
        print('konec')












if __name__ == "__main__":
    main()