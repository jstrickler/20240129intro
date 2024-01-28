import os

os.system("hostname")  # Just run "hostname"

with os.popen('netstat -an') as netstat_in:  # Open command line "netstat -an" as a file-like object
    for entry in netstat_in:  # Iterate over lines in output of "netstat -an"
        if 'ESTAB' in entry:  # Check to see if line contains "ESTAB"
            print(entry, end='')
print()
