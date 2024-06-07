# Desktop Cleanup Script
This script monitors your desktop for any new or modified files and automatically moves them to specific folders based on their file extensions. It helps in organizing your desktop and ensuring that files are sorted into appropriate directories.

## Features
Monitors the desktop for new or modified files.
Moves files to specific folders based on their file extensions.
Creates necessary folders if they do not exist.
Logs actions taken by the script for later review.
Installation
Clone the Repository:

sh
Copy code
git clone git@github.com:kmje405/desktop_cleanup.git
cd desktop_cleanup
Install Dependencies:

Make sure you have watchdog installed. If not, install it using pip:

sh
Copy code
pip install watchdog
Configuration
The script is pre-configured to monitor the desktop and sort files into the following folders based on their extensions:

Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff
Documents: .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx
Archives: .zip, .rar, .7z, .tar, .gz
Videos: .mp4, .mov, .wmv, .avi, .mkv
Music: .mp3, .wav, .aac, .flac
If you need to add or change the file extensions or folder names, you can do so by editing the FILE_TYPE_FOLDERS dictionary in the script.

## Usage
Run the Script:

Navigate to the directory where the script is located and run:

sh
Copy code
python desktop_cleanup.py
The script will start monitoring your desktop for any new or modified files and move them to the appropriate folders.

Stop the Script:

To stop the script, press Ctrl+C in the terminal where the script is running.

## Logging
The script logs all its actions to a file named desktop_cleanup.log in the same directory as the script. You can check this log file to see what actions were performed by the script.

## Troubleshooting
Script not moving files: Ensure the script has the necessary permissions to access and move files on your desktop.
Missing folders: The script creates the necessary folders automatically. If a folder is missing, ensure the FILE_TYPE_FOLDERS dictionary is correctly configured.
Logging issues: Check if the desktop_cleanup.log file is created in the script's directory and if it has the correct write permissions.
Contributing
Feel free to submit issues and pull requests to improve this script. Your contributions are welcome!

## License
This script is open-source and available under the MIT License. See the LICENSE file for more details.

