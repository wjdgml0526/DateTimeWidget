# DateTimeWidget <br>
<img width="1113" alt="스크린샷 2024-11-12 오후 10 09 31" src="https://github.com/user-attachments/assets/debf16aa-a517-40c1-8068-478a67d31a58"><br>

## Overview <br>
DateTimeWidget is a Python-based desktop widget that displays the current date and time in real-time. Built with Tkinter, this widget is designed for live streaming overlays or as a standalone desktop app. The widget’s appearance can be customized, and it includes a sleek, Darcula-themed interface, inspired by PyCharm.<br>

## Features
- Display today's date and current time
- Updates the time every second
- Customizable colors and font.

## Requirements
This project requires Python and the `tkinter` library, along with a specific font for consistent styling.

### Installation
1. Ensure you have Python installed. [Download Python](https://www.python.org/downloads/) if you don’t have it.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/LiveTimeWidget.git
   cd LiveTimeWidget
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Install the [NanumGothicCoding](https://fonts.google.com/specimen/Nanum+Gothic+Coding) font:
   - Download it from Google Fonts.
   - After downloading, install the font on your system:
     - Windows: Right-click the font file and select "Install."
     - MacOS: Double-click the font file and select "Install Font."
     - Linux: Move the font file to the `.fonts` directory in your home folder or `/usr/share/fonts` and refresh the font cache with `fc-cache -f -v`.

## Creating an Executable with PyInstaller
To bundle this project as a standalone executable, you can use `PyInstaller`.<br>
Note that PyInstaller creates executables specific to the OS it’s run on. For example, running PyInstaller on Windows will create a Windows .exe file, while running it on Linux will generate a Linux-compatible executable. Cross-compiling (creating a Windows executable from Linux or vice versa) generally requires additional setup.
1. Run the following command to create and executable:
   ```bash
   pyinstaller --onefile --windowed app.py
   ```
   - `--onefile` creates a single executable
   - `--windowed` hides the console window (useful for GUI apps).
2. After the build is complete, the executable file will be the `dist` folder.
