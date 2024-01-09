# 豆瓣电影Top250评分箱线图
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# 设置中文显示
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 读取 Excel 文件
excel_file_path = "豆瓣电影Top250.xls"
df = pd.read_excel(excel_file_path, sheet_name='豆瓣电影Top250')

# 绘制评分的箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['评分'], color='skyblue')
plt.title('豆瓣电影Top250评分箱线图')
plt.xlabel('评分')
plt.show()




