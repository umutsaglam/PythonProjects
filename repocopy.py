import requests

username = "umutsaglam"
token = ""

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

repolar = []
page = 1
while True:
    url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        page_repolar = response.json()
        if len(page_repolar) == 0:
            break
        repolar.extend(page_repolar)
        page += 1
    else:
        print("Repolar alınırken bir hata oluştu. Hata kodu:", response.status_code)
        break

for repo in repolar:
    print(repo["full_name"])


