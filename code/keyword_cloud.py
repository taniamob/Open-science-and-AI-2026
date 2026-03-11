from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open("outcome/abstracts.txt", encoding="utf8").read()

wc = WordCloud(width=1000, height=500).generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("outcome/keyword_cloud.png")