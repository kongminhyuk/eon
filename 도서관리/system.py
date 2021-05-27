def addbook():
    print("===도서 추가===")
def addbook():
    a = input('제목 저자 출판연도 출판사명 장르: ')
    with open("C:/books/input.txt","a") as file:
     file.write('\n'+ a)
     print('추가완료')

def searchbook():
    print("===도서 검색===")
    print("1.도서 검색")
    print("2.개별 검색")
    a=int(input("\n ◀: "))
    if a==1:
        b = input("책 정보 : ")
        with open("C:/books/input.txt","r") as file:
            line = file.readlines()
        for l in line:
            if b in l:
                print(l, end = "")
    elif a==2:
        print("0:제목") 
        print("1:저자") 
        print("2:출판연도")
        print("3:출판사")
        print("4:장르")  
        c=int(input("\n ◀:"))
        with open("C:/books/input.txt","r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                list = line.split(" ")
                if c == 1:
                    print(list[0])
                elif c == 2:
                    print(list[1])
                elif c == 3:
                    print(list[2])
                elif c == 4:
                    print(list[3])
                elif c == 5:
                    print(list[4])
                else:
                    print("잘못 입력하셨습니다.")
    else:
        print("잘못 입력하셨습니다.")

def correctbook():
    print("===도서 수정===")
    viewall()
    new_text = ''
    problem = input('수정하려는 부분을 입력하세요:')
    new = input('변경하려는 단어를 입력하세요:')
    with open('C:/books/input.txt','r') as file:
        lines = file.readlines() 
        for i, l in enumerate(lines):
            new_string = l.strip().replace(problem,new)
            if new_string:
                new_text += new_string + '\n'
            else:
                new_text += '\n'

    with open("C:/books/input.txt","w") as file:
        file.write(new_text)
    print('변경 완료')

def removebook():
    print("===도서 삭제===")
    title = input("삭제할 도서의 제목:")
    with open("C:/books/input.txt", 'r') as f:
        data = f.readlines()
    with open("C:/books/input.txt", 'w') as of:
        for i in data:
            if not i.startswith(title):
                of.write(i)
    print("삭제 완료")

def viewall():  
    print("===전체 보기===") 
    f = open('C:/books/input.txt', 'r')
    data = f.read()
    print(data)
    f.close()