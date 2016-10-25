# Ben Girone 10/24/16
# This script uses numerical integration to approximate a double integral

# sample point is the upper right corner of each rectangle

# edit this to change the function being used
z = lambda x,y: 1 - (x * (y * y)) # z = f(x,y)

# edit this to change the domain of x and y
Rx = [0,4] 
Ry = [-1,2]

# edit this to change the precision of the approximation
m = 2
n = 3

# edit this to change the sample point location
sampleType = "top L" # Options = "top R", "top L", "bottom R", "bottom L", "mid"

### Do Not Edit Beyond This Comment ###

deltaX = (Rx[1] - Rx[0])/m # calculate the change in x
deltaY = (Ry[1] - Ry[0])/n # calculate the change in y

# function to approximate 
def summation(m, n, dX, dY, R, f):
    
    # variable declaration
    x_ij = 0
    y_ij = 0
    sum = 0

    # perform the summation
    for i in range (0, m):
        x_ij = R[0] - (i * dX)

        for j in range (0, n):
            y_ij = R[1] - (j * dY)
            sum = sum + f(x_ij,y_ij) * (dX * dY)

    return sum

#function to find sample points for sub-rectangles
def samplePoint(type, x,  y, dX, dY):
    if (type == 'mid'):
        x = (x + (x - dX))/2
        y = (y + (y - dY))/2
    elif (type == 'top R'):
        x = x
        y = y
    elif (type == 'top L'):
        x = x - dX
        y = y
    elif (type == 'bottom R'):
        x = x
        y = y - dY
    elif (type == 'bottom L'):
        x = x - dX
        y = y - dY
    else:
        print ('ERROR: You did not enter a valid input for the sample point')

    return [x, y]

print(summation(m,n,deltaX,deltaY,samplePoint(sampleType, Rx[1], Ry[1], deltaX, deltaY),z))
