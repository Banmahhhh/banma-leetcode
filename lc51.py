# n queen problem
# use a list queen[] to present the table
# the ith element of queen[] stores the queen's position of ith row
class Solution:
    def add_to_answer(self, queen, answer, n):
        temp = [['.' for i in range(n)] for j in range(n)]
        temp2 = []
        for i in range(n):
            temp[i][queen[i]] = 'Q'
            temp2.append(''.join(temp[i]))
        # print("temp2 is")
        # print(temp2)
        answer.append(temp2)
        return answer
    def valid(self, queen, i, j):
        for k in range(i):
            if queen[k] == j or abs(queen[k]-j) == i-k:
                return False
        return True
    def solveNQueens(self, n: int):
        answer = []
        grid = [['.' for i in range(n)] for j in range(n)]
        queen = [-1 for i in range(n)]
        i = 0
        j = 0
        while i < n:
            while j < n:
                if self.valid(queen, i, j):
                    queen[i] = j
                    j = 0
                    # print("1")
                    # print(queen)
                    break
                else:
                    j += 1
            if queen[i] == -1:
                if i == 0:
                    break # trace back to the first line, but still cannot find a answer, which means all answers are found
                else:
                    i -= 1
                    j = queen[i] + 1
                    queen[i] = -1
                    continue
            else:
                if i == n-1:                   
                    # print("success")
                    # print(queen)
                    answer = self.add_to_answer(queen, answer, n)
                    j = queen[i] + 1
                    queen[i] = -1
                    continue
                else:
                    j = 0
            i += 1
        print(answer)
        return answer
            
s = Solution()
s.solveNQueens(4)