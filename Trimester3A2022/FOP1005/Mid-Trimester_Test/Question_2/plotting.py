import matplotlib.pyplot as plt

# Add the required packages to make the program work.
Names1 = ['part_1', 'part_2', 'part_3']
Values1 = [1, 10, 100]

plt.figure(figsize=(10, 10))
plt.subplot(131)
# add code here for plotting a scatterplot using Names1 and Values1
plt.scatter(Names1, Values1)

plt.subplot(132)
# add code here for plotting bar using Names1 and Values1
plt.bar(Names1, Values1)
plt.subplot(133)
# add code here to make line plot with Names1 and Values1
plt.plot(Names1, Values1)
plt.suptitle('Different types of plotting')

# add the code here to save the figure with name “Display.png”
plt.savefig('Display.png')
plt.show()
