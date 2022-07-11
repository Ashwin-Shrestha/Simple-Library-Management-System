#The os module in Python provides functions for creating and removing a directory
import os
class Library:
    """Library class is made for managing a library. It has total 5 modules "getDate","getTime","Return Book","Borrow Book","BookCode Display" and a main function"""
    #Constructor is called and the data in stock file is kept inside a dictionary along with book ID as keys 
    def __init__(self,textfile):
        self.textfile="library.txt"
        self.libr_dict={}
        ID=1
        file=open("library.txt","r")
        text=file.readlines()
        for line in text:
            x=line.split(",")
            self.libr_dict.update({str(ID):{"Title": x[0], "Author" : x[1],"Quantity" : x[2],"Price" : x[3]}})
            ID=ID+1

###Function to retrieve date and time
    def getDate(self):
        import datetime
        dates=datetime.datetime.now
        return str(dates().date())

    def getTime(self):
        import datetime
        self.dates=datetime.datetime.now
        return str(self.dates().time())
    
###Function to display Book Code of the particular Books
    def discode(self):
       print("------------------Book Codes---------------------------")
       print ("BookCode","\t","Title")
       for keys,value in self.libr_dict.items():
           print(keys,"\t\t",value.get("Title"))

#Function to Borrow Books
    def borrow(self):
        Bcode=input("Enter the code of the book you want to borrow: ")
        if Bcode in self.libr_dict.keys():
            if (int(self.libr_dict[Bcode]["Quantity"] ) > 0):
                fname= str(input("Enter Your Full Name: "))
                book=self.libr_dict[Bcode]["Title"]
                bookname.append(book)
                issuedate=L.getDate()
                issuetime=L.getTime()
                price=int(self.libr_dict[Bcode]["Price"])
                total.append(price)
                tot=0
                for each in range(0,len(total)):
                    tot=tot+total[each]

#The stock file is updated according to the borrowing of book
                up=open("library.txt","r")
                upw=open("temp.txt","w")
                quant=int(self.libr_dict[Bcode]["Quantity"])
                s=" "
                while(s):
                    s=up.readline()
                    spl=s.split(",")
                    if len(s)>0:
                        if (spl[0]== str(self.libr_dict[Bcode]["Title"] )):
                            bname=self.libr_dict[Bcode]["Title"]
                            bauthor=self.libr_dict[Bcode]["Author"]
                            bquant=quant-1
                            bprice=self.libr_dict[Bcode]["Price"]
                            upw.write(bname+","+bauthor+","+str(bquant)+","+bprice)
                        else:
                            upw.write(s)
                up.close()
                upw.close()
                os.remove("library.txt")
                os.rename("temp.txt","library.txt")
#A Borrow Note is provided after borrowing the books
                
                fh=open("BorrowNote.txt","w")
                fh.write("---------------------------Book Borrow Notice----------------------------------------------\n")
                fh.write("\n")
                fh.write("Name of the person :" +str( fname)+"\n")
                fh.write("Date Issued:" +str(issuedate)+"\n")
                fh.write("Time of issue:" +str(issuetime)+"\n")
                fh.write("Total price: "+str(tot)+"$"+"\n")
                fh.write("Books Borrowed: \n")
                for i in range (len(bookname)):
                    fh.write(str(bookname[i])+"\n")
                fh.close()
                ask=input ("Do you wish to borrow more books(y/n): ")
                asking=ask.upper()
                if (asking=="Y"):
                    print("Thank you for borrowing the book "+book)
                    return self.borrow()
                elif(asking=="N"):
                    print("Thank you for borrowing the book "+book)
                else:
                    print("Error in choosing the value.Please choose carefully")
            else:
                print("The book is out of stock")
        else:
            print("The code you entered is wrong.Please try again")
            return self.borrow()

#Function to return the borrowed books
    def _return(self):
        Rcode=input("Please enter the code of the book you want to return:")
        days=int(input("Enter the number of days you have borrowed the books for:"))
        if Rcode in self.libr_dict.keys():
            fname= str(input("Enter Your Full Name: "))
            book=self.libr_dict[Rcode]["Title"]
            rbookname.append(book)
            returndate=L.getDate()
            returntime=L.getTime()
            price=int(self.libr_dict[Rcode]["Price"])
            rprice.append(price)
            rtot=0
            for each in range(0,len(rprice)):
                rtot=rtot+rprice[each]
            fineday=0
            if (days>10):
                print("You are late in returning the book so a fine is added to the total but the book " + book+ " has been returned. Thank you")
                fineday=days-10
                fineprice=(1/50)*rtot*fineday
            elif (days<=10):
                print("Thank you for returning the book " + book +" on time.Hope you have a wonderful day!!")
                fineprice=0
            else:
                print("The input you have entered is wrong.")
                return self._return()

            grand=rtot+fineprice
#Return Note is given after returning of book is successfull
            fh=open("ReturnNote.txt","w")
            fh.write("---------------------------Book Return Notice----------------------------------------------\n")
            fh.write("\n")
            fh.write("Name of the person :" +str( fname)+"\n")
            fh.write("Date Issued:" +str(returndate)+"\n")
            fh.write("Time of issue:" +str(returntime)+"\n")
            fh.write("Fine:"+str(fineprice)+"$"+"\n")
            fh.write("Total price: "+str(grand)+"$"+"\n")
            fh.write("Books Returned: \n")
            for i in range (len(rbookname)):
                fh.write(str(rbookname[i])+"\n")
            fh.close()
#Stock File is updated
            ret=open("library.txt","r")
            retw=open("temp.txt","w")
            quant=int(self.libr_dict[Rcode]["Quantity"])
            s=" "
            while(s):
                s=ret.readline()
                retspl=s.split(",")
                if len(s)>0:
                    if (retspl[0]== str(self.libr_dict[Rcode]["Title"] )):
                        retname=self.libr_dict[Rcode]["Title"]
                        retauthor=self.libr_dict[Rcode]["Author"]
                        retquant=quant+1
                        retprice=self.libr_dict[Rcode]["Price"]
                        retw.write(retname+","+retauthor+","+str(retquant)+","+retprice)
                    else:
                        retw.write(s)
            ret.close()
            retw.close()
            os.remove("library.txt")
            os.rename("temp.txt","library.txt")
        
            ask=input ("Do you wish to return more books(y/n): ")
            asking=ask.upper()
            if (asking=="Y"):
                return self._return()
            elif(asking=="N"):
                print("Thank you for returning the book")
            else:
                print("Error in choosing the value.Please choose carefully")
        else:
            print("The code you entered is wrong.Please try again")
            return self._return()

#The main function has the UI of the Program with which the user interacts.      
    def main():
        while(True):
            print("---------------------------|Welcome to Library Management System|---------------------------")
            print("------------------------------------------------------------------------------------------------------------")
            print("Press d to display available books")
            print("Press b to borrow books")
            print("Press r to return borrowed books")
            print("Press q to quit the system")
            try:
                s=input("Please select a choice: ")
                print()
                x=s.upper()
                if (x=="D"):
                    with open("library.txt","r") as dis:
                        line=dis.read()
                        print("The Available Books(Book Title, Author,Quantity,Price) are:")
                        print()
                        print(line)
                elif(x=="B"):
                    L.discode()
                    L.borrow()
                elif (x=="R"):
                    L.discode()
                    L._return()
                elif(x=="Q"):
                     print("Thank you for using the Library Management System.We hope seeing you again.")
                     break
                else:
                    print("Enter the valid choice as shown above.")
            except ValueError:
                print("Please give the correct input.")
#Calling Constructor
L=Library("library.txt")

#Global variables are defined
bookname=[]
total=[]
rprice=[]
rbookname=[]

#Main function is called 
Library.main()

    

            
