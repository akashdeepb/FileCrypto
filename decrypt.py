import os,sys,getpass
import pyAesCrypt
import dhelp
from shutil import copyfile
import validate
bufferSize=64*1024
export=""
dir_path = os.getcwd()+"/"
if len(sys.argv)==1:
    dhelp.main()
else:
    recFlag=0
    if sys.argv[1]=='-h' or sys.argv[1]=='--help':
        dhelp.optHelp()
        sys.exit(0)
    key=getpass.getpass("Enter Key : ")
    for i in range(1,len(sys.argv)):
        if sys.argv[i]=='-e' or sys.argv[i]=='--export':
            export=sys.argv[i+1]
            if os.path.isdir(export):
                overwrite=input(export+" already exists. Do you want to use the same directory?(y/n): ")
                if overwrite=='y' or overwrite=='yes':
                    print("Writing...")
                else:
                    print("Cancelled by user. Exiting... ;)")
                    sys.exit(0)
            else:
                print("\n Making a New Directory "+export)
                os.mkdir(export)
            dir_path = os.path.dirname(os.path.realpath(__file__))+"/"+export+"/"
        elif sys.argv[i]=='-r' or sys.argv[i]=='-R' or sys.argv[i]=='--recursive':
            recFlag=1
        elif os.path.isfile(sys.argv[i]):
            if export:
                if os.path.isfile(dir_path+sys.argv[i]):
                    overwrite=input(sys.argv[i]+" already exists. Do you want to Overwrite?(y/n): ")
                    if overwrite=='y' or overwrite=='yes':
                        try:
                            file = open(dir_path+sys.argv[i],'r+')
                            file.close()
                        except:
                            print('Error Creating '+sys.argv[i])
                            print(' Continuing ... ')
                            sys.exit(0)
                    else:
                        print("Continuing ... ")
                        continue

            print("\n-> Decrypting "+sys.argv[i]+" ...")
            pyAesCrypt.decryptFile(sys.argv[i],"fileCryptotemp~",key,bufferSize)
            copyfile("fileCryptotemp~",dir_path+sys.argv[i])
            print("\n\t ✔ "+sys.argv[i]+" Decrypted")
        else:
            print("\n✘ "+sys.argv[i]+" not found")
    if os.path.isfile("fileCryptotemp~"):
        os.remove("fileCryptotemp~")
