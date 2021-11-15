# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_dictionary_step1
# 辞書への追加、key検索
n = int(input())
dic = {}
for i in range(n):
    s,a = input().split()
    dic[s] = a

print(dic[input()])

# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_dictionary_step2
# 辞書のデータ更新
n = int(input())
player_damege = {}

for i in range(n):
    player = input()
    player_damege[player] = 0

m = int(input())

for i in range(m):
    p,d = input().split()
    player_damege[p] += int(d)

print(player_damege[input()])

# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_dictionary_step3
# 辞書ソート(keyでソート)
n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())
for i in range(m):
    p,d = input().split()
    dmg[p] += int(d)

name_list = sorted(dmg.keys())

for p in name_list:
    print(dmg[p])