#豆瓣电影Top250每个评分段中电影的数量条形图
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

#设置中文显示
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 读取Excel文件
df = pd.read_excel("豆瓣电影Top250.xls")

# 创建评分段
bins = [0, 8.5, 9.0, 9.5, 10.0]
labels = ['8.0-8.5', '8.6-9.0', '9.1-9.5', '9.6-10.0']

# 将数据分组并统计数量
df['Rating Segment'] = pd.cut(df['评分'].astype(float), bins=bins, labels=labels, include_lowest=True)
rating_counts = df['Rating Segment'].value_counts()

# 绘制条形图
plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette='pastel')

# 为条形图添加注释
for i, count in enumerate(rating_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')

# 旋转x轴标签
plt.xticks(rotation=45)

plt.xlabel('评分段')
plt.ylabel('电影数量')
plt.title('不同评分段电影数量分布')
plt.show()
