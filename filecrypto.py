import sys,os
import validate
import subprocess
if len(sys.argv)==1:
    import fileCryptHelp
else:
    if sys.argv[1]=='--remove' or sys.argv[1]=='-r' or sys.argv[1]=='remove' or sys.argv[1]=='rm' or sys.argv[1]=='uninstall':
        print("\n Removing FileCrypto may result in loss of encrypted file. It is advised to decrypt all the encrypted files before removing FileCrypto as you may lose all the data saved in files encrypted with FileCrypto.")
        cnfRm=input("\n Do you want to remove FileCrypto?(y/n) : ")
        if cnfRm=='yes' or cnfRm=='y':
            subprocess.call(['./remove.sh'])
        else:
            print("\n Cancelled by User ... ;)")
            exit(0)
    