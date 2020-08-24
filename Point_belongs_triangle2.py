#! python 3

import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.master = master
        self.customFont1 = tkFont.Font(family="Times New Roman", size=14) 
        self.customFont2 = tkFont.Font(family="Times New Roman", size=10)
        self.init_window()
        
       
    def init_window(self):
        window.title("PointBelongsToTriangle")
#        window.resizable(width = False, height = False)
        window.geometry('600x650')
        
        label0 = tk.Label(text = "\nWelcome to PointBelongsToTriangle app!\t\n", font=self.customFont1)
        label0.grid(column = 2, row = 0, columnspan = 5, sticky=tk.N+tk.S)
       
        label0_1 = tk.Label(text = "\t", font=self.customFont2)
        label0_1.grid(column = 0, row = 0, sticky=tk.E)
        label0_2 = tk.Label(text = "\t", font=self.customFont2)
        label0_2.grid(column = 8, row = 0, sticky=tk.E) 
        
        label1 = tk.Label(text = "Apex A:", font=self.customFont2)
        label1.grid(column = 1, row = 1, sticky=tk.E)
        label1_1 = tk.Label(text = "x:", font=self.customFont2)
        label1_1.grid(column = 3, row = 1, sticky=tk.W)        
        self.entry1_1 = tk.Entry(width = 4, font=self.customFont2)
        self.entry1_1.grid(column = 4, row = 1, sticky=tk.W)
        self.entry1_1.insert(tk.END, 1)        
        label1_2 = tk.Label(text = "y:", font=self.customFont2)
        label1_2.grid(column = 6, row = 1, sticky=tk.W)        
        self.entry1_2 = tk.Entry(width = 4, font=self.customFont2)
        self.entry1_2.grid(column = 7, row = 1, sticky=tk.W)
        self.entry1_2.insert(tk.END, 0) 

        label2 = tk.Label(text = "Apex B:", font=self.customFont2)
        label2.grid(column = 1, row = 2, sticky=tk.E)
        label2_1 = tk.Label(text = "x:", font=self.customFont2)
        label2_1.grid(column = 3, row = 2, sticky=tk.W)        
        self.entry2_1 = tk.Entry(width = 4, font=self.customFont2)
        self.entry2_1.grid(column = 4, row = 2, sticky=tk.W)
        self.entry2_1.insert(tk.END, 0) 
        label2_2 = tk.Label(text = "y:", font=self.customFont2)
        label2_2.grid(column = 6, row = 2, sticky=tk.W)        
        self.entry2_2 = tk.Entry(width = 4, font=self.customFont2)
        self.entry2_2.grid(column = 7, row = 2, sticky=tk.W)
        self.entry2_2.insert(tk.END, 3) 

        label3 = tk.Label(text = "Apex C:", font=self.customFont2)
        label3.grid(column = 1, row = 3, sticky=tk.E)
        label3_1 = tk.Label(text = "x:", font=self.customFont2)
        label3_1.grid(column = 3, row = 3, sticky=tk.W)        
        self.entry3_1 = tk.Entry(width = 4, font=self.customFont2)
        self.entry3_1.grid(column = 4, row = 3, sticky=tk.W)
        self.entry3_1.insert(tk.END, 3) 
        label3_2 = tk.Label(text = "y:", font=self.customFont2)
        label3_2.grid(column = 6, row = 3, sticky=tk.W)        
        self.entry3_2 = tk.Entry(width = 4, font=self.customFont2)
        self.entry3_2.grid(column = 7, row = 3, sticky=tk.W)
        self.entry3_2.insert(tk.END, 0) 
        
        empty_row = tk.Label(text = " ", font=self.customFont2)
        empty_row.grid(column = 0, row = 4)        
        
        label4 = tk.Label(text = "Target point D:", font=self.customFont2)
        label4.grid(column = 1, row = 5, sticky=tk.E)
        label4_1 = tk.Label(text = "x:", font=self.customFont2)
        label4_1.grid(column = 3, row = 5, sticky=tk.W)        
        self.entry4_1 = tk.Entry(width = 4, font=self.customFont2)
        self.entry4_1.grid(column = 4, row = 5, sticky=tk.W)
        self.entry4_1.insert(tk.END, 1) 
        label4_2 = tk.Label(text = "y:", font=self.customFont2)
        label4_2.grid(column = 6, row = 5, sticky=tk.W)        
        self.entry4_2 = tk.Entry(width = 4, font=self.customFont2)
        self.entry4_2.grid(column = 7, row = 5, sticky=tk.W)  
        self.entry4_2.insert(tk.END, 1)               
        
        empty_row = tk.Label(text = " ", font=self.customFont2)
        empty_row.grid(column = 0, row = 8)   
        
        button_5 = tk.Button(text = "Proceed", font=self.customFont2, command=self.calculate)
        button_5.grid(column = 1, row = 9, columnspan = 7, sticky=tk.W+tk.E)
        
        empty_row = tk.Label(text = " ", font=self.customFont2)
        empty_row.grid(column = 0, row = 10) 

        self.label_result = tk.Label(text = "", font=self.customFont1)
        self.label_result.grid(column = 1, row = 11, columnspan=7, sticky=tk.W+tk.E)                
        
        empty_row = tk.Label(text = " ", font=self.customFont2)
        empty_row.grid(column = 0, row = 12)   
        
        photo = tk.PhotoImage(file="rsz_1image1.png")
        label_photo1 = tk.Label(image=photo)
        label_photo1.image = photo
        label_photo1.grid(column = 1, row = 0, sticky=tk.W)
        label_photo2 = tk.Label(image=photo)
        label_photo2.image = photo
        label_photo2.grid(column = 7, row = 0, sticky=tk.E)        

    def getTriangleArea(self, P1, P2, P3, label):
        Square = abs(0.5*(((P1[0])*(P2[1])-(P1[1])*(P2[0]))+((P2[0])*(P3[1])-(P2[1])*(P3[0]))+((P3[0])*(P1[1])-(P3[1])*(P1[0]))))
        print("Square " + label + ":", Square)
        return Square


    def calculate(self):
        try:
            A = [int(self.entry1_1.get()), int(self.entry1_2.get())]
            B = [int(self.entry2_1.get()), int(self.entry2_2.get())]
            C = [int(self.entry3_1.get()), int(self.entry3_2.get())]
            D = [int(self.entry4_1.get()), int(self.entry4_2.get())]
            triSquare = self.getTriangleArea(A, B, D, "ABD") + self.getTriangleArea(B, C, D, "BCD") + self.getTriangleArea(A, C, D, "ACD")
            print("Sum of added triangles:", triSquare)
            mainSquare = self.getTriangleArea(A, B, C, "ABC")
            
            if triSquare == mainSquare:
                print("Inside the triangle")
                self.label_result['text'] = "Inside the triangle"
    
            else:
                print("Outside the triangle")  
                self.label_result['text'] = "Outside the triangle"
            self.toPlot(A, B, C, D)            
        except:
            print("Incorrect input. Only integers are allowed")
            self.label_result['text'] = "Incorrect input. Only integers are allowed"
            self.plot_widget.grid_forget()


    def toPlot(self, A, B, C, D):
        
        fig = plt.figure()
        plt.ion()        
        canvas = FigureCanvasTkAgg(fig, master=window)
        self.plot_widget = canvas.get_tk_widget() 
        
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
         
        self.plot_widget.grid(row=14, column=1, columnspan=7)        

    
window = tk.Tk()
app = Window(window)
window.mainloop()











