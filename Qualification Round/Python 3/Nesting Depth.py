#Basil Chacko Mathew Code is for Code Jam 04/04/2020

import re, os
b = []
s = []
def main():
    t = int(input())
    for x in range(1,t+1):
        s = input()
        splist = list(filter(None, re.split('(0+)', s)))
        for i in (splist):
            if "9" in i:
                lists = ["(((((((((",")))))))))"]
                a = "".join(i).join(lists)
                b.append(a)
            elif "8" in i:
                lists = ["((((((((","))))))))"]
                a = "".join(i).join(lists)
                b.append(a)
            elif "7" in i:
                lists = ["(((((((",")))))))"]
                a = "".join(i).join(lists)
            elif "6" in i:
                lists = ["((((((","))))))"]
                a = "".join(i).join(lists)
                b.append(a)
                b.append(a)
            elif "5" in i:
                lists = ["(((((",")))))"]
                a = "".join(i).join(lists)
                b.append(a)
            elif "4" in i:
                lists = ["((((","))))"]
                a = "".join(i).join(lists)
                b.append(a)
            elif "3" in i:
                lists = ["(((",")))"]
                a = "".join(i).join(lists)
                b.append(a)
            elif "2" in i:
                lists = ["((","))"]
                a = "".join(i).join(lists)
                b.append(a)
            elif "1" in i:
                lists = ["(",")"]
                a = "".join(i).join(lists)
                b.append(a)
            else:
                b.append(i)
                continue
        y = "".join(b)
        print('Case #{}: {} '.format(x, y))
        del y
        b.clear()
if __name__ == '__main__':
    main()
