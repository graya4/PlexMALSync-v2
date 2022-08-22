import malupdate as mal
import sys
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.video import Episode, Season, Show
from jikanpy import Jikan
# https://python-plexapi.readthedocs.io/en/latest/configuration.html

userInfoFile = open("testingFolders\\userInfo.txt", "r")
userInfoList = userInfoFile.readlines()
userName = userInfoList[0].split("|")[1].strip()
passWord = userInfoList[1].split("|")[1].strip()
plexServerName = userInfoList[2].split("|")[1].strip()
animeServers = userInfoList[3].split("|")
plexUserName = userInfoList[4].split("|")[1].strip()
plexPassWord = userInfoList[5].split("|")[1].strip()
print(animeServers)

userInfo = mal.User.login(userName, passWord)
jikan = Jikan()
show_title = ""
for i in range(1, len(sys.argv)):
    if(i == len(sys.argv)):
        show_title += sys.argv[i]
    else:
        show_title += sys.argv[i] + " "
print(show_title)
print("---------------")
#print(anilist.get_anime_id(show_title))
#print(userInfo)

#print(mal.User.getAnimeList(userInfo["access_token"], "completed"))
found_id = ""
foundFlag = 0
search_result = jikan.search('anime', show_title)
for x in search_result["results"]:
    #print(jikan.anime(x["mal_id"]))
    #print(jikan.anime(x["mal_id"])["title"])
    if(jikan.anime(x["mal_id"])["title"] in show_title):
        found_id = x["mal_id"]
        foundFlag = 1
        #print("FOUND!")
    #print("SYNONYMS")
    for y in jikan.anime(x["mal_id"])["title_synonyms"]:
        #print(y)
        if(y in show_title):
            found_id = x["mal_id"]
            foundFlag = 1
            #print("FOUND!")
    #print("-------------------------------------")
    if(foundFlag == 1):
        break
print(found_id)
#print(mal.Anime.search(userInfo["access_token"], show_title, ["related_anime", "my_list_status"]))
#print(mal.User.getAnimeList(userInfo["access_token"], "watching"))
#print(mal.User.updateList(userInfo["access_token"], 80, {"num_watched_episodes" : 19}))