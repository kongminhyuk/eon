import os
from book import book

class system:

def Run(self):
while True: 
    key = self.SelectMenu() 
    if key =='1':
        self.addbook()
    elif key =='2':
        self.findbook()
    elif key =='3':
        self.modifybook()   
    elif key =='4':
        self.removebook()
    elif key =='5':
        self.ViewAll()
    elif key =='6': 
        print("프로그램 종료")
        break
    else:
        print("다시 선택해 주세요..")
    input("엔터키를 눌러주세요..")

def SelectMenu(): #메뉴
    os.system('cls') print("=== 도서 관리 프로그램 ===") 
    print("1:도서 추가") 
    print("2:도서 검색") 
    print("3:도서 수정")
    print("4:도서 삭제") 
    print("5:전체 보기")
    return input("\n메뉴 입력 ◀:")

def addbook():    #도서 추가
    print("=== 도서추가 ===")
    addbook = input("도서명, 저자, 출판연도, 출판사명, 장르: ")
    with open('C:/books/input.txt','newbook') as file:
        file.write('\n'+ newbook)
        print("추가 완료.")

def findbook():   #도서 검색
    print("=== 도서검색 ===")
    import re, glob
    key = input("검색할 단어를 입력하시오: ")
    p = re.compile(key)
    for i in glob.glob(r'C:/books/input.txt'):
        with open(i, 'r') as file:
            for x, y in enumerate(f.readlines(),1):
               m = p.findall(y)
               if m:
                   print("관련 도서 : %s" %y)
           print()
def modifybook():  #도서 수정
    print("=== 도서수정 ===")
    viewall()
    new_text = ''
    promble_word = input("수정하고자 하는 부분:")
    modify_word = input("수정하고자 하는 내용:")
    
    with open('C:/books/input.txt','r') as file:
        lines = file.readlines() 
        for i, l in enumerate(lines):
            new_string = l.strip().replace(promble_word,modify_word)
            if new_string:
                new_text += new_string + '\n'
            else:
                new_text += '\n'
    with open('C:/books/input.txt','w') as file:
        file.write(new_text)
    print("수정 완료")

def removebook():   #도서 삭제
    print("=== 도서삭제 ===")
    with open('C:/books/input.txt', 'r') as infile:
        lines = infile.readlines()
    viewall()
    remove_num = int(input("삭제하고 싶은 번호를 입력하세요: "))
    with open('C:/books/input.txt', 'w') as outfile:
        for i, line in enumerate(lines):
            if i != remove_num-1:
                outfile.write(line)
    print("삭제 완료")

def viewall():    #전체 보기
    print("=== 전체보기 ===")
    wiht open('C:/books/input.txt', 'r') as f
    all = f.read()
    print(all)