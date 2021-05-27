import os 
from Book import Book
class application: 
    def Run(self): 
     while True: 
            key = self.selectmenu()
            if  key == 1:
                self.add_book()
            elif key == 2:
                self.find_book()
            elif key == 3:
                self.search_book()    
            elif key == 4:
                self.correct_book()
            elif key == 5:
                self.remove_book()   
            elif key == 6:
                self.view_all()
            elif key == 7:
                print('프로그램 종료')
                break
            else:
                print("잘못 입력하셨습니다.")
            input("엔터 키를 누르세요.")
    
    def selectMenu(self): 
        os.system("cls") 
        print("== 도서 관리 프로그램 ==") 
        f = open("C:/books/input.txt", 'r')
        data = f.read()
        print(data)
        f.close()
        print("1:장르 추가") 
        print("2:도서 추가") 
        print("3:도서 삭제") 
        print("4:도서 검색") 
        print("5:도서 수정") 
        print("6:전체 보기")
        return input("\n메뉴 입력 ◀:") 
    
    def add_book(self):
        print("===도서 추가===")
        a = input('도서명, 저자, 출판연도, 출판사명, 장르: ')
        f = open("C:/books/input.txt", 'a')
        f.write('\n'+a)
        f.close()
        print("추가 완료")

    def find_book(self): 
        print("===도서 검색===") 
        print("1:제목") 
        print("2:저자") 
        print("3:출판연도")
        print("4:출판사")
        print("5:장르")  
        self.option=int(input("\n ◀:"))
        if self.option== 1:
            self.Findtitle()
        elif self.option== 2:
            self.Findauthor()
        elif self.option== 3:
            self.Findyear()
        elif self.option== 4:
            self.Findpublisher()
        elif self.option== 5:
            self.Findgenre()
        else:
            print("잘못 선택하였습니다.") 
        input("엔터 키를 누르세요.") 
    def Findtitle(self):
        title = input("도서명:")
        book =self.Find(title) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.ViewBook(book) 
    def Findauthor(self):
        author = input("저자:") 
        book =self.Find_author(author) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.ViewBook(book) 
    def Findyear(self):
        year = input("출판연도:") 
        book =self.Find_year(year) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.ViewBook(book) 
    def Findpublisher(self):
        publisher = input("출판사:") 
        book =self.Find_publisher(publisher) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.ViewBook(book)
    def correctbook():
        new_text = ''
        promble = input('문제 단어:')
        new_word = input('변경 단어:')
        with open('C:/books/input.txt', 'a') as file:
            lines = file.readlines() 
            for i, l in enumerate(lines):
                new_string = l.strip().replace(promble,new_word)
            if new_string:
                new_text += new_string + '\n'
            else:
                new_text += '\n'
    def removeBook(self):
        print("===도서 삭제===") 
        title = input("도서 제목:") 
        book =self.Find(title) 
        if book == None: 
            print("존재하지 않는 도서입니다.") 
            return 
        self.books.remove(book)
        del book
        print('삭제완료')
    
    def ViewAll(self): 
        print("===전체 보기===") 
        f = open('C:/books/input.txt', 'a')
        data = f.read()
        print(data)
        f.close()   
        self.ViewBooks() 