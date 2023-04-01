import subprocess
input1 = input()

while True:
   if input1 == "run notepad":
        subprocess.run(['notepad.exe'])
        print("notepad should be running")
        input1 = input()

    if input1 == "run spotify":
        subprocess.run(['spotify.exe'])
        print("spotify should be running")
        input1 =  input()
        if  input1.startswith("play"):
              input1, song_name = input1.split(" ", 1)
              subprocess.call(["spotify", "play",song_name])
    
    if input1 == "quit":
        break          
   
