# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# class Solution:
#     def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
#         answer = []
#         l = len(intervals)
#         axis = [[0 for x in range(2)] for y in range(l*2)]
#         ori_list = []
#         for i in range(l):
#             print(intervals[i].start)
#             axis[2*i][0] = intervals[i].start
#             axis[2*i][1] = i
#             axis[2*i+1][0] = intervals[i].end
#             axis[2*i+1][1] = i
#             ori_list.append(intervals[i].start)
#             ori_list.append(intervals[i].end)
#         print(ori_list)
#         axis.sort(key=lambda x: x[0])
#         print(axis)
#         temp = 0 #check whether it is start or end of the result interval, 0 is start, 1 is end
#         start=0
#         end=0
#         for i in range(2*l):
#             if temp == 0:
#                 start = axis[i][0]
#                 temp = 1
#                 end = ori_list[axis[i][1]]
#             elif temp == 1:
#                 if axis[i][0] != end:
#                     if ori_list[axis[i][1]] > end:
#                         end = ori_list[axis[i][1]]
#                 else:
#                     if i<(2*l-1) and axis[i][0] == axis[i+1][0]:
#                         if ori_list[axis[i+1][1]] > end:
#                             end = ori_list[axis[i+1][1]]
#                     else:
#                         answer.append([start, end])

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        answer = []
        intervals.sort(key=lambda x: x.start)
        
        for inter in intervals:
            if len(answer)>0 and answer[-1].end>=inter.start:
                answer[-1].end = max(answer[-1].end, inter.end)
            else:
                answer.append(inter) 
        return answer

