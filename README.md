# Kasim LaunchPad Loading Screen

## Overview

The **Kasim LaunchPad Loading Screen** is an open-source, Python-based application that provides an attractive loading screen for desktop applications. Built using Tkinter and PIL, this project displays a splash screen with a rotating progress indicator, a logo, and a copyright notice. It serves as an excellent starting point for integrating a polished loading screen into your own projects.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Configuration](#configuration)
- [Installation & Usage](#installation--usage)
- [File Details](#file-details)
- [License](#license)
- [Contact](#contact)

## Features

- **Animated Splash Screen**:  
  Displays a loading screen with a rotating arc to indicate progress.
  
- **Customizable Branding**:  
  Shows your project name and logo, which can be set via a configuration file.
  
- **Interactive Copyright Notice**:  
  Includes a clickable label that opens the GitHub profile when clicked.
  
- **Centralized Configuration**:  
  Uses a `config.ini` file to manage project name, logo path, and GitHub URL.
  
- **Open Source**:  
  The project is released under the MIT License, allowing you to modify and use it freely.

## Configuration

Before running the application, update the `config.ini` file with your desired settings. Key parameters include:

- **project_name**: The name of your project (e.g., "Kasim LaunchPad").
- **logo_path**: The path to your logo image file.

### Example \`config.ini\`:

```ini
[DEFAULT]
project_name = Kasim LaunchPad
logo_path = images/your_logo.png
github_url = https://github.com/kasyan1337
```

## Installation \& Usage

1. Ensure Python 3.7 or later is installed on your system.
2. Clone the Repository:
```bash
git clone <repository_url>
```
3. Navigate to the Project Directory:
```bash
cd <project_directory>
```
4. Install Dependencies:
```bash
pip install -r requirements.txt
```

\*Required packages:\* \`tkinter\` \(pre-installed with Python\), \`Pillow\` \(PIL\)

5. Run the Application:
```bash
python main.py
```

Upon running, the application will display a splash screen for the duration specified in the code \(default is 4000 milliseconds\), then automatically close.

## File Details

- \`main.py\`:
  Contains the main logic to display the splash screen, load configurations from \`config.ini\`, and manage the GUI elements.
- \`config.ini\`:
  Configuration file for setting the project name, logo path, and GitHub URL.
- \`images/\`:
  Directory for storing the logo image and other visual assets.

## License

This project is open source and is released under the MIT License. You are free to use, modify, and distribute this software as long as the original license terms are included.

## Contact

For support or inquiries, please contact Kasim Janci at kasim.janci98@gmail.com.