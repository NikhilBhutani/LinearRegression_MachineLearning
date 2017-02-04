from numpy import *


 def compute_error_for_line_given_points(b, m, points):

 	  # initialize it a 0
 	  totalError = 
 	  # for every point 
 	  for i in range(0, len(points)):
 	  	  # get the x value
 	  	  x = points[i, 0]
 	  	  # get the y value
 	  	  y = points[i, 1]
          # get the difference, square it and add it to the total
          totalError += (y-(m*x +b)) **2
          
          # get the average 
          return totalError / float(len(points))





 def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
 	# starting b and m
 	b = starting_b
 	m = starting_m

 	#gradient descent
 	for i in range(num_iterations):
 		#update b and m with new more accurate b and m by performing
 		#this gradient step
 		b, m = step_gradient(b, m, array(points), learning_rate)

 	#Once this gradient descent is done, we are going to return is optimal b and m
 	return [b, m]


 def step_gradient(b_current, m_current, points, learningRate):

     # These are starting points for our gradients and gradient means slope.
     # Gradient is going to act like a compass and its going to always point down the hill. Once we calculate the error, its going to act as a compass for us.
     # Its going to tell us, where we should be going, What direction we should be going.
     b_gradient = 0
     m_gradient = 0

      N = float(len(points))

     for i in range(0, len(points)):
     	x = points[i, 0]
     	y = points[i, 1]

     	 #direction with respect to b and m, this is the last part but its very imp one, and this where calculas comes into play
     	 #computing partial derivatives of our error functions 
     	   b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
           m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    
    #Update our b and m values using our partial derivatives
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    
    return [new_b, new_m]



 	


 def run(): 

 	 #Step 1 - collect our data
 	 #genfromtext Its going to get the data point from our data file.
 	 #points is going to take bunch of xy value pairs.
 	 # Where x is amount of hours studied, and y is the test score and its seperated by the commas.
     # genfromtext is generally running two main loops. The first loop converts each line to a sequence of strings. And the second one is converting each string to
     # the appropriate data type.
     points = genfromtext('data.csv', delimiter=",");

     #Step 2 - define our hyperparameters.
     # In machine learning, these are tuning nuts for our model. They are basically the paramaters that define how our model is analyzing certain data.
     # How fast its spinning through the data. What operations performing on the data.
     #Learning Rate - defines how fast should our model converge, Convergence is a word for optimal result, the line of best fit in case of linear regression.
     #IF the learning  rate is too small, we are going to get slow convergence. But if its too big, then our error function might not decrease, so it might not
     # converge.

     learning_rate = 0.0001
     
     # here we calculate the slope
     # y = mx+b

     initial_b = 0
     initial_m = 0

     #number of iteration, how much do we train this model?

     num_iterations = 1000

     #Step 3 - train our model

     # So In this line, we're going to show the starting b value, the starting m value, so what is our starting y-intercept, what is our starting slope. 
     # And, what is our starting error?  And to get that error, given our b and m values, we have this function here called compute_error_for_line_given_points.
     # It is going to take the b, m and the points, and its going to compute the error for that and its going to output that.
     print 'starting gradient descent at b= {0}, m = {1}, error = {2}'.format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))

     # Now we are going to perform our gradient descent, and its going to give us the optimal slope and the optimal y descent.
     # For gradient descent, we are going to call this method gradient_descent_runner
     # This is where we are actually training our model, these paramters are all the things we need
     [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)

     # ending point, where b is 2, m is 2 and then error is 3
     print 'starting gradient descent at b= {2}, m = {2}, error = {3}'.format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))
 

if __name__ == '__main__':
	run()