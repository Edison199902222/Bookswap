class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        desk = collections.defaultdict(collections.Counter)
        meal = set()
        for _, table, food in orders:
            meal.add(food)
            desk[table][food] += 1
        foods = sorted(meal)
        result = [['Table'] + [food for food in foods]]
        for table in sorted(desk, key=int):
            temp = []
            temp.append(str(table))
            for food in foods:
                temp.append(str(desk[table][food]))
            result.append(temp)
        return result

'''
先创建一个ddefaultdict(collections.Counter) 这个的意思就是 默认value 是 括号里面的东西
collections.Counter 也是一个字典 
创建一个meal set
然后遍历order 
把table 代表桌子号 把food 放进meal中
然后 把 table 作为desk 的key 对应 一个 字典 counter
counter中有 food作为key 出现的次数作为 value
遍历完成后 排序foods
然后 遍历 排序好的desk
创建一个 list，把table number 放进temp中 再遍历 foods 把 对应的次数添加进去
'''