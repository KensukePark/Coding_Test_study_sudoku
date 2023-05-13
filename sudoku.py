#가로줄 확인
def rule_1(x,num):
    for i in range(0,9):
        if sudo[x][i] == num:
            return False
    return True

#세로줄 확인
def rule_2(y, num):
    for i in range(0,9):
        if sudo[i][y] == num:
            return False
    return True

#3*3 박스 확인
def rule_3(x,y, num):
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudo[start_x+i][start_y+j] == num:
                return False
    return True

def solve(index):
    if len(loc) == index:
        for i in range(0, 9):
            if sudo[i].count(0) != 0:
                return 0
    
        for i in range(0, 9):
            for j in range(0, 9):
                print(sudo[i][j], end=' ')
            print()
        return 0

    for i in range(1, 10):
        if rule_1(loc[index][0], i) and rule_2(loc[index][1], i) and rule_3(loc[index][0], loc[index][1], i):
            sudo[loc[index][0]][loc[index][1]] = i
            solve(index+1)
            sudo[loc[index][0]][loc[index][1]] = 0

#스도쿠 불러오기
            
sudo = []
for i in range(0,9):
    temp = input()
    temp_split = temp.split(' ')
    int_temp = list(map(int,temp_split[:9]))
    sudo.append(int_temp)

#풀어야 할 칸 좌표 저장
loc = []
for i in range(0,9):
    for j in range(0,9):
        if sudo[i][j] == 0:
            loc.append((i,j))

solve(0)
