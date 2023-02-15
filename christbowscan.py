import socket

# Définit les codes de couleur
green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"

# Définir l'adresse IP de l'hôte à scanner
target = input("Entrez l'adresse IP de l'hôte à scanner: ")

# Scanner les ports ouverts de 1 à 65500
for port in range(1, 65501):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        s.connect((target, port))
        service = socket.getservbyport(port)
        print(f"{green}[+] Port {port} ({service}) is open{reset}")
        s.send(b'Version\n')
        result = s.recv(1024).decode('utf-8').strip()
        if result:
            print(f"{green}[+] Version: {result}{reset}")
        s.close()
    except:
        pass
