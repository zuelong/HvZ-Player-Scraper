from robobrowser import RoboBrowser
import getpass
import codecs

username = input("Username: ")
password = getpass.getpass("Password: ")

url = 'http://www.hvzsource.com/account/login'
browser = RoboBrowser()
browser.open(url)

form = browser.get_form(action="/account/login/")
form['email'].value = username
form['password'].value = password
browser.submit_form(form)
link = browser.find("a", href="/players/")
browser.follow_link(link)
player_name_list = []
player_list = []
for tags in browser.select(".game-title"):
    text = tags.text.strip()
    if "Moderator" in text:
        text = text[:-12]
    player_name_list.append(text.strip().upper())
i = 0
for tags in browser.select(".nobottommargin"):
    player_list.append([player_name_list[i], tags.text.strip()[-9:-1].strip().upper()])
    i+=1

file = codecs.open("player_scan.txt", "w", "utf-8")

for player in player_list:
    file.write(player[0] + " | " + player[1] + "\r\n")

file.close()

