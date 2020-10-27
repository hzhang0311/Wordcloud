import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import jieba as jb
from wordcloud import WordCloud, STOPWORDS

# 设只mpl图像输出像素
mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
mpl.rcParams['font.size']=12                #10
mpl.rcParams['savefig.dpi']=900             #72
mpl.rcParams['figure.subplot.bottom']=.1

# 导入数据
data = pd.read_csv("D:/INTERN/赢商网数据/赢商网-要闻-项目-2020.csv")
stopwords = set(STOPWORDS)
font = r'C:\Windows\Fonts\simyou.TTF'

# 将词条分段
def cut(text):
    word_list = jb.cut(text,cut_all= True)
    result = " ".join(word_list)
    return result

text = cut(str(data['标题']))

# 词云图绘制
wordcloud = WordCloud(
                          font_path=font,
                          background_color='white',
                          stopwords=stopwords,
                          max_words=4000,
                          max_font_size=60,
                          random_state=42
                         ).generate(text)

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=900)
