#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.requests ps.schedule ps.pygithub ps.aiohttp ])"
# Above shebang for Nixos usage

# use real access token, use SAME token that was used in real Github operations via PyGithub library
TOKEN='GITHUB_REPO_TOKEN'
import requests
import json

headers = {
    'Authorization': f'token {TOKEN}',
}

response = requests.get('https://api.github.com/rate_limit', headers=headers)



# Check if the request was successful (status code 200)
if response.status_code == 200:
    # If the content is JSON, you can pretty print it
    try:
        content_json = response.json()
        print(json.dumps(content_json, indent=2))
    except ValueError:
        # If it's not JSON, just print the content as text
        print(response.text)
else:
    print(f"Failed to retrieve rate limit. Status code: {response.status_code}")
    print(response.text)
