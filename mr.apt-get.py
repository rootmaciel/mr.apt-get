#usr/bin/python3

import os
os.system("neofetch")
print('''\033[36m
    _______________________________________________________
    []Versao 1.1-------Mr.Apt-Get_Install-------PenTester[]
    []                                                   []
    []------Debian------Diego - Maciel------Hacking------[]
    []___________________________________________________[]\033[0;0m''')
print('''\033[35m
    #Linux, #Debian, #Hacking,
    Script para debian via apt-get install
    Escolha as ferramentas a serem instaladas de acordo com as numerações:\033[0;0m''')

print("\nPara uma Instalação Recomenda Numero(99)")

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

    |31: OpenShot       |36: Code Blocks   |41: ltrace
    |32: ffmpeg & adb   |37: binwalk       |42: searchsploit
    |33: sqlmap         |38: PyJupyter     |43: dnsrecon
    |34: fluxion        |39: Xprobe2       |44: dirb
    |35: okadminfinder  |40: wpscan        |45: Storm-Breaker

    |46: Parcellite     |47: Bluetooth     |48: Zaproxy
\033[0;0m''')

num = input("\033[37mEscolha um numero (0/Exit): \033[0;0m")

while num != 0:

    if num == '0':
        print("Thanks u")
        os.system(exit())

    if num == '99':
        num1 = input("Instalação Recomendada não inclui ferramentas como metasploit, setoolkit, entre outras, Deseja Continuar? Enter ou (0/Exit): ")
        if num1 == '0':
            print("Thanks u")
            os.system(exit())
        
        os.system("apt install -y make git figlet vlc cmatrix vim idle3 python-pip python3-pip nmap qbittorrent wireshark ettercap-graphical sslstrip dsniff driftnet aircrack-ng libclc-dev libclc-r600 mesa-opencl-icd ocl-icd-libopencl1 hashcat aircrack-ng reaver crunch perl netcat siege fcrackzip slowhttptest net-tools wget kazam openshot ffmpeg adb codeblocks binwalk dnsrecon ltrace dirb parcellite blueman")

    if num == '1':
        print("\n[OK]Instalando make install...")
        os.system("apt-get -y install make")
        print("\n[OK]Concluido...")

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
        os.system("apt-get -y install python3-pip")
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
        os.system("chmod 777 -R MITMf")
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
        print("\n[OK]Baixando e instalando dependências...")
        os.system("apt -y install python-pip")
        os.system("apt-get -y install python-ptyprocess")
        os.system("pip install pexpect")
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git")
        os.system("chmod 777 -R social-engineer-toolkit")
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
        os.system("chmod 777 -R sqlmap")
        print("\n[OK]Concluido...")

    if num =='34':
        print("\n[OK]Instalando fluxion...")
        os.system("git clone https://github.com/wi-fi-analyzer/fluxion.git")
        os.system("chmod 777 -R fluxion")
        print("\n[OK]Concluido...")

    if num =='35':
        print("\n[OK]Instalando OkAdminFinder...")
        os.system("git clone https://github.com/mIcHyAmRaNe/okadminfinder3.git")
        os.system("chmod 777 -R okadminfinder3")
        os.chdir("okadminfinder3")
        os.system("apt-get -y install tor")
        os.system("apt-get -y install python3-socks")
        os.system("apt-get -y install python-pip")
        os.system("apt-get -y install python3-pip")
        os.system("pip3 install --user -r requirements.txt")
        print("\n[OK]Concluido...")

    if num =='36':
        print("\n[OK]Baixando Code Blocks...")
        os.system("apt-get -y install codeblocks")
        print("\n[OK]Concluido...")

    if num =='37':
        print("\n[OK]Baixando Binwalk...")
        os.system("apt-get -y install binwalk")
        print("\n[OK]Concluido...")

    if num =='38':
        print("\n[OK]Baixando PyJupyter...")
        os.system("apt-get -y install python3")
        os.system("python3 -m pip install --upgrade pip")
        os.system("pip3 install Jupyter")
        os.system("pip3 install pyautogui")
        os.system("pip3 install pyperclip")
        print("\n[OK]Concluido...")
        print("\nOBS: No Error = P/ Iniciar: pyjupyter notebook")

    if num =='39':
        print("\n[OK]Baixando Xprobe2...")
        os.system("apt-get -y install xprobe2")
        print("\n[OK]Concluido...")

    if num =='40':
        print("\n[OK]Baixando wpscan...")
        os.system("apt update && sudo apt upgrade -y")
        os.system("apt install curl git libcurl4-openssl-dev make zlib1g-dev gawk g++ gcc libreadline6-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config ruby ruby-bundler ruby-dev")
        os.system("gem install wpscan")
        print("\n[OK]Concluido...")

    if num =='41':
        print("\n[OK]Instalando ltrace...")
        os.system("apt-get install ltrace")
        print("\n[OK]Concluido...")

    if num =='42':
        print("\n[OK]Instalando searchsploit...")
        os.system("apt-get install snap")
        os.system("apt-get install snapd")
        os.system("snap install core")
        os.system("snap install searchsploit")
        os.system("clone https://github.com/offensive-security/exploitdb.git")
        print("\n[OK]Concluido...")

    if num =='43':
        print("\n[OK]Instalando dnsrecon...")
        os.system("apt-get install dnsrecon")
        print("\n[OK]Concluido..")

    if num =='44':
        print("\n[OK]Instalando dirb...")
        os.system("apt-get install dirb")
        print("\n[OK]Concluido..")
        
    if num =='45':
        print("\n[OK]Instalando Storm-Breaker...")
        os.system("git clone https://github.com/ultrasecurity/Storm-Breaker.git")
        os.system("cd Storm-Breaker")
        os.system("bash install.sh")
        os.system("python3 -m pip install -r requirements.txt")
        print("\n[OK]Concluido..")

    if num =='46':
        print("\n[OK]Instalando Area de Transferencia...")
        os.system("apt-get install parcellite")
        print("\n[OK]Concluido..")
    
    if num =='47':
        print("\n[OK]Instalando Bluetooth...")
        os.system("apt-get install blueman")
        print("\n[OK]Concluido..")

    if num =='48':
        print("\n[OK]Instalando ZAPROXY...")
        os.system("echo 'deb http://download.opensuse.org/repositories/home:/cabelo/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/home:cabelo.list")
        os.system("curl -fsSL https://download.opensuse.org/repositories/home:cabelo/Debian_12/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_cabelo.gpg > /dev/null")
        os.system("sudo apt update")
        os.system("sudo apt install owasp-zap")
        print("\n[OK]Concluido..")
        
    print('''\033[36m
    _______________________________________________________
    []Versao 1.1-------Mr.Apt-Get_Install-------PenTester[]
    []                                                   []
    []------Debian------Diego - Maciel------Hacking------[]
    []___________________________________________________[]\033[0;0m''')
    print('''\033[35m
    #Linux, #Debian, #Hacking,
    Script para debian via apt-get install
    Escolha as ferramentas a serem instaladas de acordo com as numerações:\033[0;0m''')

    print("\nPara uma Instalação Recomenda Numero(99)")

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

    |31: OpenShot       |36: Code Blocks   |41: ltrace
    |32: ffmpeg & adb   |37: binwalk       |42: searchsploit
    |33: sqlmap         |38: PyJupyter     |43: dnsrecon
    |34: fluxion        |39: Xprobe2       |44: dirb
    |35: okadminfinder  |40: wpscan        |45: Storm-Breaker

    |46: Parcellite     |47: Bluetooth     |48: Zaproxy
    \033[0;0m''')

    num = input("\033[37mEscolha um numero (0/Exit):\033[0;0m")
