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
    username = input("Input your username: ")
    password = input("Input your password: ")
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
    for i in range(len(ar)//2):
        with open(f"{pathtotest}/sample-{i}.in",mode="w",newline="\n") as f:
            f.write(ar[2 * i])
        with open(f"{pathtotest}/sample-{i}.out",mode="w",newline="\n") as f:
            f.write(ar[2 * i + 1])
def main():
    mysession=getsession()
    if mysession == -1:
        print("Failed to get session. Aborting...")
        return 1
    problem_url = "https://atcoder.jp/contests/abc355/submissions"
    result = mysession.get(problem_url)
    print(result.text)
    print(result.url)

if __name__=="__main__":
    main()