import matplotlib.pyplot as plt

products = ["Category A","Category B","Category C","Category D","Category E"]
sales = [10,20,30,40,10]

explode = [0,0.1,0,0,0.4] 
colors = ["brown","gray","cyan","wheat","green"]

plt.pie(sales,explode = explode,labels= products,colors = colors,shadow = True)

plt.title("Percentage Distribution")
plt.legend(products)
plt.show()
