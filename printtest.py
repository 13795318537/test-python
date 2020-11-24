# print('test123')


# name = 'zhuyaoqi'
# age = 30
# if name == input('qingshuruxingm:'):
#     print('yes')
# else:
#     print('no')

#=======================
# import random
# while True:
    
#     player = int(input('请输入剪刀0,石头1,布2:'))

#     computer = random.randint(0,2)
#     if (player == 0 and computer == 2 ) or (player == 1 and computer == 0 ) or (player == 2 and computer == 1):
#         print('你胜利了')
#         print(computer)
#         continue
#     elif player == computer:
#         print('打平，重来')
#         print(computer)
#         continue
#     elif player == 3:
#         print('游戏结束')
#         break
#     else:
#         print('你输了')
#         print(computer)
#         continue
    
#=========================================

# print('='*50)
# print('名字管理系统')
# print('1.新增一个名字')
# print('2.删除一个名字')
# print('3.修改一个名字')
# print('4.查询一个名字')
# print('5.退出系统')
# print('='*50)

# names = []

# while True:
#     num = int(input('请输出序号:'))
#     if num == 1:
#         name = input('输入新增名字：')
#         names.append(name)
#         print(names)
#     elif num == 2:
#         name = input('输入删除名字：')
#         names.remove(name)
#         print(names)
#     elif num == 3:
#         name = input('输入修改名字：')
#         for index,temp in enumerate(names):
#             if temp == name:
#                 print('找到了此人')
#                 newname = input('输入一个修改后的名字')
#                 names[index] = newname
#             else:       
#                 print('查无此人')

#     elif num == 4:
#         name = input('请输入查询姓名：')
#         if name in names:
#             print('有此人%s'%name)
#         else:
#             print('未找到%s'%name)
#     elif num == 5:
#         break
#     else:
#         print('输入有误，请重新输入')


#=======================================

# print('='*50)
# print('名片管理系统')
# print('1.新增一个名字')
# print('2.删除一个名字')
# print('3.修改一个名字')
# print('4.查询一个名字')
# print('5.退出系统')
# print('='*50)

# infor_card = []

# while True:
#     num = int(input('输入一个序号：'))

#     if num == 1:
#         name = input('请输入名字')
#         age = input('请输入年龄')
#         addr = input('请输入地址')
#         new_infor = {'姓名':name,'年龄':age,'地址':addr}
#         print(new_infor)
#         infor_card.append(new_infor)
#         print(infor_card)
#     elif num == 2:
#         name = input('输入删除姓名')
#         for temp in infor_card:
#             if name == temp['姓名']:
#                 infor_card.remove(temp)
#                 print(infor_card)
#             else:
#                 print('未找到')
#     elif num == 3:
#         name = input('输入一个修改的名字')
#         for index,temp in enumerate(infor_card):
#             if name == temp['姓名']:
#                 print('找到了%s'%(name))
#                 name = input('输入一个新的名字')
#                 age = input('输入新年龄')
#                 addr = input('输入新地址')
#                 infor_card[index] = {'姓名':name,'年龄':age,'地址':addr}
#                 print(infor_card)
#     elif num == 4:
#         find_name = input('查询一个名字')
#         flag = 0
#         for temp in infor_card:
#             if find_name == temp['姓名']:
#                 print(temp)
#                 flag = 1
#                 break
#         if flag == 0:
#             print('无此人')
#     elif num == 5:
#         print('退出系统')
#         break
#     elif num == 6:
#         pass
#     else:
#         print('输入有误重新输入')

# def conut_nums(a,b):
#     count = a+b
#     print(count)
#     return count

# def chengfa_nums(a):
#     chengfa = a*5
#     print('乘后结果%d'%chengfa)

# a = int(input('输入一个A值'))
# b = int(input('输入一个B值'))

# conut_nums(a,b)

# result = conut_nums(a,b)

# chengfa_nums(result)


#子类继承父类

class Animal:
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    def __str__(self):
        return '%s是名字,%d是年龄'%(self.name,self.age)
    def eat(self):
        print('%s可以吃'%(self.name))
    def __sleep(self):
        print('可以睡觉')
    def get_sleep(self):
        self.__sleep()

class Dog(Animal):
    def __init__(self,new_name,new_color):
        self.name = new_name
        self.name = new_color
    def __str__(self):
        return '%s是名字'%(self.name)
    def dark(self):
        print('可以汪汪叫')

fish = Animal('Anny',8)
fish.eat()
dog = Dog('tim','red')
dog.eat()
dog.get_sleep()



