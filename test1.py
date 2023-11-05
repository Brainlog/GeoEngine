import subprocess
output = subprocess.check_output(["python3", "test2.py"])
print(output.decode("utf-8"))