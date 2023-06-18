class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank):
        t1=mainTank
        t2=additionalTank
        ans=0
        tt1=1
        while(t1>0):
            t1-=1
            if(t2>0):
                if (tt1%5==0):
                    ans+=1
                    t1+=1
                    t2-=1
            tt1+=1
        return mainTank*10+ans*10
        