# Welcome to Brutos Directory Scanner 🚀

The Brutos is a python script used to provide agility in obtaining verifications to informations about related to directories in URLs destined for CTF (Capture the Flag) challenges.

Note: Please don't use this script on servers that you don't have permissions for (and if you do this it is just your responsibility).

## Author:

- [Sérgio Corrêa](https://github.com/correa-sergio)


## How to Run:

- Clone the project

```bash
git clone https://github.com/correa-sergio/brutos-dir-url
```
- Go to the project directory

```bash
cd brutos-dir-url
```

## Install the Requirements

- create a virtual environment (Optional)
```bash
python3 -m venv venv
```

- Activate the Environment (Optional)

```bash
source venv/bin/activate
```
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.

```bash
pip install -r requirements.txt
```
- Input

```python
python3 brutos.py -h
```

```python 
Usage example: 

usage: Ex: python3 brutos.py -u just-an-example-CTF.com.br -f wordlist.txt

Brutos URL Scanner - Version 1.0

optional arguments:
  -h, --help            Show this help message and exit
  -f FILE, --file FILE  The list of words for analysis
  -u URL, --url URL     The address reflected in the target
  -v, --version         Show program's version number and exit
```

- Output Example:

```python
Processing ... ████████████████████████████████ 100%

[+] http://just-an-example-CTF.com.br:8080/app
[+] http://just-an-example-CTF.com.br:8080/css
[+] http://just-an-example-CTF.com.br:8080/login

[!] Processing Time : - 0:00:00.004054
[!] We found 3 directory(ies)
[!] Brutos Directory Scanner - v. 1.0
```

## License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Contribution:

Suggestions and issues are welcome (Feel free to send me an e-mail). ✉️

Made with love. By me. To the community ♥️