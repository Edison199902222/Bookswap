
'''
创建两个字典
一个放重要性 一个放id
res存储累计重要性
遍历 id 同时 在重要性的字典里 累加
'''
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates



class Solution:
    def getImportance(self, employees, id: int) -> int:
        importantce = {}
        subid = {}
        for employee in employees:
            importantce[employee.id] = employee.importance
            subid[employee.id] = employee.subordinates
        res = self.dfs(importantce,subid,id)
        return res


    def dfs(self,importance,subid,id):
        res = importance[id]
        for _id in subid[id]:
            res += self.dfs(importance,subid,_id)
        return res

if __name__ == "__main__":
    solution = Solution()
    list1 = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    print(solution.getImportance(list1,1))