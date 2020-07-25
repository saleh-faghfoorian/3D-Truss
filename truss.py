import numpy as np                          # Done By Saleh, Email : saleh.faghfoorian@gmail.com , github.com/saleh-faghfoorian
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

                                            
Mat_types = 0                               # This project is coded to solve each 3D truss problem (completely general)
N         = 0
M         = 0

#-------------------------------------------------------------------------------------------------------------------------

materials  = []
nodes     = []
elements  = []
ex_forces = []
FS        = []        
STR       = []
disp      = []
x_p       = []
y_p       = []
z_p       = []

#-------------------------------------------------  Definition of Classes  ------------------------------------------------


class material:                                     # defining material
    def __init__(self, number, E, S_y):
        self.number = number
        self.E = E
        self.S_y = S_y


class node:                                         # defining node
    def __init__(self, number, x, y, z, f_e_x, f_e_y, f_e_z, constraint_x, constraint_y, constraint_z):
        self.number                = number
        self.x                     = x
        self.y                     = y
        self.z                     = z
        self.f_e_x                 = f_e_x
        self.f_e_y                 = f_e_y
        self.f_e_z                 = f_e_z
        self.constraint_x          = constraint_x
        self.constraint_y          = constraint_y
        self.constraint_z          = constraint_z
        self.u                     = 0.0
        self.v                     = 0.0
        self.w                     = 0.0
        self.elements_connected    = []


class element:                                      # defining element
    def __init__(self, number, node_i, node_j, A, Material):
        self.number   = number
        self.node_i   = node_i
        self.node_j   = node_j
        self.L        = 0.0
        self.A        = A
        self.Material = Material
        self.v_x      = 0.0
        self.v_y      = 0.0
        self.v_z      = 0.0
        self.alpha    = 0.0
        self.beta     = 0.0
        self.gamma    = 0.0
        self.delta    = 0.0
        self.f        = 0.0
        self.stress   = 0.0
        self.FS       = 0.0


#-------------------------------------------------  Drawing Elements  ------------------------------------------------------

def draw_elements(node_1, node_2):
    x_1 = float(nodes[int(node_1)].x)
    y_1 = float(nodes[int(node_1)].y)
    z_1 = float(nodes[int(node_1)].z)
    x_2 = float(nodes[int(node_2)].x)
    y_2 = float(nodes[int(node_2)].y)
    z_2 = float(nodes[int(node_2)].z)
    ax.plot([x_1, x_2], [y_1, y_2], [z_1, z_2], color = 'black')

#-------------------------------------------------  Getting Materials  -----------------------------------------------------

mat = open("./materials.txt","r+")                  # opening material file : properties of the materials
while mat.readline():                               # fining the number of materials used in the elements
    Mat_types += 1
mat.close()
mat = open("./materials.txt","r+")
for i in range(Mat_types):                          # creating a list of materials
    M_list = mat.readline()
    M_list = M_list.split()
    M_i    = material(M_list[0], M_list[1], M_list[2])
    materials.append(M_i)
mat.close()

#-------------------------------------------------  Getting Nodes  ---------------------------------------------------------

nodes_file = open("./nodes.txt","r+")               # opening nodes file : properties of nodes
while nodes_file.readline():                        # finding the number of nodes
    N += 1
nodes_file.close()
nodes_file = open("./nodes.txt","r+")
for i in range(N):                                  # getting nodes from file
    lists  = nodes_file.readline()
    lists  = lists.split()
    node_1 = node(lists[0],lists[1],lists[2],lists[3],lists[4],lists[5],lists[6],lists[7],lists[8],lists[9])
    nodes.append(node_1)
    if int(lists[7]) == 1 :
        nodes[i].u = 0
    if int(lists[8]) == 1 :
        nodes[i].v = 0
    if int(lists[9]) == 1 :
        nodes[i].w = 0
nodes_file.close()

for i in range(N):                                  # creating a vector of external forces
    ex_forces.append(float(nodes[i].f_e_x))
    ex_forces.append(float(nodes[i].f_e_y))
    ex_forces.append(float(nodes[i].f_e_z))

#-------------------------------------------------  Getting Elements  ------------------------------------------------------

elements_file = open("./elements.txt","r+")         # opening elements file : properties of elements
while elements_file.readline():                     # finding the number of elements
    M += 1
elements_file.close()
elements_file = open("./elements.txt","r+")

for i in range(M):                                  # getting elements from file
    list_2            = elements_file.readline()
    list_2            = list_2.split()
    element_1         = element(int(list_2[0]),int(list_2[1]),int(list_2[2]),float(list_2[3]),int(list_2[4]))
    elements.append(element_1)

    elements[i].L     = np.sqrt((float(nodes[elements[i].node_i].x) - float(nodes[elements[i].node_j].x))**2 \
    + (float(nodes[elements[i].node_i].y) - float(nodes[elements[i].node_j].y))**2 \
    + (float(nodes[elements[i].node_i].z) - float(nodes[elements[i].node_j].z))**2)
    

    elements[i].v_x  = float(nodes[elements[i].node_j].x) - float(nodes[elements[i].node_i].x)
    elements[i].v_y  = float(nodes[elements[i].node_j].y) - float(nodes[elements[i].node_i].y)
    elements[i].v_z  = float(nodes[elements[i].node_j].z) - float(nodes[elements[i].node_i].z)


    elements[i].alpha = np.arccos(elements[i].v_x / elements[i].L)
    elements[i].beta  = np.arccos(elements[i].v_y / elements[i].L)
    elements[i].gamma = np.arccos(elements[i].v_z / elements[i].L)


elements_file.close()

for i in range(N):                                  # finding elements are connected to each node
    for j in range(M):                                             
        if int(nodes[i].number) == int(elements[j].node_i) or int(nodes[i].number) == int(elements[j].node_j) :
            nodes[i].elements_connected.append(int(elements[j].number))

C = [[0]*(3*N) for i in range(3*N)]


#-------------------------------------------------  X - Equilibirium  ------------------------------------------------------

for i in range(N):
    for j in range(3*N):  
        if i==j :
            c               = [((-1) * float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
            * (np.cos(float(elements[r].alpha)))**2 / float(elements[r].L)) for r in nodes[i].elements_connected]
            d               = [((-1) * float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
            * np.cos(float(elements[r].alpha)) * np.cos(float(elements[r].beta)) / float(elements[r].L)) \
            for r in nodes[i].elements_connected]
            e               = [((-1) * float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
            * np.cos(float(elements[r].alpha)) * np.cos(float(elements[r].gamma)) / float(elements[r].L)) \
            for r in nodes[i].elements_connected]
            C[3*i][3*i]     = sum(c)
            C[3*i][3*i + 1] = sum(d)
            C[3*i][3*i + 2] = sum(e)
        else :
            for r in nodes[i].elements_connected :
                if int(elements[r].node_i) == i :
                    q = elements[r].node_j
                elif int(elements[r].node_j) == i :
                    q = elements[r].node_i
                C[3*i][3*q]     = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * (np.cos(float(elements[r].alpha)))**2 / float(elements[r].L))
                C[3*i][3*q + 1] = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * np.cos(float(elements[r].alpha)) * np.cos(float(elements[r].beta)) / float(elements[r].L))
                C[3*i][3*q + 2] = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * np.cos(float(elements[r].alpha)) * np.cos(float(elements[r].gamma)) / float(elements[r].L))

#-------------------------------------------------  Y - Equilibirium  ------------------------------------------------------

for i in range(N):
    for j in range(3*N):
        if i == j :
            g_1 = [(-1)*(float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
            * np.cos(float(elements[r].beta)) * np.cos(float(elements[r].alpha)) / float(elements[r].L)) \
            for r in nodes[i].elements_connected]
            g_2 = [(-1)*(float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
            * (np.cos(float(elements[r].beta)))**2  / float(elements[r].L)) for r in nodes[i].elements_connected]
            g_3 = [(-1)*(float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
            * np.cos(float(elements[r].beta)) * np.cos(float(elements[r].gamma)) / float(elements[r].L)) \
            for r in nodes[i].elements_connected]
            C[3*i + 1][3*i]     = sum(g_1)
            C[3*i + 1][3*i + 1] = sum(g_2)
            C[3*i + 1][3*i + 2] = sum(g_3)
        else :
            for r in nodes[i].elements_connected :
                if int(elements[r].node_i) == i :
                    p = elements[r].node_j
                elif int(elements[r].node_j) == i :
                    p = elements[r].node_i
                C[3*i + 1][3*p]     = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * np.cos(float(elements[r].beta)) * np.cos(float(elements[r].alpha)) / float(elements[r].L))
                C[3*i + 1][3*p + 1] = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * (np.cos(float(elements[r].beta)))**2 / float(elements[r].L))
                C[3*i + 1][3*p + 2] = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * np.cos(float(elements[r].beta)) * np.cos(float(elements[r].gamma)) / float(elements[r].L))

#-------------------------------------------------  Z - Equilibirium  ------------------------------------------------------

for i in range(N):
    for j in range(3*N):
            if i == j :
                a = [(-1)*(float(elements[r].A) * float(materials[int(elements[r].Material)].E) * np.cos(float(elements[r].gamma)) \
                * float(np.cos(elements[r].alpha)) / float(elements[r].L)) for r in nodes[i].elements_connected]
                b = [(-1)*(float(elements[r].A) * float(materials[int(elements[r].Material)].E) * np.cos(float(elements[r].gamma)) \
                * np.cos(float(elements[r].beta)) / float(elements[r].L)) for r in nodes[i].elements_connected]
                c = [(-1)*(float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                * (np.cos(float(elements[r].gamma)))**2 / float(elements[r].L)) for r in nodes[i].elements_connected]
                C[3*i + 2][3*i]     = sum(a)
                C[3*i + 2][3*i + 1] = sum(b)
                C[3*i + 2][3*i + 2] = sum(c)
            else :
                for r in nodes[i].elements_connected :
                    if int(elements[r].node_i) == i :
                        p = elements[r].node_j
                    elif int(elements[r].node_j) == i :
                        p = elements[r].node_i
                    C[3*i + 2][3*p]     = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                    * np.cos(float(elements[r].gamma)) * np.cos(float(elements[r].alpha)) / float(elements[r].L))
                    C[3*i + 2][3*p + 1] = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                    * np.cos(float(elements[r].gamma)) * np.cos(float(elements[r].beta)) / float(elements[r].L))
                    C[3*i + 2][3*p + 2] = (float(elements[r].A) * float(materials[int(elements[r].Material)].E) \
                    * (np.cos(float(elements[r].gamma)))**2 / float(elements[r].L))

#-------------------------------------------------  Creating New Matrix  ---------------------------------------------------

for i in range(N):                                  # calculating new Matrix C
    if int(nodes[i].constraint_x) == 1 :
        C[3*i][3*i] = 1
        for k in range(N):
            if (k != i) and (int(nodes[k].constraint_x) == 1) :
                C[3*i][3*k] = 0
            if int(nodes[k].constraint_y) == 1 :
                C[3*i][3*k + 1] = 0
            if int(nodes[k].constraint_z) == 1 :
                C[3*i][3*k + 2] = 0



    if int(nodes[i].constraint_y) == 1 :
        C[3*i + 1][3*i + 1] = 1
        for j in range(N):
            if int(nodes[j].constraint_x) == 1 :
                C[3*i + 1][3*j] = 0
            if (j != i) and (int(nodes[j].constraint_y) == 1) :
                C[3*i + 1][3*j + 1] = 0
            if int(nodes[j].constraint_z) == 1 :
                C[3*i + 1][3*j + 2] = 0
                
    

    if int(nodes[i].constraint_z) == 1 :
        C[3*i + 2][3*i + 2] = 1
        for e in range(N):
            if int(nodes[e].constraint_x) == 1 :
                C[3*i + 2][3*e] = 0
            if int(nodes[e].constraint_y) == 1 :
                C[3*i + 2][3*e + 1] = 0
            if (e != i) and (int(nodes[e].constraint_z) == 1) :
                C[3*i + 2][3*e + 2] = 0


    if int(nodes[i].constraint_x) == 0 :
        for s in range(N):
            if int(nodes[s].constraint_x) == 1 :
                C[3*i][3*s] = 0
            if int(nodes[s].constraint_y) == 1 :
                C[3*i][3*s + 1] = 0
            if int(nodes[s].constraint_z) == 1 :
                C[3*i][3*s + 2] =0



    if int(nodes[i].constraint_y) == 0 :
        for q in range(N):
            if int(nodes[q].constraint_x) == 1 :
                C[3*i + 1][3*q] = 0
            if int(nodes[q].constraint_y) == 1 :
                C[3*i + 1][3*q + 1] = 0
            if int(nodes[q].constraint_z) == 1 :
                C[3*i + 1][3*q + 2] = 0


    if int(nodes[i].constraint_z) == 0 :
        for y in range(N):
            if int(nodes[y].constraint_x) == 1 :
                C[3*i + 2][3*y] = 0
            if int(nodes[y].constraint_y) == 1 :
                C[3*i + 2][3*y + 1] = 0
            if int(nodes[y].constraint_z) == 1 :
                C[3*i + 2][3*y + 2] = 0

#-------------------------------------------------  Solving Matrix Equations  ----------------------------------------------

K = np.linalg.inv(C)                                # inverse of matrix C

for i in range(N):                                  # calculating new Matrix ex_forces
    ex_forces[i] = float(ex_forces[i])
    if int(nodes[i].constraint_x) == 1 :
        ex_forces[3*i] = 0.0
    if int(nodes[i].constraint_y) == 1 :
        ex_forces[3*i + 1] = 0.0
    if int(nodes[i].constraint_z) == 1 :
        ex_forces[3*i + 2] = 0.0


for i in range(3*N):                                # multiplication of Matrices K and ex_forces
    d = [(-1) * K[i][j] * ex_forces[j] for j in range(3*N)]
    disp.append(sum(d))


for i in range(N):                                  # determining all of variables
    if int(nodes[i].constraint_x) == 0 :
        nodes[i].u = disp[3*i]
    if int(nodes[i].constraint_y) == 0 :
        nodes[i].v = disp[3*i + 1]
    if int(nodes[i].constraint_z) == 0 :
        nodes[i].w = disp[3*i + 2]
    if int(nodes[i].constraint_x) == 1 :
        nodes[i].f_e_x = disp[3*i]
    if int(nodes[i].constraint_y) == 1 :
        nodes[i].f_e_y = disp[3*i + 1]
    if int(nodes[i].constraint_z) == 1 :
        nodes[i].f_e_z = disp[3*i + 2]


for i in range(M):                                  # calculating forces, stresses, and Factor of Safety

    delta_u = float(nodes[int(elements[i].node_j)].u) - float(nodes[int(elements[i].node_i)].u)
    delta_v = float(nodes[int(elements[i].node_j)].v) - float(nodes[int(elements[i].node_i)].v)
    delta_w = float(nodes[int(elements[i].node_j)].w) - float(nodes[int(elements[i].node_i)].w)

    elements[i].delta = (delta_u * np.cos(elements[i].alpha)) + (delta_v * np.cos(elements[i].beta)) \
    + (delta_w * np.cos(elements[i].gamma))

    elements[i].f = float(elements[i].A) * float(materials[int(elements[i].Material)].E) * float(elements[i].delta) \
    / float(elements[i].L)

    elements[i].stress = elements[i].f / float(elements[i].A)
    
    if elements[i].stress != 0 :
        elements[i].FS     = np.abs(float(materials[int(elements[i].Material)].S_y) / elements[i].stress)


for k in range(M):                                  # Creating a list for FS and Stresses
    STR.append(np.abs(float(elements[k].stress)))
    if np.abs(float(elements[k].f)) >= 0.000001 :
        FS.append(elements[k].FS)


#-------------------------------------------------  Reporting Results  -----------------------------------------------------


outputs = open("./Report.txt","w+")                 # writing Results in the report file
outputs.write("Element Number\t\t   Force(N)\t\tForce-Type\t     Displacement\t      Stress\t\t\t  FS\n")

for i in range(M):                                  # continuing writing Results
    

    outputs.write(str(elements[i].number))          # writing element number
    outputs.write("\t\t\t")


    if abs(float(elements[i].f)) < 0.000001 :       # writing force
        outputs.write("      0.00")
    else :
        outputs.write("{0:10.2f}".format(np.abs(float(elements[i].f))))
    outputs.write(" N\t\t")


    if abs(float(elements[i].f)) < 0.000001 :       # writing force-type
        outputs.write("zero member\t")
    elif float(elements[i].f) < 0 :
        outputs.write("Compression\t")
    elif float(elements[i].f) > 0 :
        outputs.write("Tension\t\t")
    outputs.write("\t")


    if abs(float(elements[i].delta)) < 0.000001 :   # writing displacement
        outputs.write("0.00 mm")
    else :
        outputs.write("{0:2.2f}".format(np.abs(float(elements[i].delta))))
        outputs.write(" mm")
    outputs.write("\t\t")


    if abs(float(elements[i].stress)) < 0.000001 :  # writing stress
        outputs.write("      0.00 MPa\t")
    else :
        outputs.write("{0:10.2f}".format(np.abs(float(elements[i].stress))))
        outputs.write(" MPa\t")
    outputs.write("\t\t")


    if abs(float(elements[i].f)) < 0.000001 :       # writing factor of safety
        outputs.write("----\t\t")
    else :
        outputs.write("{0:3.2f}".format((np.abs(float(elements[i].FS)))))
    outputs.write("\n")
outputs.write("\n\n")
outputs.write("The Maximum Stress is = ")
outputs.write("{0:6.2f}".format((max(STR))))
outputs.write(" MPa\n\n")
outputs.write("Minimum Fator of Safety for the elements of this truss is = ")
outputs.write("{0:3.2f}".format((min(FS))))
outputs.write("\n\n")
outputs.write("Numner of types of materials used in the elements is = ")
outputs.write(str(Mat_types))
outputs.close()


x_f = [int(elements[i].number) for i in range(M)]
y_f = [float(np.abs(elements[i].f)) for i in range(M)]
for i in range(M):
    plt.plot([x_f[i], x_f[i]], [0, y_f[i]], color = 'b', linestyle = '-', zorder = 5)
plt.xlabel("Element Number")
plt.ylabel("Element Force (N)")
plt.title("Element Force (N)")
plt.savefig("./Force Diagram.png")                 # saving a diagram for forces of each elements


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#-------------------------------------------------  3D Plotting  ----------------------------------------------------------

for i in range(N):
    x_p.append(float(nodes[i].x))
    y_p.append(float(nodes[i].y))
    z_p.append(float(nodes[i].z))


ax.scatter(x_p, y_p, z_p, c='r', marker='o')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')


for i in range(M):
    draw_elements(elements[i].node_i, elements[i].node_j)

plt.savefig("./truss.png")
