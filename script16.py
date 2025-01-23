    headers = {
        'Host': 'projects.scratch.mit.edu',
        'Cookie': 'obviously not sharing this, but I can confirm it is valid and this part does work',
        'Content-Length': '2435',
        'Sec-Ch-Ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
        'Sec-Ch-Ua-Platform': "Linux",
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://scratch.mit.edu',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://scratch.mit.edu/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    payload = {"project payload taken from inspect goes here"}
    url = 'https://projects.scratch.mit.edu/{project_id}'
    resp = requests.put(url, headers = headers, data = payload)
    print(resp)
    }
