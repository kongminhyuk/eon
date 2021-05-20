a = list(map(int,input("값을 입력하시오:").split()))
#입력된 값을 list로 만들어 저장 
def bubble_sort(arr): #bubble 함수 정의
    for i in range(0,len(arr)-1,1): # 이중for문 사용 / (리스트의 크기-1)부터 1씩 증가하며 반복
        for j in range(0,len(arr)-1,1): #(리스트의 크기-1)부터 1씩 증가하며 반복
            if arr[j]>arr[j+1]: # j가 j+1 보다 크면 위치를 바꿈
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble_sort(a)) #bubble_sort에 a를 대입하여 출력