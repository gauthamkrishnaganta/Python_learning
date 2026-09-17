'''
Matplotlib:
-----------
--> This is an Python library used to create graphs and charts
--> Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Installation of Matplotlib:
----------------------------
--> If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

Install it using this command --> C:\Users\Your Name>pip install matplotlib

plot()
------
--> This function can create a line graphs with given data
xlabel()
--------
--> Used to represent the x-axis values
ylabel()
---------
--> Used to represent the y-axis values
title()
--------
--> to define the title of the graph
pie()
------
--> Used to create pie charts
legend()
--------
--> This is used to display a legend on a plot. A legend identifies which plotted data corresponds to which label.
grid()
-------
--> function to add grid lines to the plot.
subplot()
---------
--> function you can draw multiple plots in one figure
scatter()
---------
--> function to draw a scatter plot.
--> The scatter() function plots one dot for each observation.
bar():
------
--> function to draw bar graphs.
barh():
-------
--> If you want the bars to be displayed horizontally instead of vertically, use the barh()
hist():
-------
--> hist() function to create histograms
--> The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.


import matplotlib.pyplot as plt

marks = [85,87,90,95,100]
students = ['prasad','gautham','krishna','sandeep','bunny']
#plt.plot(students,marks,color='red')
plt.barh(students,marks,color='red')
plt.title('Students_marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()


import matplotlib.pyplot as plt
subjects = ['python','java','c']
students = [45,25,36]
plt.pie(students,labels=subjects)
plt.title('Total Students')
plt.legend(subjects)
plt.show()

import matplotlib.pyplot as plt
subjects = ['python','java','c']
marks = [45,25,36]
plt.scatter(subjects,marks)
plt.xlabel('student_marks')
plt.ylabel('students')
plt.show()

import matplotlib.pyplot as plt
sales = [800,400,950,1200]
plt.hist(sales)
plt.title('sales_hist')
plt.xlabel('sales')
plt.ylabel('Frequency')
plt.show()

import matplotlib.pyplot as plt
sales = [800,400,950,1200]
plt.boxplot(sales)
plt.show()

'''
