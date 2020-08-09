# 3D-Truss
You can solve every 3D Truss problem easily ! :sunglasses:
This is a program for solving every 3D truss problem. This solving method is based on deformation of the elements of the truss.
This is a project done by Saleh Faghfoorian, mechanical engineering undergraduate student at Sharif University of Technology.

## Nodes File's Format (Input)
you should enter your nodes information in this format :
```
1st Column : number of the node
2nd Column : x component of position of the node (in the cartesian coordinate system x-y)
3rd Column : y component of position of the node (in the cartesian coordinate system x-y)
4rd Column : z component of position of the node (in the cartesian coordinate system x-y)
5th Column : x component of Force applied on the node
6th Column : y component of Force applied on the node
7th Column : z component of Force applied on the node
8th Column : x component of constraint of the node (0 for no restriction , 1 for restricion in displacement)
9th Column : y component of constraint of the node (0 for no restriction , 1 for restricion in displacement)
10th Column : z component of constraint of the node (0 for no restriction , 1 for restricion in displacement)
```
## Elements File's Format (Input)
you should enter your elements information in this format :
```
1st Column : number of the element
2nd Column : number of node on the buttom of the element
3rd Column : number of node on the top of the element
4th Column : area of the element
5th Column : material number of the element
```

## Material File's Format (Input)
```
1st Column : number of the material type
2nd Column : Young's modulus of the material
3rd Column : Yield Strength of the material
```
* Now you just need to run the code (like 2D mode)
* Job's done! :sunglasses:
* Now you have a report which tells you the forces, displacements, stresses, and the factor of safety.
* Also you have 2 diagrams.
* 1st diagram is the truss view in (3D cartesian coordinate system)
* 2nd diagram is the force of each element.(elements which haven't diagram, are zero members)


## Sample

![Sample Image](http://8upload.ir/uploads/f515952344.png)
Report :
```
Element Number		   Force(N)		Force-Type	     Displacement	      Stress			  FS
0			   1860.43 N		Tension			0.00 mm		      0.25 MPa			947.36
1			   2334.25 N		Tension			0.00 mm		      0.31 MPa			755.06
2			  11337.13 N		Tension			0.01 mm		      1.51 MPa			155.46
3			  15531.81 N		Compression		0.01 mm		      2.07 MPa			113.48
4			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
5			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
6			   1555.70 N		Tension			0.00 mm		      0.21 MPa			1132.93
7			   4034.40 N		Tension			0.00 mm		      0.54 MPa			436.87
8			   6204.43 N		Compression		0.00 mm		      0.83 MPa			284.07
9			   5436.28 N		Compression		0.00 mm		      0.72 MPa			324.21
10			  17932.20 N		Compression		0.01 mm		      2.39 MPa			98.29
11			  45937.58 N		Compression		0.04 mm		      6.13 MPa			38.37
12			  20000.00 N		Tension			0.01 mm		      2.67 MPa			88.12
13			  17653.31 N		Tension			0.02 mm		      2.35 MPa			99.84
14			   7517.22 N		Tension			0.01 mm		      1.00 MPa			234.46
15			  10630.96 N		Compression		0.01 mm		      1.42 MPa			165.79
16			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
17			  38915.23 N		Tension			0.04 mm		      5.19 MPa			45.29
18			  27517.22 N		Compression		0.02 mm		      3.67 MPa			64.05
19			   1555.70 N		Compression		0.00 mm		      0.21 MPa			1132.93
20			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
21			   1860.43 N		Tension			0.00 mm		      0.25 MPa			947.36
22			   2334.25 N		Tension			0.00 mm		      0.31 MPa			755.06
23			  11337.13 N		Tension			0.01 mm		      1.51 MPa			155.46
24			  15531.81 N		Compression		0.01 mm		      2.07 MPa			113.48
25			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
26			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
27			   1555.70 N		Tension			0.00 mm		      0.21 MPa			1132.93
28			   4034.40 N		Tension			0.00 mm		      0.54 MPa			436.87
29			   6204.43 N		Compression		0.00 mm		      0.83 MPa			284.07
30			   5436.28 N		Compression		0.00 mm		      0.72 MPa			324.21
31			  17932.20 N		Compression		0.01 mm		      2.39 MPa			98.29
32			  45937.58 N		Compression		0.04 mm		      6.13 MPa			38.37
33			  20000.00 N		Tension			0.01 mm		      2.67 MPa			88.13
34			  17653.31 N		Tension			0.02 mm		      2.35 MPa			99.84
35			   7517.22 N		Tension			0.01 mm		      1.00 MPa			234.46
36			  10630.96 N		Compression		0.01 mm		      1.42 MPa			165.79
37			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
38			  38915.23 N		Tension			0.04 mm		      5.19 MPa			45.29
39			  27517.22 N		Compression		0.02 mm		      3.67 MPa			64.05
40			   1555.70 N		Compression		0.00 mm		      0.21 MPa			1132.93
41			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
42			  17932.20 N		Compression		0.01 mm		      2.39 MPa			98.29
43			   5436.28 N		Compression		0.00 mm		      0.72 MPa			324.21
44			   6204.43 N		Compression		0.00 mm		      0.83 MPa			284.07
45			   4034.40 N		Tension			0.00 mm		      0.54 MPa			436.87
46			   1277.09 N		Compression		0.00 mm		      0.17 MPa			1380.09
47			   4034.40 N		Tension			0.00 mm		      0.54 MPa			436.87
48			   6204.43 N		Compression		0.00 mm		      0.83 MPa			284.07
49			   5436.28 N		Compression		0.00 mm		      0.72 MPa			324.21
50			  17932.20 N		Compression		0.01 mm		      2.39 MPa			98.29
51			   4606.24 N		Tension			0.00 mm		      0.61 MPa			382.63
52			   5201.34 N		Tension			0.00 mm		      0.69 MPa			338.85
53			   2304.80 N		Tension			0.00 mm		      0.31 MPa			764.71
54			    432.60 N		Tension			0.00 mm		      0.06 MPa			4074.20
55			   6514.20 N		Compression		0.01 mm		      0.87 MPa			270.56
56			    841.61 N		Compression		0.00 mm		      0.11 MPa			2094.21
57			   2417.87 N		Compression		0.00 mm		      0.32 MPa			728.95
58			   1806.08 N		Tension			0.00 mm		      0.24 MPa			975.87
59			   6514.20 N		Compression		0.01 mm		      0.87 MPa			270.56
60			    841.61 N		Compression		0.00 mm		      0.11 MPa			2094.21
61			   2417.87 N		Compression		0.00 mm		      0.32 MPa			728.95
62			   1806.08 N		Tension			0.00 mm		      0.24 MPa			975.87
63			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
64			    621.85 N		Compression		0.00 mm		      0.08 MPa			2834.28
65			   3627.94 N		Compression		0.00 mm		      0.48 MPa			485.81
66			   1057.68 N		Tension			0.00 mm		      0.14 MPa			1666.39
67			   3918.83 N		Tension			0.00 mm		      0.52 MPa			449.75
68			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
69			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
70			    774.75 N		Tension			0.00 mm		      0.10 MPa			2274.92
71			    104.68 N		Tension			0.00 mm		      0.01 MPa			16837.40
72			   5026.00 N		Tension			0.00 mm		      0.67 MPa			350.68
73			   6521.78 N		Compression		0.01 mm		      0.87 MPa			270.25
74			    979.71 N		Tension			0.00 mm		      0.13 MPa			1799.00
75			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		
76			    774.75 N		Tension			0.00 mm		      0.10 MPa			2274.92
77			    104.68 N		Tension			0.00 mm		      0.01 MPa			16837.40
78			   5026.00 N		Tension			0.00 mm		      0.67 MPa			350.68
79			   6521.78 N		Compression		0.01 mm		      0.87 MPa			270.25
80			    979.71 N		Tension			0.00 mm		      0.13 MPa			1799.00
81			      0.00 N		zero member		0.00 mm		      0.00 MPa			----		

The Maximum Stress is =   6.13 MPa

Minimum Fator of Safety for the elements of this truss is = 38.37

Numner of types of materials used in the elements is = 1
```
## Force Diagram

![Sample Image](http://8upload.ir/uploads/f1096174.png)

## Developers
* **Saleh Faghfoorian** [Saleh Faghfoorian](https://github.com/saleh-faghfoorian)
