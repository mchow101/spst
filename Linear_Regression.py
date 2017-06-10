__author__ = 'Bhagat'

import matplotlib.pyplot as plt
from library import mean, product, square, subtract

class line:
    def __init__(self, xs, ys,predict_x=0.0):
        self.xs = xs
        self.ys = ys
        self.predict_x=predict_x
        self.best_fit_slope_and_intercept()
        self.regression_line = [(self.m*x)+self.b for x in xs]
        self.coefficient_of_determination()
        self.predict(self.predict_x)

    def get_xs(self):
        return self.xs

    def get_ys(self):
        return self.ys

    def get_b(self):
        return self.b

    def get_r_squared(self):
        return self.r_squared

    def get_m(self):
        return self.m

    def get_regression_line(self):
        return self.regression_line

    def best_fit_slope_and_intercept(self):
        self.m=( mean(self.xs) * mean(self.ys) - mean(product(self.xs,self.ys))) / (mean(self.xs)**2 - mean(square(self.xs)))
        self.b=mean(self.ys)-self.m*mean(self.xs)

    def squared_error(self,ys_orig, ys_line):
        return sum(square(subtract(ys_line,ys_orig)))

    def coefficient_of_determination(self):
        y_mean_line = [mean(self.ys) for y in self.ys]
        squared_error_regr = self.squared_error(self.ys, self.regression_line)
        squared_error_y_mean = self.squared_error(self.ys, y_mean_line)
        try:
            self.r_squared = 1 - squared_error_regr/squared_error_y_mean
        except ZeroDivisionError:
            self.r_squared = 1

    def graph(self,color='black',size=10,predict_size=100,predict_color='green'):
        plt.scatter(self.xs,self.ys,s=size,color=color)
        plt.plot(self.xs,self.regression_line,color=color)
        plt.title('# of people with disease each year')
        plt.xlabel('year')
        plt.ylabel('# of people with disease')
        if not self.predict_x==0:
            plt.scatter(self.predict_x,self.predict_y, s=predict_size, color=predict_color)
        plt.show()

    def predict(self, predict_x=0.0):
        self.predict_x=predict_x
        self.predict_y = (self.m*self.predict_x)+self.b
        if self.predict_y<0:
            self.predict_y=0
        return self.predict_y

    def clear_predict(self):
        self.predict_x=0
# xs, ys = create_dataset(40,15,2,True)
# graph = line(xs,ys)
# graph.graph()
