import matplotlib.pyplot as plt

year = [2010,2012,2014,2016,2018,2020]
population = [8.5,9.1,9.8,10.5,11.2,11.9]

plt.plot(year,population,marker = 'o',linestyle = "--",color = "orange")

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth Owner Year")
plt.show()
