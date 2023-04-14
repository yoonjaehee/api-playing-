import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
excel = pd.read_excel('C:\\Users\\ytjh0\\Desktop\\api.xlsx', header=None)
excel = excel.drop(index=0)
excel = excel.drop(index=1)
excel = excel.drop(index=2)
excel = excel.drop(columns=[0,1,2,3,4,5,6,7,8,9,10,11,12])
excel = excel[::-1]
for i in range(0, 6):
    excel = excel.rename(columns={i+13: i+1})
excel = excel.rename(columns={19: 'bonus'})
excel.index = [i for i in range(1,len(excel)+1)]
excel.head()
excel.to_csv('C:\\Users\\ytjh0\\Desktop\\lotto.csv')
apt = pd.DataFrame(excel)
excel.insert(0,'num',1)
for i in range(1,len(excel)+1):
    excel.loc[i,'num'] = i
print(excel)
x=excel['num']
y1=excel[1]
y2=excel[2]
y3=excel[3]
y4=excel[4]
y5=excel[5]
y6=excel[6]
ybo=excel['bonus']
pre_num1 = LinearRegression()
pre_num1.fit(x.values.reshape(-1,1),y1)
ans1=pre_num1.predict([[len(excel)+1]])[0]

pre_num2 = LinearRegression()
pre_num2.fit(x.values.reshape(-1,1),y2)
ans2=pre_num2.predict([[len(excel)+1]])[0]
plt.plot(x,y1,'o')
plt.show()

pre_num3 = LinearRegression()
pre_num3.fit(x.values.reshape(-1,1),y3)
ans3=pre_num3.predict([[len(excel)+1]])[0]

pre_num4 = LinearRegression()
pre_num4.fit(x.values.reshape(-1,1),y4)
ans4=pre_num4.predict([[len(excel)+1]])[0]

pre_num5 = LinearRegression()
pre_num5.fit(x.values.reshape(-1,1),y5)
ans5=pre_num5.predict([[len(excel)+1]])[0]

pre_num6 = LinearRegression()
pre_num6.fit(x.values.reshape(-1,1),y6)
ans6=pre_num6.predict([[len(excel)+1]])[0]

pre_num7 = LinearRegression()
pre_num7.fit(x.values.reshape(-1,1),ybo)
ans7=pre_num7.predict([[len(excel)+1]])[0]

this_week=[]
this_week.append(int(round(ans1,0)))
this_week.append(int(round(ans2,0)))
this_week.append(int(round(ans3,0)))
this_week.append(int(round(ans4,0)))
this_week.append(int(round(ans5,0)))
this_week.append(int(round(ans6,0)))
this_week.append(int(round(ans7,0)))
print(this_week)
