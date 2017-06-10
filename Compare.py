__author__ = 'Bhagat'
import matplotlib.pyplot as plt
def compare(lines,colors,size=10):
    if len(lines) != len(colors):
        return None
    for x in range(len(colors)):
        plt.scatter(lines[x].get_xs(),lines[x].get_ys(),color=colors[x])
        plt.plot(lines[x].get_xs(),lines[x].get_regression_line(),color=colors[x])
    plt.title('# of people with disease each year')
    plt.xlabel('Year')
    plt.ylabel('# of people with disease')
    plt.show()
