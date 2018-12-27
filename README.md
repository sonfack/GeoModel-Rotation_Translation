# Geometry model 
Our ojectif is to determine **R** the *rotation matrix* and **t**
the *translation matrix* such that for all set of points **A** 
taken in the space and represented by a *(N,3)* size with each
having coordinate *(x,y,z)* we can fine the set of of points **B**
such that **B** = **RA + t**.  
To solve this problem, we have a certain number of steps to take:  
1. Calculate the **centroid** of each set of point the space 
ei : **A** and **B**
2. Calculate the **Optimal Rotation** using the **Singular Value
Decomposition**
3. Calculate the **Translation matrix**  

## Calculate the *centroid*
What we call ***centroid*** is the center or the ***average***
point of a set of points.  
The function **def enterPoint(N=4)** is to enter the set of points
The functin **def createCentroid(M)** is to calculate the centroid of a
given set of points in the space.

## Calculate the *Optimal Rotation*
$$ $$
## Calculate the *Translation matrix*

