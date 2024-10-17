from rich import print as rprint
import string
import time
import subprocess
import requests
from bs4 import BeautifulSoup
import qrcode
from rich.console import Console
from rich.prompt import Prompt
import os
import random
import socket
import psutil
import shlex

rooted = False
console = Console()

def enable_root():
    global rooted
    root_confirm = input("Confirm root? (y/n): ")
    if root_confirm.lower() == "y":
        rooted = True
        print("Root enabled.")
    else:
        rooted = False
        print("Root disabled.")

def show_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

def list_files():
    files = os.listdir('.')
    print("Files in current directory:")
    for file in files:
        print(file)

def change_directory(directory):
    try:
        os.chdir(directory)
        print(f"Changed directory to {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found.")

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            print(f"File {filename} created.")
    except IOError:
        print(f"Error creating file {filename}.")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted.")
    except FileNotFoundError:
        print(f"File {filename} not found.")

def list_processes():
    output = subprocess.check_output("ps aux", shell=True, stderr=subprocess.STDOUT, text=True)
    print("Running processes:")
    print(output)

def system_info():
    uname = subprocess.check_output("uname -a", shell=True, stderr=subprocess.STDOUT, text=True)
    print("System information:")
    print(uname)

def ping_host(hostname):
    response = os.system(f"ping -c 1 {hostname}")
    if response == 0:
        print(f"{hostname} is up!")
    else:
        print(f"{hostname} is down!")

def download_file(url, filename):
    try:
        subprocess.run(['wget', '-O', filename, url])
        print(f"Downloaded {url} as {filename}.")
    except subprocess.CalledProcessError:
        print(f"Error downloading {url}.")

def search_file(filename):
    try:
        output = subprocess.check_output(f"find / -name {filename}", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"File {filename} found at:")
        print(output)
    except subprocess.CalledProcessError:
        print(f"File {filename} not found.")

def scan_ports(ip_address):
    try:
        output = subprocess.check_output(f"nmap {ip_address}", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"Port scan results for {ip_address}:")
        print(output)
    except subprocess.CalledProcessError:
        print(f"Error scanning ports for {ip_address}.")

def git_clone(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url])
        print(f"Cloned repository from {repo_url}.")
    except subprocess.CalledProcessError:
        print(f"Error cloning repository from {repo_url}.")

def system_reboot():
    try:
        os.system("sudo reboot")
        print("System rebooting...")
    except:
        print("Failed to reboot system.")

def system_shutdown():
    try:
        os.system("sudo shutdown now")
        print("System shutting down...")
    except:
        print("Failed to shutdown system.")

def list_interfaces():
    output = subprocess.check_output("ifconfig", shell=True, stderr=subprocess.STDOUT, text=True)
    print("Network interfaces:")
    print(output)

def generate_password(tamanho=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(tamanho))
    console.print(f"[bold green]Your password is:[/bold green] {password}")

def currency_converter(value, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
        data = requests.get(url).json()
        rates = data['rates']
        rate = rates[to_currency.upper()]
        result = value * rate
        console.print(f"[bold cyan]Converted value:[/bold cyan] {result:.2f} {to_currency.upper()}")
    except Exception as e:
        console.print("[bold red]Error when searching for exchange rate. Check the currency code.[/bold red]")

def generate_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.show()
    console.print("[bold green]QR Code generated and displayed![/bold green]")

def system_monitoring():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    console.print(f"[bold magenta]CPU:[/bold magenta] {cpu}% | [bold magenta]Memory:[/bold magenta] {memory}%")

tasks = []

def add_task():
    task = Prompt.ask("[bold yellow]Type in the task you want to add[/bold yellow]")
    tasks.append(task)
    console.print(f"[bold green]Task '{task}' added to the list![/bold green]")

def list_tasks():
    if tasks:
        console.print("[bold blue]Your tasks:[/bold blue]")
        for idx, task in enumerate(tasks, 1):
            console.print(f"{idx}. {task}")
    else:
        console.print("[bold red]No tasks on the list.[/bold red]")

def remove_task():
    list_tasks()
    if tasks:
        idx = Prompt.ask("[bold yellow]Enter the task number to remove[/bold yellow]", default="1")
        try:
            removed_task = tasks.pop(int(idx) - 1)
            console.print(f"[bold red]Task '{removed_task}' removed from the list![/bold red]")
        except (ValueError, IndexError):
            console.print("[bold red]Invalid task number![/bold red]")

def compress_files(files_str, output):
    files = files_str.split()
    try:
        subprocess.run(['zip', '-r', output] + files)
        print(f"Files compressed into {output}.")
    except subprocess.CalledProcessError:
        print(f"Error compressing files into {output}.")

def decompress_files(file):
    try:
        subprocess.run(['unzip', file])
        print(f"File {file} decompressed.")
    except subprocess.CalledProcessError:
        print(f"Error decompressing file {file}.")

def show_uptime():
    try:
        output = subprocess.check_output("uptime", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"System uptime:\n{output}")
    except subprocess.CalledProcessError:
        print("Error getting system uptime.")

def memory_usage():
    try:
        output = subprocess.check_output("free -h", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"Memory usage:\n{output}")
    except subprocess.CalledProcessError:
        print("Error getting memory usage.")

def cpu_usage():
    try:
        output = subprocess.check_output("top -bn1 | grep 'Cpu(s)'", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"CPU usage:\n{output}")
    except subprocess.CalledProcessError:
        print("Error getting CPU usage.")

def edit_file(filename):
    try:
        editor = os.getenv('EDITOR', 'nano')
        subprocess.run([editor, filename])
        print(f"File {filename} edited.")
    except subprocess.CalledProcessError:
        print(f"Error editing file {filename}.")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f"Content of {filename}:")
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except IOError:
        print(f"Error reading file {filename}.")

def speed_test():
    try:
        output = subprocess.check_output("speedtest-cli", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"Speed test results:\n{output}")
    except subprocess.CalledProcessError:
        print("Error performing speed test.")

def traceroute(host):
    try:
        output = subprocess.check_output(f"traceroute {host}", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"Traceroute results for {host}:\n{output}")
    except subprocess.CalledProcessError:
        print(f"Error performing traceroute for {host}.")

def whois_query(domain):
    try:
        output = subprocess.check_output(f"whois {domain}", shell=True, stderr=subprocess.STDOUT, text=True)
        print(f"WHOIS results for {domain}:\n{output}")
    except subprocess.CalledProcessError:
        print(f"Error performing WHOIS lookup for {domain}.")

def install_package(package_name):
    try:
        os.system(f"sudo apt-get install -y {package_name}")
        print(f"Package {package_name} installed successfully.")
    except Exception as e:
        print(f"Error installing package: {e}")

def uninstall_package(package_name):
    try:
        os.system(f"sudo apt-get remove -y {package_name}")
        print(f"Package {package_name} removed successfully.")
    except Exception as e:
        print(f"Error removing package: {e}")

def update_repositories():
    try:
        os.system("sudo apt-get update")
        print("System repositories updated.")
    except Exception as e:
        print(f"Error updating repositories: {e}")

def upgrade_system():
    try:
        os.system("sudo apt-get upgrade -y")
        print("System packages upgraded.")
    except Exception as e:
        print(f"Error upgrading packages: {e}")

def flush_dns():
    if rooted:
        try:
            os.system("sudo systemd-resolve --flush-caches")
            print("DNS cache flushed.")
        except Exception as e:
            print(f"Error flushing DNS cache: {e}")
    else:
        print("Root privileges required to flush DNS.")

def add_user(username):
    if rooted:
        try:
            os.system(f"sudo adduser {username}")
            print(f"User {username} added.")
        except Exception as e:
            print(f"Error adding user {username}: {e}")
    else:
        print("Root privileges required to add a user.")

def delete_user(username):
    if rooted:
        try:
            os.system(f"sudo deluser {username}")
            print(f"User {username} deleted.")
        except Exception as e:
            print(f"Error deleting user {username}: {e}")
    else:
        print("Root privileges required to delete a user.")

def clear_syslog():
    if rooted:
        try:
            os.system("sudo truncate -s 0 /var/log/syslog")
            print("System logs cleared.")
        except Exception as e:
            print(f"Error clearing system logs: {e}")
    else:
        print("Root privileges required to clear system logs.")

def set_hostname(new_hostname):
    if rooted:
        try:
            os.system(f"sudo hostnamectl set-hostname {new_hostname}")
            print(f"Hostname changed to {new_hostname}.")
        except Exception as e:
            print(f"Error changing hostname: {e}")
    else:
        print("Root privileges required to change hostname.")

def firewall_status():
    if rooted:
        try:
            output = subprocess.check_output("sudo ufw status", shell=True, text=True)
            print(f"Firewall status:\n{output}")
        except Exception as e:
            print(f"Error checking firewall status: {e}")
    else:
        print("Root privileges required to check firewall status.")

def mount_device(device, mount_point):
    if rooted:
        try:
            os.system(f"sudo mount {device} {mount_point}")
            print(f"Mounted {device} on {mount_point}.")
        except Exception as e:
            print(f"Error mounting device {device}: {e}")
    else:
        print("Root privileges required to mount device.")

def unmount_device(mount_point):
    if rooted:
        try:
            os.system(f"sudo umount {mount_point}")
            print(f"Unmounted {mount_point}.")
        except Exception as e:
            print(f"Error unmounting {mount_point}: {e}")
    else:
        print("Root privileges required to unmount device.")

def kill_process(pid):
    if rooted:
        try:
            os.system(f"sudo kill {pid}")
            print(f"Process {pid} killed.")
        except Exception as e:
            print(f"Error killing process {pid}: {e}")


def display_help():
    print("""
Available commands:
    sip--showip              Display hostname and IP address.
    txt--listfiles           List files in current directory.
    cd <directory>           Change current directory.
    txt--file <filename>     Create a new file.
    txt--delfile <filename>  Delete a file.
    txt--gitclone <repo_url> Clone a GitHub repository.
    sys--list_processes      List running processes.
    sys--info                Display system information.
    sip--ping <hostname>     Ping a hostname.
    txt--download <url> <filename>         Download a file from URL.
    txt--srch_file <filename>              Search for a file.
    sip--scanports <ip_address>            Scan ports of an IP address.
    sys--reboot             Reboot the system.
    sys--list_interfaces    List network interfaces.
    sys--uptime             Show system uptime.
    sys--memory_usage       Display memory usage.
    sys--cpu_usage          Display CPU usage.
    txt--editfile <filename> Edit a text file.
    txt--readfile <filename> Read a text file.
    net--speedtest          Perform a speed test.
    net--traceroute <host>  Perform a traceroute.
    net--whois <domain>     Perform a WHOIS lookup.
    zip--compress <files> <output>   Compress files into a zip archive.
    zip--decompress <file>  Decompress a zip archive.
    generate--password      Generate a random password.
    generate--qrcode <text> Generate a QR Code from text.
    sys--monitor            Display system CPU and memory usage.
    task--add               Add a task to the task list.
    task--list              List all tasks.
    task--remove            Remove a task from the list.
    help                    Display this help message.
    root--ROOT=true         Enable root privileges.
    root--ROOT=false        Disable root privileges.
    shutdown                Shutdown the system.

Rooted commands:
    root--installpkg <package_name>      Install a python package
    root--uninstallpkg <package_name>    Uninstall a python package
    root--updaterepo                     Update the list of system repositories and installed package versions.
    root--upgradeall                     Upgrade all installed packages on the system.
    root--killprocess <pid>              Kill a running process by its process ID (PID).
    root--chmod <permissions> <file_path>           root--chmod <permissions> <file_path>
    root--mount <device> <mount_point>              Mount a device to a specific mount point.
    root--umount <mount_point>           Unmount a device from a mount point.    
    root--flushdns                       Clear the DNS cache.
    root--adduser <username>             Add a new user to the system.
    root--deluser <username>             Remove a user from the system.
    root--clearsyslog                    Clear the system logs.
    root--sethostname <new_hostname>     Change the hostname of the system.
    root--firewallstatus                 Check the status of the system firewall.   
    
Prefixes:
    fun--       Just have fun in games or functions.
    py--        Use for python-related things.
    sip--       IP-related commands.
    txt--       Text file operations.
    sys--       System-related commands.
    net--       Network-related commands.
    zip--       File compression/decompression.
    generate--  Generate passwords, QR codes, etc.
    task--      Task management commands.
    root--      Root-related commands.
    cd          Change directory.
    """)

def run_command(command):
    commands = {
    "sip--showip": show_ip,
    "txt--listfiles": list_files,
    "cd": change_directory,
    "txt--file": create_file,
    "txt--delfile": delete_file,
    "txt--gitclone": git_clone,
    "sys--list_processes": list_processes,
    "sys--info": system_info,
    "sip--ping": ping_host,
    "txt--download": download_file,
    "txt--srch_file": search_file,
    "sip--scanports": scan_ports,
    "sys--reboot": system_reboot,
    "sys--list_interfaces": list_interfaces,
    "sys--uptime": show_uptime,
    "sys--memory_usage": memory_usage,
    "sys--cpu_usage": cpu_usage,
    "txt--editfile": edit_file,
    "txt--readfile": read_file,
    "net--speedtest": speed_test,
    "net--traceroute": traceroute,
    "net--whois": whois_query,
    "zip--compress": compress_files,
    "zip--decompress": decompress_files,
    "generate--password": generate_password,
    "generate--qrcode": generate_qrcode,
    "sys--monitoring": system_monitoring,
    "txt--addtask": add_task,
    "txt--listtasks": list_tasks,
    "txt--removetask": remove_task,
    "cur--convert": currency_converter,
    "sys--shutdown": system_shutdown,
    "root--flushdns": flush_dns,
    "root--adduser": add_user,
    "root--deluser": delete_user,
    "root--clearlogs": clear_syslog,
    "root--sethostname": set_hostname,
    "root--firewallstatus": firewall_status,
    "root--installpackage": install_package,
    "root--uninstallpackage": uninstall_package,
    "root--updaterepos": update_repositories,
    "root--upgradesystem": upgrade_system,
    "root--killprocess": kill_process,
    "root--changepermissions": change_permissions,
    "root--changeowner": change_owner,
    "root--mountdevice": mount_device,
    "root--unmountdevice": unmount_device,
    "root": display_help
}

    command_parts = shlex.split(command)
    if not command_parts:
        print("No command entered.")
        return

    command_type = command_parts[0]
    args = command_parts[1:]

    if command_type in commands:
        try:
            commands[command_type](*args)
        except TypeError as e:
            print(f"Incorrect arguments for command '{command_type}'.")
    else:
        print(f"Command '{command}' not found.")

console.print('''
CatghostOS terminal [[blue]Version: 0.0.0.1[/blue] BETA]
   (©) CatghostOS made by Devdeczin
   Powered by: [bold red]Fsociety[/bold red] 👩🏻‍💻 and [green]Linux Terminal[/green] 🐧
''')

while True:
    usuario = os.getenv("USER") or os.getenv("USERNAME") or "???"
    if not rooted:
        command = input(f"{usuario}@CatGhOSt> ")
    else:
        command = input(f"ROOTEDMODE*{usuario}@CatGhOSt> ")

    if command.strip() == "help":
        display_help()
    elif command.strip():
        run_command(command)
    else:
        print("No command entered.")
