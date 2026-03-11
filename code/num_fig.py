import os
from lxml import etree
import matplotlib.pyplot as plt

folder = "data/xml"

names = []
counts = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    tree = etree.parse(path)
    figures = tree.xpath("//tei:figure", namespaces={"tei": "http://www.tei-c.org/ns/1.0"})
    names.append(file)
    counts.append(len(figures))

plt.bar(names, counts)
plt.xticks(rotation=90)
plt.ylabel("Number of Figures")
plt.tight_layout()
plt.savefig("outcome/num_figures.png")