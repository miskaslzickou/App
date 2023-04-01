import subprocess

while True:
    input1 = input("Enter a command: ")
    
    if input1 == "run notepad":
        subprocess.run(['notepad.exe'])
        print("notepad should be running")

    elif input1 == "run spotify":
        subprocess.run(['spotify.exe'])
        print("spotify should be running")

  

    elif input1 == "quit":
        break

    else:
        print("Invalid command")