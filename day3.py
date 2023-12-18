#Day3 project
print('''
   180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
    |     |     |     |     |     |     |     |     |     |     |     |     |
90N-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90N
    |           . _..::__:  ,-"-"._        |7       ,     _,.__             |
    |   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|
    |>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                mt-2_|
60N-+  \_.:--.       `._ )`^-. "'       , [_/(                       __,/-' +-60N
    | '"'     \         "    _L        oD_,--'                )     /. (|   |
    |          |           ,'          _)_.\\._<> 6              _,' /  '   |
    |          `.         /           [_/_'` `"(                <'}  )      |
30N-+           \\    .-. )           /   `-'"..' `:._          _)  '       +-30N
    |    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |
    |              `._,   ""         |           \`'   \|   ?_)  {\         |
    |                 `=.---.        `._._       ,'     "`  |' ,- '.        |
000-+                   |    `-._         |     /          `:`<_|h--._      +-000
    |                   (        >        .     | ,          `=.__.`-'\     |
    |                    `.     /         |     |{|              ,-.,\     .|
    |                     |   ,'           \   / `'            ,"     \     |
30S-+                     |  /              |_'                |  __  /     +-30S
    |                     | |                                  '-'  `-'   \.|
    |                     |/                                         "    / |
    |                     \.                                             '  |
60S-+                                                                       +-60S
    |                      ,/            ______._.--._ _..---.---------._   |
    |     ,-----"-..?----_/ )      __,-'"             "                  (  |
    |-.._(                  `-----'                                       `-|
90S-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90S
    Map 1998 Matthew Thomas.|Freely usable as long as this|line is included.|
    |     |     |     |     |     |     |     |     |     |     |     |     |
   180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----
''')
print("      Welcome to Lalitpur!\nYour mission is to reach my college.\n")
choice1=input('You are at my gate. Where do you want to go?Type "Left" or "Right"').lower()
if choice1=="left":
    choice2=input('You have come to the busstop. And there is a bus. Type "walk" to walk for the college or Type "ride" ').lower()
    if choice2=="ride":
        choice3=input("Your bus has reached Nabil Bank. Will you get out of the bus?Yes or No ").lower()
        if(choice3=="yes"):
            print("You have reached my college. Mission Successful!")
        else:
            print("Nobody knows where you gonna end up. Mission Failed!")    
        
    else:
        print("You'll get lost.Mission Failed!")   
else:
    print("You'll get lost.Mission Failed!")    

