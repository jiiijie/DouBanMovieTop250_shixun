#豆瓣电影Top250评分分布饼图
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 读取 Excel 文件
excel_file_path = "豆瓣电影Top250.xls"
df = pd.read_excel(excel_file_path, sheet_name='豆瓣电影Top250')

# 创建评分段
bins = [8.0, 8.5, 9.0, 9.5, 10.0]
labels = ['8.0-8.5', '8.6-9.0', '9.1-9.5', '9.6-10.0']

# 将数据分组并统计数量
df['Rating Segment'] = pd.cut(df['评分'].astype(float), bins=bins, labels=labels, include_lowest=True)
rating_counts = df['Rating Segment'].value_counts()

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99','#ffcc99','#ff6666'])

# 添加标题
plt.title('豆瓣电影Top250评分占比情况')

# 显示图表
plt.show()
