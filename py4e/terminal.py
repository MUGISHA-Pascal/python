import subprocess
import os

def run_command(command):
    result=subprocess.run(command,shell=True,capture_output=True,text=True)
    if result.returncode != 0:
        print(f"the error is {result.stderr}")
    else:
        print(f"the output is {result.stdout}")
def main():
    app_name=input("enter the name of the nodejs app : ")
    modules=input("enter the modules to install (separated by space) : ")
    os.mkdir(app_name)
    os.chdir(app_name)

    run_command("npm init -y")
    run_command(f"npm install {modules}")

    indexjs_content="console.log(hello world);"

    with open("index.js","w") as file:
        file.write(indexjs_content)
    print(f"created the nodejs app :{app_name}")
if __name__ =="__main__":
    main()

