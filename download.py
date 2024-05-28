import requests
from bs4 import BeautifulSoup
import pathlib
import os
import re
LOGIN_URL = "https://atcoder.jp/login"
def getsession():
    session = requests.session()
    result = session.get(LOGIN_URL)
    soup = BeautifulSoup(result.text,"lxml")
    csrf_token = soup.find(attrs={"name": "csrf_token"}).get("value")
    USERPATH="../username.txt"
    PASSWORDPATH="../password.txt"
    if os.path.exists(USERPATH) and os.path.exists(PASSWORDPATH):
        with open(USERPATH) as f:
            textlist=[s.rstrip() for s in f.readlines()]
            username=textlist[0]
        with open(PASSWORDPATH) as f:
            textlist=[s.rstrip() for s in f.readlines()]
            password=textlist[0]
    else:
        username=input("Input your username: ")
        password = input("Input your password: ")
        with open(USERPATH,mode="w",newline="\n") as f:
            f.write(username)
        with open(PASSWORDPATH,mode="w",newline="\n") as f:
            f.write(password)
    login_info = {
    "csrf_token": csrf_token,
    "username": username,
    "password": password,
    "continue": "https://atcoder.jp"
    }
    result = session.post(LOGIN_URL,data=login_info)
    if result.status_code==200:
        return session
    else:
        return -1
def returnurl():
    nowdirectory=pathlib.Path(os.getcwd()).name
    for i in range(len(nowdirectory)):
        if nowdirectory[len(nowdirectory) - 1 - i] == "_":
            return f"https://atcoder.jp/contests/{nowdirectory[0:(len(nowdirectory)-1-i)]}/tasks/{nowdirectory}"
def savetotest(ar):
    pathtotest = "./test"
    if not os.path.exists(pathtotest):
        os.system("mkdir test")
    for i in range(0,len(ar),2):
        with open(f"{pathtotest}/sample-{i//2}.in",mode="w",newline="\r\n") as f:
            f.write(ar[i])
        with open(f"{pathtotest}/sample-{i//2}.out",mode="w",newline="\r\n") as f:
            f.write(ar[i + 1])
def getsample(url,session):
    result = session.get(url)
    soup = BeautifulSoup(result.text,"lxml")
    rawsample = list(soup.find_all("pre"))
    sample = []
    for i in rawsample:
        if i.string is None:
            continue
        sample.append(i.string)
    sample = sample[0:len(sample)//2]
    return sample

def main():
    mysession=getsession()
    if mysession == -1:
        print("Failed to get session. Aborting...")
        return 1
    problem_url = returnurl()
    print(problem_url)
    sampledata = getsample(problem_url,mysession)
    savetotest(sampledata)

if __name__=="__main__":
    main()