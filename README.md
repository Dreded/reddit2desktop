# reddit2desktop

A simple script that utilizes PRAW to find the hottest post of /r/wallpapers and set it as your desktop wallpaper.

How to use:
I would suggest using a venv
Either git clone or download and extract zip
Enter the folder you created and run...
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

Go to https://www.reddit.com/prefs/apps/ and create a personal script
rename reddit2desktop.config.example to reddit2desktop.config and edit contents as needed

Run the script:
    python3 main.py

If you like it, put it in task scheduler or crontab to run every day for a new wallpaper!
