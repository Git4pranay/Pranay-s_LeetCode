class Solution:
    def isValid(self, s):
        stack=['-']
        for i in range(len(s)):
            if s[i]=='(':
               stack.append('(')
            elif s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif s[i]==')':
                stack.append(')')
            
            if s[i]=='[':
                stack.append('[')
            elif s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif s[i]==']':
                stack.append(']')
            
            if s[i]=='{':
                stack.append('{')
            elif s[i]=='}' and stack[-1]=='{':
                stack.pop()
            elif s[i]=='}':
                stack.append('}')
        if stack[-1]=='-':
            return 1
        return 0
            
            

    
