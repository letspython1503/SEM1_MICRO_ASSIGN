import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"D:\Vcode\SEM1_MICRO_ASSIGN\COVID2020.csv")
print(data.describe())
print(data)
sns.histplot(data['Change'], kde=True)
plt.title('Distribution of NIFTY 500 index changes in %')
plt.show()
