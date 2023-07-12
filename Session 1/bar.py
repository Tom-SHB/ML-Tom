import matplotlib.pyplot as plt

products = ["product1","product2","product3","product4"]
sales = [320,123,500,652]

plt.bar(products,sales,color = ["red","green","cyan","blue"])
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()
