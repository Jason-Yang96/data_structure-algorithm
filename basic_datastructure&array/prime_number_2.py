counter = 0 # 전체 연산 횟수
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500

prime[ptr] = 2
ptr += 1 

for n in range(3, 1001, 2): # 짝수는 계산할 필요가 없으므로(어차피 2를 제외하고 소수가 아님)
    for i in range(0, ptr):
        counter  += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n # 자식 for 문을 다 돌고 나면(break으로 탈출하지 않으면) 새로운 소수를 추가해준다.
        ptr += 1 

for i in range(ptr):
    print(prime[i])
print(f"# of counting: {counter}")

