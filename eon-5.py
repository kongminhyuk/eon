a = list(map(int,input("array를 입력해주세요: ").split())) #입력하는 수를 받아 배열로 저장(array)
b = list(map(int,input("i, j, k: ").split())) #i,j,k를 입력받아 배열로 저장(commands)

def ARRAY(x): #array 함수 선언
    x = x[b[0]-1:b[1]] # 0번째 부터 존재하므로 -1
    x.sort() # X를 정렬
    return x[b[2]-1] #b[K-1]로 return
print(ARRAY(a)) #array(x)에 인수 a를 넣고 출력