import os
import time

intro = '''
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   GMR @  `98v8P'   NUKER   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '

                      > กดปุ่มตกลง
'''

def print_intro():
    for line in intro.splitlines():
        print(line)
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน

def print_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = '''
   )   (          (        (    )   
  ())  )\  ( (  : )\  (    )\  ((.  
 (()))((_) )\)\  (_() )\  ((_) ))\  
(/ __|(_))(_((_)((_)()( )((_))((_)) 
| (_ | || | '  \/ _` | '_| || | ' \)
 \___|\_._|_|_|_|__/_|_|  \_._|_||_|
                                           
    > Gumarun Store ©
    '''
    print(banner)

# เรียกใช้ฟังก์ชัน
# print_intro()
# input("\nกด Enter เพื่อดำเนินการต่อ...")  # รอผู้ใช้กด Enter
print_logo()