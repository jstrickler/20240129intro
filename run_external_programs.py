from subprocess import run, PIPE, SubprocessError

cmd = "hostname"

run(cmd)

process = run(cmd, stdout=PIPE)
raw_output = process.stdout  # bytes
output = raw_output.decode().rstrip()  # str
print(output)
print('-' * 60)

cmd = "netstat -n"
cmd_words = cmd.split()

process = run(cmd_words, stdout=PIPE)
lines = process.stdout.decode().splitlines()
for line in lines:
    if "ESTAB" in line:
        print(line)