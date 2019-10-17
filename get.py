# get.py

import requests

res = requests.get('https://api.github.com/users/cjineson')
data = res.json()
print('Login: ' + data['login'])
repos = data['repos_url']
print('Repos URL: ' + repos)

res = requests.get(repos)
data = res.json()
for repo in data:
    print('Repo: ' + repo['full_name'] +'\t URL: ' + repo['url'])