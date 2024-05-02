# BalogFuzzer
URL Fuzzer is a Python-based tool designed to assist in penetration testing by automating the discovery of hidden directories and files on a web server. As my first project in the ethical hacking space, it serves as a practical application of penetration testing concepts and a platform for continuous learning and development.
![image](https://github.com/Balog9/BalogFuzzer/assets/162159064/5f8772ba-7029-4bcd-936c-d2ec36aad6bc)
![image](https://github.com/Balog9/BalogFuzzer/assets/162159064/53d29314-e549-4320-ae44-746a51546105)



## Key Features
- Automated discovery of web directories and files.
- Option to perform recursive scanning for comprehensive coverage.
- Utilization of custom wordlists to tailor the scan.
- Capability to save scan results for subsequent analysis.
- Adjustable request intervals to manage server load during scanning.


BalogFuzzer is in active development for continuous improvements and feature additions.

## Usage
Run the tool using the following command structure:
```bash
python BalogFuzzer.py -U <URL> -w <wordlist> [options]
```
### Options
- -U, --url [required]: The base URL to start fuzzing.
- -w, --wordlist [required]: Path to the file containing the list of paths to test.
- -r, --recursive: Enable recursive fuzzing into directories found (default is non-recursive).
- -s, --save: Save found paths to the specified file.
- -f, --frequency: Time delay between requests in seconds (to control server load).
  
## Examples

Basic usage:
```bash
python BalogFuzzer.py -U http://example.com -w wordlist.txt
```
Saving results:
```bash
python BalogFuzzer.py -U http://example.com -w wordlist.txt -s results.txt
```
Using a delay between requests:
```bash
python BalogFuzzer.py -U http://example.com -w wordlist.txt -f 0.5
```

## Disclaimer
URL Fuzzer is intended for educational purposes and ethical use only. Always secure permission before running the tool against any web server. Unauthorized testing is illegal and unethical.

## Contributions
Feedback and contributions are welcomed to help improve this tool. Feel free to submit issues, requests, or pull requests on GitHub.

