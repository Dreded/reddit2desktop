# reddit2desktop

A simple script that utilizes PRAW to find the hottest X posts of a random list of subs you specify and set it as your desktop wallpaper.\
Should work in Windows or KDE Plasma\
The Script will choose 1 image at random from the list of subs you specify and it defaults to randomly selecting one of the top 10 posts.\
\
How to use:\
I would suggest using a venv\
Either git clone or download and extract zip\
Enter the folder you created and run...\
python3 -m venv venv\
source ./venv/bin/activate\
pip install -r requirements.txt\
\
Go to https://www.reddit.com/prefs/apps/ and create a personal script\
rename reddit2desktop.config.example to reddit2desktop.config and edit contents as needed\
at the very least you will need to add your client_id and client_secret found on the link above(click edit for secret id is below app name)\
\
Run the script:\
    python3 main.py\
\
If you like it, put it in task scheduler or crontab to run every day for a new wallpaper!\
