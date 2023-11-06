import subprocess
log = open("../ErrorLogs/log.txt", "w")
def parser():
    file = open("../Codes_Examples/code.py", "r") 
    str = file.read()
    file.close()
    file = open("../Codes_Examples/code.py", "w")
    file.write(str)
    file.close()
    try:
        output = subprocess.check_output(["python3", "../Codes_Examples/code.py"], stderr=log)
    except Exception as e:
        print("error")
        print(e)
        return
    # output = subprocess.check_output(["python3", "../Codes_Examples/code.py"], stderr=log)
    file.close()
    log.close()
    print(output.decode("utf-8"))
    return
parser()