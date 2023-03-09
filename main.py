import time

time.sleep(3)
print("hi wlcm to tizz game")
time.sleep(2)
main_menu = input("START - CREDITS - QUIT: ")

if main_menu == "CREDITS":
    time.sleep(1)
    print("LOADING")
    time.sleep(2)
    print("MDE BY - RAGHAV RAWAT")
    main_menu = input("START - CREDITS - QUIT: ")
if main_menu == "QUIT":
    time.sleep(2)
    print("bye !(:")
    time.sleep(1)
    quit()
if main_menu == "START":
    time.sleep(4)
    username = input("pls enter the username u want to play the game (only in alphabets): ")
    time.sleep(3)
    print("hi!", username)
    time.sleep(2)
    print("sorry btw tiz is still in progress")
else:
    time.sleep(2)
    print("????? pls make sure u enter the spelling correctly")
