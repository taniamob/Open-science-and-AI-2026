import os
from lxml import etree

folder = "data/xml"
abstracts = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    tree = etree.parse(path)
    abs_nodes = tree.xpath("//tei:abstract//text()", namespaces={"tei": "http://www.tei-c.org/ns/1.0"})
    text = " ".join(abs_nodes)
    if text.strip():
        abstracts.append(text)

with open("outcome/abstracts.txt", "w", encoding="utf8") as f:
    for a in abstracts:
        f.write(a + "\n")