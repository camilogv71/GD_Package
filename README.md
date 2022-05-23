# Gradient Descent Package
This is a package for the gradient descent algorithm without the use of a third-party solver.

# Installation

Run the command ´python setup.py install´ on the main folder

# Initial Parameters

The class 'GDOptProblem' takes as input the maximum iterations, learning rate and tolerance for the gradient descent algorithms. If none are given, the following default values are assumed:

* Max number of iterations = 800
* Learning rate = 0.01
* Tolerance = 0.0001

The function 'solve' takes as input the seed values for x1 and x2. The 'evaluate_Func' function within the 'GDOptProblem' can be changed in order to optimize a different function.
