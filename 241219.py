# class Zergling:
#     def __init__(self):
#         self.hp=20
#         self.mana=50

#     def run(self):
#         print("뛴다")
#         self.hp-=1
#         self.mana+=1

#     def show_stats(self):
#         print(f'HP : {self.hp}')
#         print(f'MANA : {self.mana}')

# z1=Zergling()
# z2=Zergling()

# z1.run()
# z1.show_stats()

# for i in range(5):
#     z2.run()
# z2.show_stats()

# class GameMachine():
#     def __init__(self):
#         self.coin=0

#     def input_coin(self, coinNum):
#         if (coinNum > 5):
#             print("최대 5개까지만 넣을 수 있습니다!")
#             return
#         if (self.coin+coinNum > 10):
#             print("입력된 코인은 10보다 초과될 수 없습니다!")
#             return
#         self.coin+=coinNum
    
#     def play_game(self):
#         if(self.coin <= 0):
#             print("코인이 부족하므로 게임을 플레이할 수 없습니다!")
#             return
#         self.coin -= 1
#         print("게임 재밌다")

#     def show_status(self):
#         print(f'남아있는 코인은 {self.coin} 입니다')

# gm=GameMachine()
# gm.input_coin(2)
# gm.show_status()
# gm.play_game()
# gm.show_status()

# class Tire():
#     def __init__(self):
#         pass
#     def run(self):
#         print("런")

# class Tire1(Tire):
#     def ran(self):
#         print("랜")

# class Tire2(Tire):
#     def run(self):
#         print("런런")

#     def ron(self):
#         print("론")

# t=Tire()
# t1=Tire1()
# t2=Tire2()

# t.run()
# t2.run()

import numpy as np
lst=[1,2,3,4,5]
result_lst=lst*2
print(result_lst)

numpy_arr=np.array([1,2,3,4,5])
result_arr=numpy_arr*2
print(result_arr)