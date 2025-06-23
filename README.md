To convert from py to exe:

1. Open terminal in the folder where your main is
2. Run this command: pyinstaller --onefile your_script.py

Your exe will be in the dist folder

Note:

Hide Console Window:
pyinstaller --onefile --noconsole your_script.py

Add icon:
pyinstaller --onefile --icon=youricon.ico your_script.py
