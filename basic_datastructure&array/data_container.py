 # mutable
l = list("abc")
print(l)

l2 = [None] * 5 
print(l2)


# immutable
t = 1,2,3
t2 = "a", "b", "c"
t3 = (1)
t4 = 1, # 원소가 하나인 경우는 ,를 붙여야 한다. 
print(f"{t} & {t2} & {t3} & {t4}") 

# 숫자나 문자 자체가 객체가 된다. 따라서 a가 32를 참조하고 있다 54를 참조하는 것으로 바뀐 것. b가 54를 참조하고 있다가 32를 참조하는 것으로 바뀐 것이다.   
a = 32
b = 54
print(id(a))
print(id(b))
a = 54
b = 32
print(id(a))
print(id(b))