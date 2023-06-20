class Solution:
    def romanToInt(self, s) :
        dic = {}
        dic['I']=1
        dic["V"]=5
        dic["X"]=10
        dic["L"]=50
        dic["C"]=100
        dic["D"]=500
        dic["M"]=1000
        ans=0
        i=0
        while(i<len(s)-1):
            a=dic[s[i]]
            b=dic[s[i+1]]
            if a<b:
                ans+=b-a
                i=i+1
                print(b-a)
            else:
                ans+=a
                print(a)
            i+=1
        if i<len(s):
            ans+=dic[s[i]]
            
        
        return ans