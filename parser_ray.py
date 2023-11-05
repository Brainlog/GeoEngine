import subprocess
# print("fjsafj")
file = open("../Codes_Examples/code.py", "r") 
log = open("../ErrorLogs/log.txt", "w")
# outstream = open("../out.txt", "w")
def parser():
    global file
    str = file.read()
    file.close()
    file = open("../Codes_Examples/code.py", "w")
    # imports = "import georay\n"
    # str = imports + str
    file.write(str)

    try:
        f1 = open("../Codes_Examples/code.py", "r")
        str1 = f1.read()
        print("str1 ",str1)
        f1.close()
        output = subprocess.check_output(["python3", "../Codes_Examples/code.py"], stderr=log)
    except Exception as e:
        print("error")
        print(e)
        return
    # output = subprocess.check_output(["python3", "../Codes_Examples/code.py"], stderr=log)
    file.close()
    log.close()
    # outstream.write(output.decode("utf-8"))
    # outstream.close()
    print("output ",output.decode("utf-8"))
    return

parser()