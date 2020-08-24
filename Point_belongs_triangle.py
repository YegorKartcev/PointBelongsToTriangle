
import matplotlib.pyplot as plt

A = [1, 0]
B = [0, 3]
C = [3, 0]
D = [2, 2]

print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)

print("\nMove the origin to D\nand calculate areas of\nconstructive triangles:\n")
 
#To deal with: DAB, DAC, DBC
def getDADB(A, B, C, D):
    #For DA and DB vectors:
    #New A coord: B(Xa-Xd; Ya-Yd)
    #New B coord: B(Xb-Xd; Yb-Yd) 
    tempXa = A[0]-D[0]
    tempYa = A[1]-D[1]
    A = [tempXa, tempYa]
    print("new A:", A)
    tempXb = B[0]-D[0]
    tempYb = B[1]-D[1]
    B = [tempXb, tempYb]
    print("new B:", B)
    Square_DADB = abs(0.5*(A[0]*B[1]-A[1]*B[0]))
    print("Square_DADB:", Square_DADB)
    return Square_DADB

def getDBDC(A, B, C, D):
    tempXc = C[0]-D[0]
    tempYc = C[1]-D[1]
    C = [tempXc, tempYc]
    print("new C:", C)    
    tempXb = B[0]-D[0]
    tempYb = B[1]-D[1]
    B = [tempXb, tempYb]
    print("new B:", B)    
    Square_DBDC = abs(0.5*(C[0]*B[1]-C[1]*B[0]))
    print("Square_DBDC:", Square_DBDC)    
    return Square_DBDC
 
def getDADC(A, B, C, D):
    tempXa = A[0]-D[0]
    tempYa = A[1]-D[1]
    A = [tempXa, tempYa]
    print("new A:", A)    
    tempXc = C[0]-D[0]
    tempYc = C[1]-D[1]
    C = [tempXc, tempYc]
    print("new C:", C)    
    Square_DADC = abs(0.5*(A[0]*C[1]-A[1]*C[0]))
    print("Square_DADC:", Square_DADC)
    return Square_DADC

def getABC(A, B, C):
    tempXc = C[0]-A[0]
    tempYc = C[1]-A[1]
    C = [tempXc, tempYc]
    print("new C:", C)    
    tempXb = B[0]-A[0]
    tempYb = B[1]-A[1]
    B = [tempXb, tempYb]
    print("new B:", B)    
    Square_ABC = abs(0.5*(C[0]*B[1]-C[1]*B[0]))
    print("Square_ABC:", Square_ABC)
    return Square_ABC

triSquare = getDADB(A, B, C, D) + getDBDC(A, B, C, D) + getDADC(A, B, C, D)
print("Sum of constructive triangles:", triSquare)
mainSquare = getABC(A, B, C)

if triSquare == mainSquare:
    print("\nInside the triangle")
else:
    print("\nOutside the triangle")  
   

plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]])
plt.plot([A[0], C[0]], [A[1], C[1]])
plt.plot([A[0], D[0]], [A[1], D[1]])
plt.plot([B[0], D[0]], [B[1], D[1]])
plt.plot([D[0], C[0]], [D[1], C[1]])
plt.plot(D[0], D[1], 'ro')

plt.fill_between([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='grey', alpha='0.5')

plt.annotate(
        "A",
        xy=(A[0], A[1]), xytext=(10, 10),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5)
        )
plt.annotate(
        "B",
        xy=(B[0], B[1]), xytext=(10, 10),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5)
        )
plt.annotate(
        "C",
        xy=(C[0], C[1]), xytext=(10, 10),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5)
        )
plt.annotate(
        "D",
        xy=(D[0], D[1]), xytext=(20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0')
        )


plt.xlabel('X')
plt.ylabel('Y')
plt.show()