import os,sys,getpass
import pyAesCrypt
from shutil import copyfile
import enchelp as ehlp
import validate
bufferSize=64*1024
export=""
dir_path = os.getcwd()+"/"
if len(sys.argv)==1:
    ehlp.main()
else:
    recFlag=0
    keyStat=0
    if sys.argv[1]=='-h' or sys.argv[1]=='--help':
        ehlp.optHelp()
        sys.exit(0)
    while keyStat==0:
        key=getpass.getpass("Enter Key : ")
        cnfkey=getpass.getpass("Confirm Key : ")
        if key!=cnfkey:
            print("\n -- Keys Doesn't Match. Try Again -- ")
            keyStat=0
        else:
            keyStat=1
    for i in range(1,len(sys.argv)):
        if sys.argv[i]=='-e' or sys.argv[i]=='--export':
            export=sys.argv[i+1]
            if os.path.isdir(export):
                overwrite=input(export+" already exists. Do you want to Use the same directory?(y/n): ")
                if overwrite=='y' or overwrite=='yes':
                    print("Writing..." )
                else:
                    print("Cancelled by user. Exiting... ;)")
                    sys.exit()
            else:
                print("Making new Directory "+export)
                os.mkdir(export)
            dir_path = os.path.dirname(os.path.realpath(__file__))+"/"+export+"/"
        elif sys.argv[i]=='-r' or sys.argv[i]=='-R' or sys.argv[i]=='--recursion':
            recFlag=1
        elif os.path.isdir(sys.argv[i]) and export != sys.argv[i]:
            if recFlag==0:
                print(sys.argv[i]+" is a directory [use -r or --recursive]to encrypt all files it contains")
            else:
                print("\n Encryption all files in "+sys.argv[i])
        elif os.path.isfile(sys.argv[i]):
            if export:
                if os.path.isfile(dir_path+sys.argv[i]):
                    overwrite=input(sys.argv[i]+" already exists. Do you want to Overwrite?(y/n): ")
                    if overwrite=='y' or overwrite=='yes':
                        try:
                            file = open(dir_path+sys.argv[i],'a+')
                            file.close()
                        except:
                            print('Error Creating '+sys.argv[i])
                            print(' Continuing ... ')
                            sys.exit(0)
                    else:
                        print("Continuing ... ")
                        continue
            copyfile(dir_path+sys.argv[i],"fileCryptotemp~")
            print("\n-> Encrypting "+sys.argv[i])
            pyAesCrypt.encryptFile("fileCryptotemp~",dir_path+sys.argv[i],key,bufferSize)
            print("\n\t ✔ "+sys.argv[i]+" Encrypted")
        else:
            if export != sys.argv[i]:
                print("\n✘  "+ sys.argv[i]+" not found.")
    if os.path.isfile("fileCryptotemp~"):
        os.remove("fileCryptotemp~")
