#!/usr/bin/python3
import subprocess

def run_dos_scripts(scripts):
    processes = []
    for script in scripts:
        process = subprocess.Popen(['python', script])
        processes.append(process)
    return processes

def main():
    dos_files = ['dos1.py', 'dos2.py', 'dos3.py', 'dos4.py', 'dos5.py']
    processes = run_dos_scripts(dos_files)
    
    print("All DoS scripts are running.")
    
    try:
        for process in processes:
            process.wait()  # Wait for all processes to complete
    except KeyboardInterrupt:
        print("Interrupted. Terminating all processes.")
        for process in processes:
            process.terminate()  # Terminate processes on interruption

if __name__ == '__main__':
    main()
