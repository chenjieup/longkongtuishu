import pandas as pd
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
'''
lie
'''
df = pd.read_csv('F:\longkongtuishu\shuju.csv',encoding="utf-8",low_memory=False)
obj = pd.DataFrame(df)
try:
    with open("douban.txt","w") as f:
        for i in obj['name']:
            li = str(i).split(',')
            print(li)
            for i in li:
                if i != 'nan':
                    f.write(i+' ')
                    print(i)
    f.close()
except:
     pass
abel_mask = plt.imread(r'F:\longkongtuishu\timeee.jpg')
f = open(u'douban.txt','r').read()
stopwords = set(STOPWORDS)
stopwords.add("font")
font = r'C:\Windows\Fonts\simfang.ttf'
wordcloud = WordCloud(background_color="white",
                      mask=abel_mask,
                      font_path=font,
                      stopwords = stopwords,
                      margin=2,
                      max_font_size = 40,
                      ).generate(f)
# img_colors = ImageColorGenerator(abel_mask)
# wordcloud.recolor(color_func=img_colors)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()