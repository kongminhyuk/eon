a = list(map(int,input("합 할 숫자를 입력하시오: ").split()))
#입력받은 수를 리스트 a에 저장

def sumlist(a): #sumlist 함수 선언
    result = 0 #result 의 초기값 설정
    for n in a: #for 반복문 사용
        result = result + n
    return result #반복문이 끝난 후 결과 값 반환
    
    print("합은 %d입니다." %sumlist(a)) #결과 값 출력