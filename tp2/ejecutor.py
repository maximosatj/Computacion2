import argparse
import subprocess
import os
import datetime

parser=argparse.ArgumentParser()
parser.add_argument("-c", "--command", required=True)
parser.add_argument("-f", "--output_file", required=True)
parser.add_argument("-l", "--log_file", required=True)
args=parser.parse_args()

if not os.path.isfile(args.output_file):
    open(args.output_file, "a").close()

if not os.path.isfile(args.log_file):
    open(args.log_file, "a").close()

try:
    process=subprocess.Popen(args.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode==0:
        with open(args.log_file, "a") as f:
            f.write("{}: Comando \"{}\" ejecutado correctamente.\n".format(datetime.datetime.now(), args.command))
    else:
        with open(args.log_file, "a") as f:
            f.write("{}: {}\n".format(datetime.datetime.now(), error.decode().strip()))

except Exception as e:
    with open(args.log_file, "a") as f:
        f.write("{}: {}\n".format(datetime.datetime.now(), str(e)))

with open(args.output_file, "a") as f:
    f.write(output.decode())