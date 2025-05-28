#!/usr/bin/env python3

import socket
import argparse
import signal
import sys
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# Soporte para colores (opcional)
try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None):
        return text

# Ctrl+C handler
def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa...", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)  # Ctrl+C

def get_arguments():
    parser = argparse.ArgumentParser(description='Escaneo de puertos TCP')
    parser.add_argument("-t", "--target", required=True, help="IP a escanear (Ej: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", required=True, help="Puertos (Ej: -p 1-1000 o 22,80,443)")
    args = parser.parse_args()

    # Validación de IP
    try:
        ipaddress.ip_address(args.target)
    except ValueError:
        print(colored("[!] IP inválida", "red"))
        sys.exit(1)

    return args.target, args.port

def port_scanner(port, host):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            print(colored(f"[+] El puerto {port} está abierto", 'green'))
        except (socket.timeout, ConnectionRefusedError, OSError):
            pass  # Puerto cerrado o inaccesible

def scan_ports(ports, target):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        if start < 1 or end > 65535 or start > end:
            print(colored("[!] Rango de puertos inválido", "red"))
            sys.exit(1)
        return list(range(start, end + 1))
    elif ',' in ports_str:
        ports = list(map(int, ports_str.split(',')))
        if not all(1 <= p <= 65535 for p in ports):
            print(colored("[!] Algún puerto está fuera del rango 1-65535", "red"))
            sys.exit(1)
        return ports
    else:
        port = int(ports_str)
        if not 1 <= port <= 65535:
            print(colored("[!] Puerto fuera del rango 1-65535", "red"))
            sys.exit(1)
        return [port]

def main():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)

if __name__ == '__main__':
    main()
