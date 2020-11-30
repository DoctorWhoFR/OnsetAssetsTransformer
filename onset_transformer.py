import re
import json 

configs_file = open('configs.json', 'r')
configs = configs_file.read();
configs_file.close();

# parse x:
y = json.loads(configs)

path = y['Path']

folder_path = y['Folder_path']


final_path = path + folder_path

regex = r"[src,href]{3,4}=\"([A-z/ .]{1,})\""

index_file = open('index.html', 'r+')
index_content = index_file.read()
index_file.close()

matches = re.finditer(regex, index_content, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

    file_name = final_path + match.group(1)

    index_content = index_content.replace(match.group(1), file_name)
    print(index_content)
    print(file_name)

print('end')

fin = open("index.html", "wt")
fin.write(index_content)
fin.close()

