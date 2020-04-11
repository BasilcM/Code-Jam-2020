#Code Jam 2020
#@Author : Basil Chacko Mathew For CodeJam

import numpy as np 
def main():
    t = int(input())
    for i in range(1,t+1):
        n = int(input())
        m = []
        while not m or len(m) < len(m[0]):
            if (len(m)<=n):
                m.append(list(map(int, input().split())))
        gfg = np.matrix(m) 
        k = gfg.trace() 
        def countIdenticalRows(mat): 
            count = 0
            for i in range(len(mat)): 
                a = []
                for j in range(len(mat[i])): 
                    #Add all the values of the row in HashSet 
                    a.append(mat[i][j])
                hr = set([x for x in a if a.count(x) > 1])
                if (len(hr)>0): 
                    count+=1
            return count 
        r = countIdenticalRows(m)
        def countIdenticalColumns(mat): 
            count = 0
            for i in range(len(mat)):
                b = []
                for j in range(len(mat[i])): 
                    #Add all the values of the Column in HashSet 
                    b.append(mat[j][i])
                    
                #Check if size of HashSet = 1 
                hc = set([x for x in b if b.count(x) > 1])
                if (len(hc)>0): 
                    count+=1
            return count
        c = countIdenticalColumns(m)
        print('Case #{}: {} {} {}'.format(i, int(k), int(r), int(c)))

if __name__ == '__main__':
    main()
