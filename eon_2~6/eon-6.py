n = int(input("피자 조각의 수 : "))  #피자 조각의 수 입력

def fibonacci(n): # 재귀를 이용해 피보나치 수열을 구현
    if n <= 2: 
        return 1 # n이 1,2 일 경우
    else: 
        return fibonacci(n-1) + fibonacci(n-2) # n이 3이상일 경우
        
print("경우의 수 : %d" % fibonacci(n+1)) # fibonacci(n+1) 출력