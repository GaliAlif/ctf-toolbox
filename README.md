\# CTF-Toolbox



A lightweight Python command-line toolkit for beginner-to-intermediate Capture The Flag (CTF) challenges.



\## Features



\- Base64, hexadecimal, and binary encoding and decoding

\- Caesar cipher encryption and decryption

\- Brute-force exploration of all 26 Caesar shifts

\- Text statistics and letter-frequency analysis

\- Automated tests using pytest



\## Requirements



\- Python 3.11 or newer



\## Setup



Clone the repository:



```bash

git clone https://github.com/YOUR\_USERNAME/ctf-toolbox.git

cd ctf-toolbox

```



Create and activate a virtual environment on Windows:



```bat

python -m venv .venv

.venv\\Scripts\\activate

```



Install the project and development dependencies:



```bash

python -m pip install -e ".\[dev]"

```



\## Usage



Encode text using Base64:



```bash

python -m ctf\_toolbox.cli encode base64 "Hello"

```



Decode Base64:



```bash

python -m ctf\_toolbox.cli decode base64 "SGVsbG8="

```



Encrypt using Caesar cipher:



```bash

python -m ctf\_toolbox.cli caesar encrypt "Hello" 3

```



Try every Caesar shift:



```bash

python -m ctf\_toolbox.cli caesar crack "Khoor"

```



Analyze text:



```bash

python -m ctf\_toolbox.cli analyze "Hello World 123"

```



\## Testing



Run the complete test suite:



```bash

python -m pytest -v

```



\## Project Goals



\- Practice Python and modular software design

\- Explore classical cryptography and encoding

\- Build a reusable toolkit for educational CTF exercises

\- Learn automated testing and open-source development



\## Ethical Use



This project is intended for education, offline analysis, and authorized CTF challenges.



\## Roadmap



\- \[x] Encoding and decoding utilities

\- \[x] Caesar cipher solver

\- \[x] Text analyzer

\- \[x] Command-line interface

\- \[x] Initial unit tests

\- \[ ] Continuous integration with GitHub Actions

\- \[ ] Additional CTF utilities



\## License



This project is released under the MIT License.



