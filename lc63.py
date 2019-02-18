'''
dynamical programming!!!!!!!
why you are so stupid
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        r = len(obstacleGrid[0])
        c = len(obstacleGrid)
        a = [[0 for i in range(r)] for j in range(c)]
        for i in range(c):
            # print("i is", i)
            if obstacleGrid[i][0] != 1:
                a[i][0] = 1
            else:
                break
        for i in range(r):
            # print("i is ", i)
            if obstacleGrid[0][i] != 1:
                a[0][i] = 1
            else:
                break
        for i in range(1,c):
            for j in range(1,r):
                if obstacleGrid[i][j] != 1:
                    a[i][j] = a[i-1][j] + a[i][j-1] 
        print(a[c-1][r-1])
        return a[c-1][r-1]