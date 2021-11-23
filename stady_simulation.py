# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_simulation_step1
# while loop
n = 10000
w = 13

while n % w != 0:
    n = n+1

print(n)

# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_simulation_step2
# while loop
n = int(input())
[a,b] = [int(n) for n in input().split()]
c = 0
p = 1
k = 1
while True:
    k += p * a
    c += 1
    if k > n:
        break
    p += k % b

print(c)

# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_simulation_boss
# while loop,list
p_HP = int(input())
p_HP_list = []
e_HP_list = []
c = 0
while True:
    c += 1
    if c <= 2:
        e_HP_list.append(1)
        p_HP_list.append(1)
    else:
        e_HP_list.append(p_HP_list[c-2] + p_HP_list[c-3])
        p_HP_list.append(e_HP_list[c-2] * 2 + e_HP_list[c-3])
    if p_HP <= sum(p_HP_list):
        break;

print(c)