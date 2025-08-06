import time
import os
import sys
import smtplib
from email.message import EmailMessage
import hashlib
import schedule


def createlog():
    
    foldername="marvellous"      # logbook folder
    if not os.path.exists(foldername):
       os.mkdir(foldername)
    filename="marvellous.txt"   

    filename=os.path.join(foldername,filename)   
    
 
    
    fobj=open(filename,"a")

    border="-"*54
    
    fobj.write(border+"\n")
    fobj.write("this is log file of maervellous scripting \n")
    
    fobj.write(border+"\n")


    
    return filename

def calculatechecksum(path,blocksize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()

    buffer=fobj.read(blocksize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer=fobj.read(blocksize)
    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "demo"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
        
    

    
    duplicate={}  # blank dictionry

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):  
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=calculatechecksum(fname)

            if checksum in duplicate:
                duplicate[checksum].append(fname)    
            else:    
                duplicate[checksum]=[fname]
    deleteduplicate(duplicate) 


def deleteduplicate(MyDict):
    timestamp=time.ctime() 
    Result=list(filter(lambda x: len(x) > 1,MyDict.values()))
    
   
    filename=createlog()  
  
    fname=open(filename,"a")
    count=0
    for value in Result:
        for subvalue in value:
            count=count+1
            if count > 1 :
                fname.write("%s \n "%subvalue)  
                
                os.remove(subvalue)  
                 
        count=0  
    fname.write("\n \n while scanning now ,above files deleted at  "+timestamp)
    fname.write("\n \n ")
    sendmail(filename) 

def sendmail(filepath):  
    fobj=open(filepath,"rb")
    data=fobj.read()

    msg= EmailMessage()
    msg.add_attachment(data,maintype="file",subtype="log",filename=filepath)

    msg["Subject"] = "log file of duplicate files in Demo folder"
    msg["From"] = "# MAIL ADDRESS OF USER "
    msg["To"]="MAIL ADDRESS OF CLIENT"

    s= smtplib.SMTP("smtp.gmail.com",)
    s.starttls()
    s.login("MAIL ADDRESS OF USER ","16 CHARECTOR APP PASSWORD OF USER ACOUNT ") 
    s.send_message(msg)
    s.quit()


def main():
    
    dir=sys.argv[1]
    interval=sys.argv[2] 
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory timeinterval")
            print("Please provide valid absolute path")

    if(len(sys.argv) == 3):
            schedule.every(int(interval)).minutes.do(lambda : FindDuplicate(dir))

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)   
            
    
    
             
        

              
             
if __name__=="__main__":
    main()            