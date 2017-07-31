import json
import os
import sys
from urllib import request
def get_recursive_file_list(path):
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        all_files.append(full_file_name)
    return all_files
jsonfile=get_recursive_file_list(".//coolshow//.json_data_cache")
print(jsonfile)
url1=[]
i=0
for file in jsonfile:
    f = open(file, encoding='utf-8')
    x=f.read()
    setting = json.loads(x)
    x=setting.get('themes','0')
    if(x=="0"):
        print("not exit")
    else:
        for a in x:
            print(a["name"])
            print( a["cpid"])
            print(a["md5"])
            url1.extend([["http://d.res.zhuti.qiku.com/bucket/themes/"+a["md5"]+".theme"]])
            url1[i].append((a["cpid"]))
            url1[i].append((a["name"]))
            i=i+1
f.close()
print(url1)
for url1 in url1:
    url = url1[0]
    print(url)
    filename = str(url1[1]) + ".theme"
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://d.res.zhuti.qiku.com',
        'Connection': 'keep-alive'
    }
    req = request.Request(url, headers=headers)
    print(filename)
    req = request.urlopen(req)
    print(req)
    with open("./data/" + filename, 'wb') as f:
        f.write(req.read())
    f.close()
