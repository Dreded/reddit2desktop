# reddit2desktop
Original Coded by: Evan Nguyen which can be found at: https://github.com/nguyenevan42/reddit2desktop \
His version is hardcoded to pick the hottest image from /r/wallpapers and only works on windows\
\
A simple script that utilizes PRAW to find the hottest X posts of a random sub from a list of subs you specify and set it as your desktop wallpaper.\
Should work in Windows or KDE Plasma\
\
The Script will choose 1 image at random from the list of subs you specify[Setting in Config file]\
It defaults to randomly selecting one of the top 10 hottest posts.[Setting in Config file]\
\
How to use:\
Either git clone or download and extract zip\
Enter the folder you created and run...\
\
I would suggest using a venv\
    >python3 -m venv venv\
    >source ./venv/bin/activate\
    >pip install -r requirements.txt\
\
Otherwise just globally install the requirements\
    >pip install -r requirements.txt\
\
Go to https://www.reddit.com/prefs/apps/ and create a personal script\
rename reddit2desktop.config.example to reddit2desktop.config and edit contents as needed\
at the very least you will need to add your client_id and client_secret found on the link above(click edit for secret id is below app name)\
\
Run the script:\
    >python3 main.py\
\
If you like it, put it in task scheduler or crontab to run every day for a new wallpaper!\
If you run the python inside the venv it will have the needed libraries availiable\
\
i added this to cron(crontab -e) so it runs everyday at 8am:\
"* 8 * * *~/Python/reddit2desktop/venv/bin/python ~/Python/reddit2desktop/main.py"
