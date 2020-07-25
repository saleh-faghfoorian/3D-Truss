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

## Developers
* **Saleh Faghfoorian** [Saleh Faghfoorian](https://github.com/saleh-faghfoorian)
