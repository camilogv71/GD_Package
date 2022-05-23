"""
Created on Sun May 22 19:07:37 2022

@author: Juan Camilo Gonzalez Vélez
"""
import numpy as np
import math as mt

class OptimizationProblem:
    """Base Optimization Problem"""
    def __init__(self, max_iterations, learning_rate, tolerance): 
        """Class initialization.

        Keyword arguments:
        max_iterations -- Maximum number of iterations 
        learning_rate -- Learning rate for Gradient Descent 
        tolerance -- Tolerance stopping criteria 
        """
        self.max_iterations = max_iterations
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        
    def evaluate_Jacobian(self, x_1, x_2):
        """Evaluate the Jacobian of the function. Used in the inherited class

        Keyword arguments:
        x_1 -- x1 value in which the Jacobian is evaluated
        x_2 -- x2 value in which the Jacobian is evaluated
        """
        pass
       
    def solve(self, x_1, x_2):
        """Optimize the function with the gradient descent algorithm.

        Keyword arguments:
        x_1 -- Seed value for the x1 variable
        x_2 -- Seed value for the x2 variable
        """
        print_format = "{:.6f}"
        updated_value = np.array([[x_1],[x_2]])
        print('Starting value: (' 
              + str(print_format.format(updated_value[0][0])) 
              + ',' + str(print_format.format(updated_value[1][0])) + ')')
        for iteration in range(self.max_iterations):
            Jacobian = self.evaluate_Jacobian(updated_value[0][0],
                                              updated_value[1][0])
            step = self.learning_rate*Jacobian    #Jacobian calculation
            norm = np.linalg.norm(step)
            if norm < self.tolerance:    #Tolerance check
                print('The solution is (x1,x2) = (' 
                      + str(print_format.format(updated_value[0][0]))
                      + ',' + str(print_format.format(updated_value[1][0]))
                      + '). Stopping criteria = Tolerance (' 
                      + str(self.tolerance) + ')')
                return updated_value
            updated_value = updated_value - step    #Update step
            function_value = self.evaluate_Func(updated_value[0][0], 
                                                updated_value[1][0])
            print('Running iteration ' + str(iteration+1)
                  + '...Current (x1,x2) value = (' 
                  + str(print_format.format(updated_value[0][0]))
                  + ',' + str(print_format.format(updated_value[1][0])) 
                  + '), f(' + str(print_format.format(updated_value[0][0]))
                  + ',' + str(print_format.format(updated_value[1][0])) 
                  + ') = ' + str(print_format.format(function_value)) 
                  + ', Residual = ' + str(print_format.format(norm)))
        print('The solution is (x1,x2) = (' 
              + str(print_format.format(updated_value[0][0]))
              + ',' + str(print_format.format(updated_value[1][0]))
              + '). Stopping criteria = Number of iterations ('
              + str(iteration+1) + ')')
        return updated_value

class GDOptProblem(OptimizationProblem):
    """Specific Optimization Problem with default values"""
    def __init__(
            self, max_iterations=800, learning_rate=0.01, 
            tolerance=0.0001):
        """Class initialization with default values.

        Keyword arguments:
        max_iterations -- Maximum number of iterations (default 800)
        learning_rate -- Learning rate for Gradient Descent (default 0.01)
        tolerance -- Tolerance stopping criteria (default 0.0001)
        """
        OptimizationProblem.__init__(self, max_iterations, 
                                     learning_rate, tolerance)
        
    def evaluate_Func(self, x_1, x_2):
        """Evaluate the optimized function .

        Keyword arguments:
        x_1 -- x1 value in which the function is evaluated
        x_2 -- x2 value in which the function is evaluated
        """
        f1 = mt.pow((mt.pow(x_1, 2) + x_2 - 3), 2)
        f2 = mt.pow((x_1 + mt.pow(x_2, 2) - 9), 2)
        Function = f1 + f2
        return Function
    
    def evaluate_Jacobian(self, x_1, x_2):
        """Evaluate the Jacobian of the function.

        Keyword arguments:
        x_1 -- x1 value in which the Jacobian is evaluated
        x_2 -- x2 value in which the Jacobian is evaluated
        """
        h = 0.001    # Differentiation step
        Jacobian = np.array([[(self.evaluate_Func(x_1 + h, x_2) 
                             - self.evaluate_Func(x_1 - h, x_2))/(2*h)],
                             [(self.evaluate_Func(x_1, x_2 + h) 
                             - self.evaluate_Func(x_1, x_2 - h))/(2*h)]])
        return Jacobian

default_problem = GDOptProblem()
default_problem.solve(0, 0)
