class Solution:
    def letterCombinations(self, digits):
        dic = {}
        dic['2']='abc'
        dic['3']='def'
        dic['4']='ghi'
        dic['5']='jkl'
        dic['6']='mno'
        dic['7']='pqrs'
        dic['8']='tuv'
        dic['9']='wxyz'
        
        return map("".join,product(*(dic[i] for i in digits))) if digits else []        

                
                
            
        