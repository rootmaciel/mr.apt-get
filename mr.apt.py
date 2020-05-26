#usr/bin/python3

import os

print()
os.system("cat /etc/*-release")
os.system("uname -a")

print('''\033[36m
_______________________________________________________
[]Versao 1.0-------Mr.Apt-Get_Install-------PenTester[]
[]                                                   []
[]------------------Debian - Hacking-----------------[]
[]___________________________________________________[]\033[0;0m''')
print('''\033[35m
#Linux, #Debian, #hacking,
Script para debian via apt-get install
Escolha as ferramentas a serem instaladas de acordo com as numerações:\033[0;0m''')

print('''\033[32m
	|1: make install    |6: vim            |11: ettercap
	|2: git clone       |7: python idle    |12: sslstrip
	|3: figlet          |8: qbitorrent     |13: dsniff  
	|4: codec vlc       |9: nmap           |14: drifnet 
	|5: cmatrix         |10: wireshark     |15: hascat  

	|16: aircrack-ng    |21: siege         |26: mitmf
	|17: reaver         |22: fcrackzip     |27: wget
	|18: crunch         |23: slowhttptest  |28: metasploit
	|19: Perl           |24: net-tools     |29: setoolkit
	|20: netcat         |25: bettercap     |30: kazam

	|31: OpenShot       |36: Code Blocks
	|32: ffmpeg & adb
	|33: sqlmap
	|34: fluxion
	|35: Proxy Jondonym
\033[0;0m''')

num = input("\033[37mEscolha um numero (0/Exit): \033[0;0m")

while num != 0:

	if num == '0':
    		os.system(exit())
	
	if num == '1':
    		print("\n[OK]Instalando make install...")
    		os.system("apt-get -y install make")

	if num == '2':
			print("\n[OK]Instalando git clone...")
			os.system("apt-get -y install git")
			print("\n[OK]Concluido...")

	if num =='3':
			print("\n[OK]Instalando figlet...")
			os.system("apt-get -y install figlet")
			print("\n[OK]Concluido...")

	if num =='4':
			print("\n[OK]Instalando reprodutor de video vlc...")
			os.system("apt-get -y install vlc")
			print("\n[OK]Concluido...")

	if num =='5':
			print("\n[OK]Instalando Terminal Matrix...")
			os.system("apt-get -y install cmatrix")
			print("\n[OK]Concluido...")

	if num =='6':
			print("\n[OK]Instalando editor de texto vim...")
			os.system("apt-get -y install vim")
			print("\n[OK]Concluido...")

	if num =='7':
			print("\n[OK]Instalando interface grafica do pyton idle...")
			os.system("apt-get -y install idle3")
			os.system("apt-get -y install python-pip")
			print("\n[OK]Concluido...")

	if num =='8':
			print("\n[OK]Instalando o gerenciador de downloads qbitorrent...")
			os.system("apt-get -y install qbittorrent")
			print("\n[OK]Concluido...")

	if num =='9':
			print("\n[OK]Instalando nmap")
			os.system("apt-get -y install nmap")
			print("\n[OK]Concluido...")

	if num =='10':
			print("\n[OK]Instalando wireshark")
			os.system("apt-get -y install wireshark")
			print("\n[OK]Concluido...")

	if num =='11':
			print("\n[OK]Instalando ettercap-modo-texto")
			os.system("apt-get -y install ettercap-graphical")
			print("\n[OK]Concluido...")

	if num =='12':
			print("\n[OK]Instalando sslstrip")
			os.system("apt-get -y install sslstrip")
			print("\n[OK]Concluido...")

	if num =='13':
			print("\n[OK]Instalando dsniff")
			os.system("apt-get -y install dsniff")
			print("\n[OK]Concluido...")

	if num =='14':
			print("\n[OK]Instalando driftnet")
			os.system("apt-get -y install driftnet")
			print("\n[OK]Concluido...")

	if num =='15':
			print("\n[OK]Instalando libclc-dev...")
			os.system("apt-get -y install libclc-dev")

			print("\n[OK]Instalando libclc-r600...")
			os.system("apt-get -y install libclc-r600")

			print("\n[OK]Instalando mesa-opencl-icd...")
			os.system("apt-get -y install mesa-opencl-icd")

			print("\n[OK]Instalando ocl-icd-libopencl1...")
			os.system("apt-get -y install ocl-icd-libopencl1")

			print("\n[OK]Instalando hashcat...")
			os.system("apt-get -y install hashcat")
			print("\n[OK]Concluido...")

	if num =='16':
			print("\n[OK]Instalando aircrack-ng...")
			os.system("apt-get -y install aircrack-ng")
			print("\n[OK]Concluido...")

	if num =='17':
			print("\n[OK]Instalando reaver...")
			os.system("apt-get -y install reaver")
			print("\n[OK]Concluido...")

	if num =='18':
			print("\n[OK]Instalando crunch...")
			os.system("apt-get -y install crunch")
			print("\n[OK]Concluido...")

	if num =='19':
			print("\n[OK]Instalando Perl-Programer...")
			os.system("apt-get -y install perl")
			print("\n[OK]Concluido...")

	if num =='20':
			print("\n[OK]Instalando Netcat...")
			os.system("apt-get -y install netcat")
			print("\n[OK]Concluido...")

	if num =='21':
			print("\n[OK]Instalando Siege...")
			os.system("apt-get -y install siege")
			print("\n[OK]Concluido...")

	if num =='22':
			print("\n[OK]Instalando fcrackzip...")
			os.system("apt-get -y install fcrackzip")
			print("\n[OK]Concluido...")

	if num =='23':
			print("\n[OK]Instalando slowhttptest...")
			os.system("apt-get -y install slowhttptest")
			print("\n[OK]Concluido...")

	if num =='24':
			print("\n[OK]Instalando net-tools...")
			os.system("apt-get -y install net-tools")
			print("\n[OK]Concluido...")

	if num =='25':
			print("\n[OK]Instalando build-essential...")
			os.system("apt-get -y install build-essential")

			print("\n[OK]Instalando ruby-dev...")
			os.system("apt-get -y install ruby-dev")

			print("\n[OK]Instalando libpcap-dev...")
			os.system("apt-get -y install libpcap-dev")

			print("\n[OK]Instalando gem..")
			os.system("apt-get -y install gem")

			print("\n[OK]apt-get update..")
			os.system("apt update")

			print("\n[OK]Instalando bettercap..")
			os.system("gem install bettercap")
			print("\n[OK]Concluido...")

	if num =='26':
			print("\n[OK]Instalando mitmf...")
			os.system("git clone https://github.com/byt3bl33d3r/MITMf.git")
			os.system("apt-get -y install python-dev python-setuptools libpcap0.8-dev libnetfilter-queue-dev libssl-dev libjpeg-dev libxml2-dev libxslt1-dev libcapstone3 libcapstone-dev libffi-dev file")
			os.chdir("MITMf")
			os.system("git submodule init && git submodule update --recursive")
			os.system("apt-get -y install python-pip")
			os.system("pip install -r requirements.txt")
			print("\n[OK]Concluido...")

	if num =='27':
			print("\n[OK]Instalando wget...")
			os.system("apt-get install wget")
			print("\n[OK]Concluido...")

	if num =='28':
			print("\n[OK]Baixando metasploit.run...")
			os.system("apt-get update")
			os.system("apt-get -y install curl")
			os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall")
			os.system("chmod 777 msfinstall")
			os.system("./msfinstall")
			os.system("rm -r msfinstall")
			print("\n[OK]Concluido...")

	if num =='29':
			print("\n[OK]Baixando setoolkit...")
			os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/ set/")
			os.system("chmod 777 set")
			os.chdir("set")
			print("\n[OK]Baixando e instalando dependências...")
			os.system("apt-get -y install wget")
			os.system("wget http://ftp.us.debian.org/debian/pool/main/p/python-crypto/python-crypto_2.6.1-7_amd64.deb")
			os.system("apt-get -y install python-ptyprocess")
			os.system("pip install pexpect")
			os.system("source /etc/profile")
			os.system("dpkg -i python-crypto_2.6.1-7_amd64.deb")
			os.system("rm -r python-crypto_2.6.1-7_amd64.deb")
			print("\n[OK]Concluido")

	if num =='30':
			print("\n[OK]Instalando kazam...")
			os.system("apt-get -y install kazam")
			print("\n[OK]Concluido...")

	if num =='31':
			print("\n[OK]Instalando OpenShot...")
			os.system("apt-get -y install openshot")
			print("\n[OK]Concluido...")

	if num =='32':
			print("\n[OK]Instalando ffmpeg & adb...")
			os.system("apt-get -y install ffmpeg")
			os.system("apt-get -y install adb")
			print("\n[OK]Concluido...")

	if num =='33':
			print("\n[OK]Instalando sqlmap...")
			os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
			os.system("chmod 777 sqlmap")
			print("\n[OK]Concluido...")

	if num =='34':
			print("\n[OK]Instalando fluxion...")
			os.system("git clone https://github.com/wi-fi-analyzer/fluxion.git")
			print("\n[OK]Concluido...")

	if num =='35':
			print("\n[OK]Baixando Proxy Jondonym...")
			os.system("wget https://jondobrowser.jondos.de/other_downloads/jondo_all.deb")
			print("\n[OK]Instalando Proxy Jondonym...")
			os.system("apt-get -y install java-wrappers")
			os.system("source /etc/profile")
			os.system("dpkg -i jondo_all.deb")
			os.system("rm -r jondo_all.deb")
			print("\n[OK]Concluido...")

	if num =='36':
			print("\n[OK]Baixando Code Blocks...")
			os.system("apt-get -y install codeblocks")
			print("\n[OK]Concluido...")

	print('''\033[36m
_______________________________________________________
[]Versao 1.0-------Mr.Apt-Get_Install-------PenTester[]
[]                                                   []
[]------------------Debian - Hacking-----------------[]
[]___________________________________________________[]\033[0;0m''')
	print('''\033[35m
#Linux, #Debian, #hacking,
Script para debian via apt-get install
Escolha as ferramentas a serem instaladas de acordo com as numerações:\033[0;0m''')
	print(''' \033[32m
	|1: make install    |6: vim            |11: ettercap
	|2: git clone       |7: python idle    |12: sslstrip
	|3: figlet          |8: qbitorrent     |13: dsniff  
	|4: codec vlc       |9: nmap           |14: drifnet 
	|5: cmatrix         |10: wireshark     |15: hascat  

	|16: aircrack-ng    |21: siege         |26: mitmf
	|17: reaver         |22: fcrackzip     |27: wget
	|18: crunch         |23: slowhttptest  |28: metasploit
	|19: Perl           |24: net-tools     |29: setoolkit
	|20: netcat         |25: bettercap     |30: kazam

	|31: OpenShot       |36: Code Blocks
	|32: ffmpeg & adb
	|33: sqlmap
	|34: fluxion
	|35: Proxy Jondonym
\033[0;0m''')
	
	num = input("\033[37mEscolha um numero 0/Exit):\033[0;0m")
