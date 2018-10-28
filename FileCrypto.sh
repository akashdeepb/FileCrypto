echo -e "\n\t\t --  Welcome to FileCrypto  --\n"
echo "An Open Source Files Security Project"
echo -e "\033[1;36m github : https://github.com/akashdeep/FileCrypto \033[1;m"
enc=$(pwd)"/encrypt.py"
dec=$(pwd)"/decrypt.py"
fc=$(pwd)"/filecrypto.py"
chmod +x remove.sh
grep "alias filecrypto=" ~/.bashrc > /dev/null
if [ $? -eq 1 ];then
	echo -n "alias filecrypto='sudo python3 ">>~/.bashrc && echo -n $fc >>~/.bashrc && echo "'">>~/.bashrc
else
	echo -e "\n filecrypto alias already exists "
fi
grep "alias encrypt=" ~/.bashrc > /dev/null
if [ $? -eq 1 ]; then
	echo -n "alias encrypt='sudo python3 ">>~/.bashrc && echo -n $enc >> ~/.bashrc && echo "'">>~/.bashrc
else
	echo -e "\n encrypt alias already exists "
fi
grep "alias decrypt=" ~/.bashrc > /dev/null
if [ $? -eq 1 ];then
	echo -n "alias decrypt='sudo python3 ">> ~/.bashrc && echo -n $dec>> ~/.bashrc && echo "'">>~/.bashrc
else
	echo -e "\n decrypt alias alread exists "
fi
echo -e "\n\n\t\t -- Installing Requirements --"
pip3 install pyAesCrypt
echo -e "\n Installation Complete ... ;) \n"
