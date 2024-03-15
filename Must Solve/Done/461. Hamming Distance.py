class Solution:
    def hammingDistance(self,x,y):
        bx = bin(x)[2:]
        by = bin(y)[2:]
        xL = len(bx)
        yL = len(by)
        nbx=""
        nby=""
        if xL>yL:
            nby="0"*(xL-yL)+by
            nbx = bx
        elif xL<yL:
            nbx="0"*(yL-xL)+bx
            nby = by
        else:
            nbx = bx
            nby=by
        i = 0
        counter=0
        while i<len(nbx):
            if nbx[i]!=nby[i]:
                counter+=1
            i+=1
        
        return counter
            