import system
import os
class book:  #클래스 book 정의
    def addbook(self):
        system.addbook()
    def findbook(self):
        system.findbook()
    def modifybook(self):
        system.modifybook()    
    def removebook(self):
        system.removebook()
    def viewall(self):
        system.viewall()
    def SelectMenu(self):
        os.system('cls') 
        print("=== 도서 관리 프로그램 ===") 
        print("1:도서 추가") 
        print("2:도서 검색") 
        print("3:도서 수정")
        print("4:도서 삭제") 
        print("5:전체 보기")
        print("6:프로그램 종료")
        print("==========================")
        return self.new_method()

    def new_method(self):
        return input("\n메뉴 입력:")
    def run(self):
        while True:
            key = self.SelectMenu()
            if key == '1':
                self.addbook()
            elif key == '2':
                self.findbook()
            elif key == '3':
                self.modifybook()
            elif key == '4':
                self.removebook()   
            elif key == '5':
                self.viewall()
            elif key == '6':
                print('프로그램을 종료합니다.')
                break
            else:
                print("잘못 입력하셨습니다.")
            input("엔터 키를 누르세요.")