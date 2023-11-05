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
    imports = "import georay\n"
    str = imports + str
    file.write(str)
    output = subprocess.check_output(["python", "../Codes_Examples/code.py"], stderr=log)
    file.close()
    log.close()
    # outstream.write(output.decode("utf-8"))
    # outstream.close()
    print("output ",output.decode("utf-8"))
    return

parser()