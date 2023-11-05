import subprocess
file = open("./Codes_Examples/code.py", "w") 
log = open("./ErrorLogs/log.txt", "w")
outstream = open("./output_code.txt", "w")
def parser(str):
    imports = "import georay\n"
    str = imports + str
    file.write(str)
    output = subprocess.check_output(["python", "./Codes_Examples/code.py"], stderr=log)
    file.close()
    log.close()
    outstream.write(output.decode("utf-8"))
    outstream.close()
    return