import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# 创建示例数据
data = {
    '客户编号': [1, 2, 3, 4, 5],
    '水果购买数量': [10, 5, 12, 2, 15],
    '食品购买数量': [5, 15, 8, 20, 3],
    '饮料购买数量': [20, 2, 8, 4, 12]
}

df = pd.DataFrame(data)

# 选择要进行聚类的特征
features = df[['水果购买数量', '食品购买数量', '饮料购买数量']]

# 使用K均值聚类，假设要分为3个簇
kmeans = KMeans(n_clusters=3)
kmeans.fit(features)

# 将聚类结果添加到数据框中
df['Cluster'] = kmeans.labels_

# 打印结果
print(df)

# 绘制聚类结果
plt.scatter(df['水果购买数量'], df['食品购买数量'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('水果购买数量')
plt.ylabel('食品购买数量')
plt.show()
