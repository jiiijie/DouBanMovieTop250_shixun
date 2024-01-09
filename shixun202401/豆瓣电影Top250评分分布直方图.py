# 豆瓣电影Top250评分分布直方图
import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置中文显示
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

def plot_rating_distribution(dataframe):
    # 提取评分数据并转换为浮点型
    ratings = dataframe['评分'].astype(float)

    # 创建图表
    plt.figure(figsize=(10, 6))

    # 使用Seaborn的distplot绘制直方图和核密度估计曲线
    sns.distplot(ratings, bins=10, color='skyblue', kde=True, hist_kws={'edgecolor': 'black', 'alpha': 0.7})

    # 添加标题和标签
    plt.title('豆瓣电影Top250评分分布')
    plt.xlabel('评分')
    plt.ylabel('密度')

    # 显示图表
    plt.show()

if __name__ == "__main__":
    # 读取 Excel 表的数据
    excel_file_path = "豆瓣电影Top250.xls"
    movie_data = pd.read_excel(excel_file_path)

    # 调用绘制评分分布的函数
    plot_rating_distribution(movie_data)
