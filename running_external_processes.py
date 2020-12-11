from subprocess import run, PIPE, CalledProcessError
import shlex
from pprint import pprint

raw_cmd = "netstat -an"

# runs on linux/Mac
# proc = run(raw_cmd, shell=True)  # slight security issue

# also runs on linux/Mac

cmd_words = shlex.split(raw_cmd)
try:
    proc = run(cmd_words, stdout=PIPE)
except CalledProcessError as err:
    print(err)
else:
    output = proc.stdout.decode().splitlines()

    # pprint(output)

    for line in output:
        if 'ESTABLISHED' in line:
            proto, inq, outq, local_ip, remote_ip, status = line.split()
            print(f"{local_ip:30s} {remote_ip:30s}")


#----------------------------------------------
# import subprocess
#
#
#
# def execute(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#
#     # Poll process for new output until finished
#     while True:
#         nextline = process.stdout.readline()
#         if nextline == '' and process.poll() is not None:
#             break
#         sys.stdout.write(nextline)
#         sys.stdout.flush()
#
#     output = process.communicate()[0]
#     exitCode = process.returncode
#
#     if (exitCode == 0):
#         return output
#     else:
#         raise ProcessException(command, exitCode, output)
#
