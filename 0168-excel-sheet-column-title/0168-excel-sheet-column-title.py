class Solution:

    def convertToTitle(self, c: int) -> str:
        l = 'abcdefghijklmnopqrstuvwxyz '
        b = c%26
        a = c//26
        ans=''
        if b==0:
            ans+='z'
            a=a-1
        ans += l[b-1]
        if a>26:
            while(a>26):
                b = a%26
                a = a//26
                ans+=l[b-1]
        ans+=l[a-1]
        return ans[::-1].upper().replace(' ','')

        
        