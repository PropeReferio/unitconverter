#unitconverter

## Installation

1. Download this file to your home directory.
2. If you like, activate your virtual environment.
3. Using a terminal in the program's directory, run `pip install -r requirements.txt`
4. Mark files as executable: `run chmod +x convert list`
5. Add to path: run `echo 'export PATH=$PATH":$HOME/bin"' >> .profile`
6. Run `source .profile.`

## Running the CLI
1. To see a list of available units, simply run `list`.
2. To convert between these units, run `convert -q {quantity} {original} {final}`.
3. -q and quantity are optional, omitting them will assume you want 1 of the original unit.
