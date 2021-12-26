size = input().split()
# i - row, j - col
init_arr = []
black_arr = []
white_arr = []
white_val = []
black_val = []
arr = []
for i in range(int(size[0])):
    init_arr.append(input().split())
    
# 흰, 검은 체스판 initialize
for j in range(8):
    if j % 2 == 1:
        black_arr.append('WBWBWBWB')
        white_arr.append('BWBWBWBW')
    else:
        white_arr.append('WBWBWBWB')
        black_arr.append('BWBWBWBW')

# 주어진 입력 체스판
for m in range(int(size[0])):
    arr.append(init_arr[m][0])

# 8x8 흰 체스판, 검은 체스판을 마련하고
# 주어진 입력과 하나씩 대조해서 
# 차이가 제일 적은 경우를 출력
for i in range(int(size[0]) - 7):
    for j in range(int(size[1]) - 7):
        white = 0
        black = 0
        for l in range(0, 8):
            for k in range(0, 8):
                if k % 2 == 0:
                    if arr[i+l][j+k] == white_arr[l][k]:
                        black += 1
                    else:
                        white += 1
                else:
                    if arr[i+l][j+k] == white_arr[l][k]:
                        black += 1
                    else:
                        white += 1
        white_val.append(white)
        black_val.append(black)
w = min(white_val)
b = min(black_val)
print(min(w, b))


