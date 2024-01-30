import subprocess

def monitor_terminal_errors(command):
    process = subprocess.Popen(['powershell.exe', '-Command', command], shell=True, stderr=subprocess.PIPE)
    
    while True:
        output = process.stderr.readline().decode().strip()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output)

if __name__ == "__main__":
    command_to_run = 'Start-Transcript -Path "error.txt"'
    monitor_terminal_errors(command_to_run)
