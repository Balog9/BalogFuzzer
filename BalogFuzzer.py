import requests
import argparse
from colorama import Fore, Style, init
import time
from tqdm import tqdm

def display_banner():
    banner_text = """
 __        __   _                            _____       _____ _          
 \ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__   |_   _| |__   ___ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \    | | | '_ \ / _ 
   \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |   | | | | | |  __/
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/    |_| |_| |_|\___|
                                                                                                                                                                                    
▀█████████▄     ▄████████  ▄█        ▄██████▄     ▄██████▄     ▄████████ ███    █▄   ▄███████▄   ▄███████▄     ▄████████    ▄████████ 
  ███    ███   ███    ███ ███       ███    ███   ███    ███   ███    ███ ███    ███ ██▀     ▄██ ██▀     ▄██   ███    ███   ███    ███ 
  ███    ███   ███    ███ ███       ███    ███   ███    █▀    ███    █▀  ███    ███       ▄███▀       ▄███▀   ███    █▀    ███    ███ 
 ▄███▄▄▄██▀    ███    ███ ███       ███    ███  ▄███         ▄███▄▄▄     ███    ███  ▀█▀▄███▀▄▄  ▀█▀▄███▀▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀██▄  ▀███████████ ███       ███    ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███   ▄███▀   ▀   ▄███▀   ▀ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ██▄   ███    ███ ███       ███    ███   ███    ███   ███        ███    ███ ▄███▀       ▄███▀         ███    █▄  ▀███████████ 
  ███    ███   ███    ███ ███▌    ▄ ███    ███   ███    ███   ███        ███    ███ ███▄     ▄█ ███▄     ▄█   ███    ███   ███    ███ 
▄█████████▀    ███    █▀  █████▄▄██  ▀██████▀    ████████▀    ███        ████████▀   ▀████████▀  ▀████████▀   ██████████   ███    ███ 
                          ▀                                                                                                ███    ███ 
                                                                                                            
                                    Made By: Or Balog
    """
    print(Fore.MAGENTA + banner_text + Style.RESET_ALL)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Recursive URL Directory Fuzzer')
    parser.add_argument('-U', '--url', required=True, help='Base URL to fuzz')
    parser.add_argument('-w', '--wordlist', required=True, help='File containing paths to fuzz')
    parser.add_argument('-r', '--recursive', action='store_true', help='Enable recursive fuzzing')
    parser.add_argument('-s', '--save', help='Save the results to a file')
    parser.add_argument('-f', '--frequency', type=float, default=0, help='Frequency of requests in seconds')
    return parser.parse_args()

def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + "\n")


def fuzz_url(base_url, path, depth=0, max_depth=3, recursive=False, wordlist_path=None, save_file=None, frequency=0, total_paths=None, current_index=None):
    if total_paths is not None and current_index is not None:
        progress = (current_index + 1) / total_paths * 100
        print(f"Progress: {progress:.2f}% ({current_index + 1}/{total_paths})", end='\r')

    if depth > max_depth:
        return
    
    # Form the full URL
    full_url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    
    # Avoid too frequent requests
    time.sleep(frequency)
    
    # Perform the HTTP request
    try:
        response = requests.get(full_url)
        if response.status_code in [200, 302, 423, 402]:
            color = Fore.GREEN if response.status_code == 200 else Fore.YELLOW
            result = f"{color}• Found path: {full_url} (Status: {response.status_code}){Style.RESET_ALL}"
            print(result)
            
            # Save to file if requested
            if save_file:
                write_to_file(save_file, f"• Found path: {full_url} (Status: {response.status_code})\n")
                
            # If recursive is true and the status code is 200, recurse into the directory
            if recursive and response.status_code == 200:
                next_level = load_wordlist(wordlist_path)
                for next_path in next_level:
                    fuzz_url(f"{full_url}/", next_path, depth+1, max_depth, recursive, wordlist_path, save_file, frequency)

    except requests.exceptions.RequestException as e:
        error_msg = f"{Fore.RED}Failed to connect to {full_url}: {e}{Style.RESET_ALL}"
        print(error_msg)
        if save_file:
            write_to_file(save_file, f"Failed to connect to {full_url}: {e}\n")

def display_completion_banner():
    completion_banner = """
    ███████╗██╗███╗   ██╗██╗███████╗██╗  ██╗███████╗██████╗ ██╗
    ██╔════╝██║████╗  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗██║
    █████╗  ██║██╔██╗ ██║██║███████╗███████║█████╗  ██║  ██║██║
    ██╔══╝  ██║██║╚██╗██║██║╚════██║██╔══██║██╔══╝  ██║  ██║╚═╝
    ██║     ██║██║ ╚████║██║███████║██║  ██║███████╗██████╔╝██╗
    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝
                                                           
    
         Scan Complete! Thank you for using BalogFuzzer!.
                      Made by Or Balog
89 97 108 108 97  72 97 112 111 101 108 33  89 97 108 108 97  66 101 101 114  83 104 101 118 97 33 

    """
    print(Fore.MAGENTA + completion_banner + Style.RESET_ALL)

def main():
    init()  # Initialize Colorama
    display_banner() 
    args = parse_arguments()
    paths = load_wordlist(args.wordlist)
    
    # Wrap paths with tqdm for a progress bar
    for path in tqdm(paths, desc='Fuzzing URLs', unit='url'):
        fuzz_url(args.url, path, recursive=args.recursive, wordlist_path=args.wordlist, save_file=args.save, frequency=args.frequency)
    
    display_completion_banner()  

if __name__ == "__main__":
    main()
