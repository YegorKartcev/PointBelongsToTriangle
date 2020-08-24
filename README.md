# PointBelongsToTriangle

![](/images/img1.JPG)

Given three points (A, B, C with coordinates) which form a triangle. The task is to determine whether another point D lies inside or outside of the triangle.

How to approach this?
Let’s connect point D to the other apexes. Now we have three more triangles: ABD, BCD and ACD. If D is within the main triangle ABC, then sum of footprints of constructive triangles will be equal to the footprint of ABC. If not - the sum will be bigger.
Having that in mind, how to get an area of the triangle with given apexes? 
From linear algebra we know that two vectors originating from the same point can be represented as a matrix. in this case 2x2 matrix. The matrix has a determinant which essentially represents an area of rectangular formed by those vectors. In our case we need to cut the area in half to get the triangle footprint.
![](/images/img2.JPG)

Let’s apply it to the original problem.
We have a triangle within a given coordinate system. Let’s shift the origin to point D and apply the principle described earlier. Here is the example of function which does the job and calculates a footprint of DADB triangle. The final script will be linked in the video description.
![](/images/img3.JPG)

Run the script and have a look at its output.
The initial set of coordinates is changed with respect to the new origin at point D and area of each individual constructive triangle was calculated and summed  as 3.0, which is equal to area of the main triangle ABC. Thus, it states that point D lies within the main triangle.
![](/images/img4.JPG)

Let’s change coordinates of point D a little and see the result.
The sum of constructive triangle areas is bigger than the ABC area. The point lies outside of the triangle.
![](/images/img5.JPG)

The script works, but it’s not convenient for users. People are used to common window interface and stay away from this kind of script-like applications.
And here is how it looks. Now we let user to easily change any of the initial coordinates and press the button to run the script behind the scene.
![](/images/img6.JPG)

The output is same as before, have in mind that user input can be incorrect and you need to prevent program crash.
![](/images/img7.JPG)

