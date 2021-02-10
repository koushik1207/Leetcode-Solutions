class Stack:
    def __init__(self):
        self.items = []
    def push(self,ele):
        self.items.append(ele)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

class Solution:
    def is_match(self,a,b):
        if a =="(" and b ==")":
            return True
  
        elif a =="{" and b =="}":
            return True
        
        elif a =="[" and b =="]":
            return True
        
        else:
            return False
    
    def isValid(self, s: str) -> bool:
        stk = Stack()
        is_bal = True
        index = 0
        while index < len(s) and is_bal:
            text = s[index]
            if text in "([{":
                stk.push(text)
            else:
                if stk.is_empty():
                    is_bal = False
                else:
                    top = stk.pop()
                    if not self.is_match(top,text):
                        is_bal = False
            index += 1
        if stk.is_empty() and is_bal:
            return True
        else:
            return False