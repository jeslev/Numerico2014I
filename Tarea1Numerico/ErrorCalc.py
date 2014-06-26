import sys

class ErrorCal:
    
    def __init__(self,num):
        self.num = num
        
        	
    def getAbsoluteError(self):
        st = str(self.num)
        n = '%.52f' % float(st)
        pos = st.find('.');
        tam = 0
        if pos>0:
            tam = len(st)-pos-1
            st2 = st
            for i in range (0,52-tam):
                st2+='0'
        #print pos, st2, tam  #original
        #print pos, n, tam	 #nuevo
        if n == st2:
            return '0.00000000000000000', '0.00000000000000000', '0'
        for i in range (0, len(n)):
            if n[i]!=st2[i]:
                pos2 = i
                n1 = n[i:]		#nuevo
                n2 = st2[i:]	#original
                res = int(n2)-int(n1)	#x-fl(x)
                #print res
                break
        res = str(res)
        pot = len(n1)-len(res)
        pot += pos2-pos
        if res[0]=='-':
            res1 = '0.'+res[1:]
        else:
            res1 = '0.'+res
        r=st2[:pos] + st2[pos+1:pos+1+pot]

        relativo = '%.17f' % (float(res1[2:2+pot])/float(r))
        if relativo[0]=='-':
            relativo = relativo[1:]
        res1 = res1[:20]
        pot*=-1
        #print r, "pot: ", pot, relativo
        return relativo, res1, pot
