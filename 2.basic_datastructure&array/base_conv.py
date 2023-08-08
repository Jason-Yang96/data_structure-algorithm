# 10진수를 n진수로 전환한다. 
# 의외로 간단하다. 특정 숫자를 n진수의 n으로 계속 나눠준 뒤에 그 나머지를 역순으로 나열해주면 된다. 

def base_conversion(x: int, r: int) -> str:
    d = ""
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while x > 0:
        d += dchar[x%r]
        x //= r

    return d[::-1]

if __name__ == "__main__":
    while True:
        while True:
            no = int(input("변환할 값을 음이 아닌 수로 입력: "))
            if no > 0:
                break
        while True: 
            cd = int(input("어떤 진수로 변환(2부터 36까지 숫자 기입): "))
            if 2 <= cd <= 36:
                break
        print(f"{no}를 {cd}진수로 변환한 수는 {base_conversion(no, cd)}")

        retry = input("one more? (Y/N)")
        if retry in {"n", "N"}:  # {}은 집합이다. 순서와 중복이 없다. 
            break