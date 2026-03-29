import os
import re
import shutil
class Menedzer:
    def __init__(self):
        self.a = 0
    def utworzplik(self,fileName):
        print("zapis")
        try:
            fp = open(fileName,'x')
            fp.close()
        except:
            print("Plik istnieje albo napotkano inny błąd")
        self.menu()
    def usunplik(self,filename):
        if os.path.exists(filename):
            os.remove(filename)
            print("Usunięto plik: " + filename)
        else:
            print("Plik nie istnieje")
        self.menu()
    def kopiujplik(self,startFile,endFile):
        try:
            shutil.copy(startFile,endFile)
            print("Skopiowano plik z " + startFile + " do " + endFile)
        except:
            print("Nie udało się skopiować")
        self.menu()
    def zmiennazwe(self,startpath,endpath):
        try:
            os.rename(startpath,endpath)
            print("Zmieniono nazwę pliku z " + startpath + " na " + endpath)
        except:
            print("Nie można zmienić nazwy pliku")
        self.menu()
    def przeniesplik(self):
        print("przenieś")
    def usunfolder(self,path):
        try:
            shutil.rmtree(path)
            print("usnięto: " + path)
        except:
            print("Nie ma takiego katalogu!")
        self.menu()
    def stworzkatalog(self,dirName):
        os.makedirs(dirName)
        print("Utworzono foldery:" + dirName)
        self.menu()
    def kopiujkatalog(self,startPath,endPath):
        try:
            shutil.copytree(startPath, endPath)
            print("Skopiowano folder z " + startPath + " do " + endPath)
        except:
            print("Coś poszło nie tak!")
        self.menu()
    def zmiensciezke(self,path):
        try:
            os.chdir(path)
        except:
            print("Nie istnieje taka ścieżka!")
        self.menu()
    def przenies(self,startFile, endFile):
        try:
            shutil.move(startFile,endFile)
        except:
            print("Nie istnieje jakiś folder!")
        self.menu()
    def menu(self):
        print("Komendy:")
        print("Utworzenie pliku : mkfile")
        print("Usunięcie pliku : rmfile")
        print("Skopiowanie pliku : cpfile")
        print("Zmień nazwę pliku lub katalogu : chgname")
        print("Przenieś plik z jednego do drugiego miejsca : mv")
        print("Zmiana ścieżki : cd")
        print("Aktualna ścieżka : pwd")
        print("Listowanie plików i folderów : ls")
        print("Utworzenie folderu : mkdir")
        print("Usunięcie folderu i jego zawartości : rmdir")
        print("Skopiowanie folderu z zawartością : cpdir")
        print("Aktualna ścieżka: " + os.getcwd())
        inp = input("Proszę podać, co chcesz zrobić: ")
        if re.search("^mkfile*",inp):
            filename = input("Proszę podać nazwę pliku: ")
            self.utworzplik(filename)
        elif re.search("^rmfile*",inp):
            filename = input("Proszę podać nazwę pliku: ")
            self.usunplik(filename)
        elif re.search("^cpfile*", inp):
            startpath = input("Proszę podać nazwę folderu skąd skopiować plik: ")
            endpath = input("Proszę podać nazwę folderu dokąd skopiować plik: ")
            self.kopiujplik(startpath,endpath)
        elif re.search("^chgname*", inp):
            startpath = input("Proszę podać nazwę pliku/katalogu: ")
            endpath = input("Proszę podać docelową nazwę pliku/katalogu: ")
            if os.path.exists(endpath):
                print("Taki plik istnieje!")
            elif os.path.exists(startpath) == False:
                print("Nie istnieje taki plik!")
            else:
                self.zmiennazwe(startpath,endpath)
        elif re.search("^move*", inp):
            startpath = input("Proszę podać nazwę pliku/katalogu: ")
            endpath = input("Proszę podać docelową nazwę pliku/katalogu: ")
            self.przenies(startpath, endpath)
        elif re.search("^cd*",inp):
            newPath = input("Proszę podać nazwę nowej ścieżki, do której chcesz się dostać: ")
            self.zmiensciezke(newPath)
        elif inp == "pwd":
            print("Aktualna ścieżka: " + os.getcwd())
            self.menu()
        elif inp == "ls":
            for dir in os.listdir():
                if os.path.isfile(dir):
                    print(dir)
                else:
                    print(dir + "/")
            self.menu()
        elif re.search("^mkdir*",inp):
            dirName = input("Proszę podać nazwę folderu: ")
            self.stworzkatalog(dirName)
        elif re.search("^rmdir*",inp):
            dirName = input("Proszę podać nazwę folderu: ")
            self.usunfolder(dirName)
        elif re.search("^cpdir*",inp):
            startpath = input("Proszę podać nazwę folderu skąd skopiować plik: ")
            endpath = input("Proszę podać nazwę folderu dokąd skopiować plik: ")
            self.kopiujkatalog(startpath, endpath)
        elif re.search("^mvFile*",inp):
            self.przeniesplik()
        elif re.search("^chName*",inp):
            self.changeFileName()
        else:
            print("Nie istnieje takie polecenie!")


start = Menedzer()
start.menu()