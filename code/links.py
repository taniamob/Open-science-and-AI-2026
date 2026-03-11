import os
import re

folder = "data/xml"
pattern = r'https?://\S+'

with open("outcome/links.txt", "w", encoding="utf8") as output:
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        text = open(path, encoding="utf8").read()
        links = re.findall(pattern, text)
        output.write(file + "\n")
        for link in links:
            output.write(link + "\n")
        output.write("\n")