class Book:
    def __init__(self,title,author,publisher,year,genre):
        self.title = title 
        self.author = author 
        self.publisher = publisher 
        self.year = year 
        self.genre = genre
    def Write(self,fs):
        fs.write(self.title+",")
        fs.write(self.author+",")
        fs.write(self.publisher+",")
        fs.write(self.year+",")
        fs.write(self.genre+",")
    @staticmethod 
    def LoadBook(fs): 
        data = fs.readline() 
        elems = data.split(",") 
        if len(elems)<6: 
            return None 
        title = elems[0] 
        author = elems[1] 
        publisher = (elems[2]) 
        year = elems[3] 
        genre = (elems[4])
        return Book(year,title,author,publisher,genre)