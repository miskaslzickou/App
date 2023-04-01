import subprocess

while True:
    input1 = input("Enter a command: ")
    

    if input1 == "run vs":
        subprocess.run(["code.exe"])
        print("vs should be running")

    if input1 == "run spotify":
        subprocess.run(['spotify.exe'])
        print("spotify should be running")
    
    if input1 == "run task":
        subprocess.run(['Taskmgr.exe'])
        print("task manager should be running")
    
    if input1 == "run firefox":
        subprocess.run(['C:/Program Files/Mozilla Firefox/firefox.exe'])
        print("Firefox should be running")
    
    if input1 == "run notepad":
        subprocess.run(['notepad.exe'])
        print("notepad should be running")

    if  input1 == "run chrome ytb":
        subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','https://www.youtube.com/'])
        print("chrome should be running with soap2dayto")
      
    if  input1 == "run chrome gpt":
        subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','https://chat.openai.com/chat'])
        print("chrome should be running with soap2dayto")
      
    
    if  input1 == "run chrome soap":
        subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','https://soap2day.to/enter.html?url=/?__cf_chl_jschl_tk__=pmd_95bebfbb2a1d1628b42a8f552051eec10d86f9b1-1627413961-0-gqNtZGzNAc2jcnBszQhi'])
        print("chrome should be running with soap2dayto")
    
    if input1 == "run dis":
        subprocess.run(['discord.exe'])
        print("discord started")
   
   
    if input1 == "kill all":
        subprocess.run(['taskkill', '/f', '/im', 'spotify.exe'])
        subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'])
        subprocess.run(['taskkill', '/f', '/im', 'firefox.exe'])
        subprocess.run(['taskkill', '/f', '/im', 'code.exe'])
   
    if input1 == "kill spotify":
        subprocess.run(['taskkill', '/f', '/im', 'spotify.exe'])
        print("spotify terminated")
    
    if input1 == "kill firefox":
        subprocess.run(['taskkill', '/f', '/im', 'firefox.exe'])
        print("firefox terminated")
    if input1 == "kill vs":
        subprocess.run(['taskkill', '/f', '/im', 'code.exe'])
        print("vs terminated")
    if input1 == "kill chrome":
        subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'])
        print("chrome terminated")
 

    if input1 == "quit":
        break

    else:
        print("Invalid command")