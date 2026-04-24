class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        mem = {}
        def help(exp):
            if exp in mem:
                return mem[exp]
            if exp.isdigit():
                return [int(exp)]
            ans = []
            for i in range(len(exp)):
                if exp[i] == "+" or exp[i] == "-" or exp[i] == "*":
                    left = help(exp[:i])
                    right = help(exp[i+1:])
                    if exp[i] == "+":
                        for j in range(len(left)):
                            for k in range(len(right)):
                                ans.append(left[j] + right[k])
                    if exp[i] == "-":
                        for j in range(len(left)):
                            for k in range(len(right)):
                                ans.append(left[j] - right[k])
                    if exp[i] == "*":
                        for j in range(len(left)):
                            for k in range(len(right)):
                                ans.append(left[j] * right[k])
                mem[exp] = ans
            return ans
        return help(expression)
        
