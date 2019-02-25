# bad implementation
# need to optimize
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        else:
            buttons = [" ", "*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
            answer = [""]
            
            for i in range(len(digits)):
                a_temp = answer
                answer = []
                for j in range(len(buttons[int(digits[i])])):
                    for k in range(len(a_temp)):                     
                        answer.append(a_temp[k] + buttons[int(digits[i])][j])
        return answer
                    