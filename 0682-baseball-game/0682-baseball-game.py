class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        
        for i in range(len(operations)):
            if operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                last_el_double = stack[-1] * 2
                stack.append(last_el_double)
            elif operations[i] == "+":
                last_2_ele = stack[-1] + stack[-2]
                stack.append(last_2_ele)
            else:
                stack.append(int(operations[i]))
        print(stack)
        if stack:
            return sum(stack)
        else:
            return 0