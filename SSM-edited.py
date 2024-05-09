# import 
#import heartrate; heartrate.trace(browser = True)
from tkinter import *
from tkinter import messagebox as dialog
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import math
import re
import xlwt
import xlrd

#window size
HEIGHT = 500
WIDTH = 600

window = Tk()

#Define Input value
class Calculator:
    def __init__(self):
    
        window.title("Factor of Safety")

        
        self.g = StringVar() 
        self.void_ratio = StringVar() 
        self.specific_gravity = StringVar() 
        self.Yb = StringVar() 
        self.Saturation = StringVar()  
        self.Effective_cohension = StringVar()  
        self.Y = StringVar()
        self.T = StringVar()  
        self.WL = StringVar()  
        self.H = StringVar()  
        self.Fs = StringVar()  
        self.Result = StringVar()
        self.Notice = StringVar()
        self.Beta_result =  StringVar()
        self.Beta_notice =StringVar()

        # Default Values
        self.void_ratio.set("0.538462")
        self.g.set('9.81')
        self.specific_gravity.set('3.276')  
        self.Yb.set('17') 
        self.Saturation.set('1') 
        self.Effective_cohension.set('6000') 
        self.Y.set('34.88')
        self.T.set('32')
        self.WL.set('2.5')
        self.H.set('4.3')

        canvas = Canvas(window, height=HEIGHT, width=WIDTH)
        canvas.pack()
        
        Intro1 = Frame(window, bg='#f5f5f5', bd=5)
        Intro1.place(relx=0.5, rely=0.00, relwidth=0.9, relheight=0.05, anchor='n')
        frame = Frame(window, bg='#f5f5f5', bd=5)
        frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.65, anchor='n')
        Lower_frame = Frame(window, bg='#fffafa', bd=5)
        Lower_frame.place(relx=0.5, rely=0.7, relwidth=0.9, relheight=0.25, anchor='n')
        #frame = Frame(window)
        #frame.pack(padx=25, pady=20)

        Label(Intro1, text="If you want to use the individual calculator, please strat filling data below:", bg='#ffe384').grid(row=0, column=1, columnspan=3)
        Label(frame, text="Gravitational acceleration constant(Default)",bg='#F0FFFF').grid(row=1, column=1, columnspan=3, sticky=W)
        Label(frame, text="Void Ratio",bg='#F0FFFF').grid(row=2, column=1, columnspan=3, sticky=W)
        Label(frame, text="Specific Gravity",bg='#F0FFFF').grid(row=3, column=1, columnspan=3, sticky=W)
        Label(frame, text="Suction Angle",bg='#F0FFFF').grid(row=4, column=1, columnspan=3, sticky=W)
        Label(frame, text="Saturation").grid(row=5, column=1, columnspan=3, sticky=W)
        Label(frame, text="Effective Cohesion",bg='#F0FFFF').grid(row=6, column=1, columnspan=3, sticky=W)
        Label(frame, text="Internal Friction Angle",bg='#F0FFFF').grid(row=7, column=1, columnspan=3, sticky=W)
        Label(frame, text="Angle of Failure Surface",bg='#F0FFFF').grid(row=8, column=1, columnspan=3, sticky=W)
        Label(frame, text="Water Level").grid(row=9, column=1, columnspan=3, sticky=W)
        Label(frame, text="Hight of Streambank",bg='#F0FFFF').grid(row=10, column=1, columnspan=3, sticky=W)
        Label(Lower_frame, text="If you want to Calculate the whole file, please fill in the data above in blue and select the file:",bg='#ffe384').grid(row=0, column=1, columnspan=3)
#Input Values
        Entry(frame, justify=RIGHT, textvariable=self.g).grid(row=1, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.void_ratio).grid(row=2, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.specific_gravity).grid(row=3, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.Yb).grid(row=4, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.Saturation).grid(row=5, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.Effective_cohension).grid(row=6, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.Y).grid(row=7, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.T).grid(row=8, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.WL).grid(row=9, column=3, sticky=W)
        Entry(frame, justify=RIGHT, textvariable=self.H).grid(row=10, column=3, sticky=W)

#Output Values
        Label(frame, text="Calculation Results:   The Factor of Safety is: ",bg='#FFB6C1').grid(row=15,column=1,sticky=E)
        Label(frame, textvariable=self.Fs,bg='#FFB6C1').grid(row=15, column=2, sticky=W)
        Label(frame, textvariable=self.Result,bg='#FFB6C1').grid(row=15, column=3, sticky=W)
        Label(frame, textvariable=self.Beta_notice,bg='#FFB6C1').grid(row=16, column=1, sticky=W)
        Label(frame, textvariable=self.Beta_result,bg='#FFB6C1').grid(row=16, column=2, sticky=W)
        Label(Lower_frame, textvariable=self.Notice,bg='#FFB6C1').grid(row=3, column=2, sticky=W)

#Units
        Message(frame, text="N / kg").grid(row=1, column=5)
        Message(frame, text="Unitless").grid(row=2, column=5)
        Message(frame, text="Unitless").grid(row=3, column=5)
        Message(frame, text="°").grid(row=4, column=5)
        Message(frame, text="Unitless").grid(row=5, column=5)
        Message(frame, text="Pa").grid(row=6, column=5)
        Message(frame, text="°").grid(row=7, column=5)
        Message(frame, text="°").grid(row=8, column=5)      
        Message(frame, text="m").grid(row=9, column=5)
        Message(frame, text="m").grid(row=10, column=5)


        Frame(frame, height=10).grid(row=13, column=4, columnspan=7)

        # Button 1: Calculate
        Button(frame, width=19, text="Calculate", command=self.calculate_1).grid(row=14, column=3)

        #Button 2: Select a File
        #Button(Lower_frame, width=19, text="Select A File", command=self.read_variables).grid(row=2, column=2)
        
        # Button 3: Calculate whole file
        Button(Lower_frame, width=19, text="Calculate the whole file", command=self.calculate_2).grid(row=6, column=2)
        
        window.mainloop()

    
# Main calculation of Button 1
    def calculate_1(self):
        #get values
        g = eval(self.g.get()) 
        e = eval(self.void_ratio.get())
        Gs= eval(self.specific_gravity.get())
        Ybb  = eval(self.Yb.get()) #how to calculate
        S = eval(self.Saturation.get())
        c = eval(self.Effective_cohension.get()) 
        YY = eval(self.Y.get())
        T= eval(self.T.get())
        WL  = eval(self.WL.get())
        H  = eval(self.H.get())
        Yb = Ybb/180*math.pi
        Y = YY/180*math.pi
        Theta = T/180*math.pi
        if (Y+math.pi/2)/2 < Theta-0.17:
            Beta = [Y/2, (Y+math.pi/2)/2, Theta-0.17]
        else:
            Beta = [Y/2, (Y/2+Theta-0.17)/2, Theta-0.17]
        p=997
        Yw=p
        U =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        N=[]
        I=[]
        Fs=[1]
        Is=[]
        Fsf1 = [-1000000]
        Fsf=[]
        V=[]
        W=[]
        K=[]
        SS=[]
        P=[0,0,0,0,0,0,0,0,0,0]
        Sum_tol1 = 0
        Sum_tol2 = 0
        Sum_tol3 = 0

#first loop(different normal force)
        for l in range (3):
            LL =H/math.tan(Theta)
            h = LL* math.tan(Beta[l])
            h2 = H-h
            #kkk=0
            jj=0
            Level =H
            x = (h2)/math.tan(Beta[l])
            y = h2
            L1 = h2/math.sin(Beta[l])
            L2 = h/math.sin(Beta[l])
            L= [L1/10,L1/10,L1/10,L1/10,L1/10,L1/10,L1/10,L1/10,L1/10,L1/10,L2/10,L2/10,L2/10,L2/10,L2/10,L2/10,L2/10,L2/10,L2/10,L2/10]

            L_tol = L[0]+L[1]+L[2]
#calculate the volume
            V.append(1/200*x*y)
            V.append(3/200*x*y)
            V.append(5/200*x*y)
            V.append(7/200*x*y)
            V.append(9/200*x*y)
            V.append(11/200*x*y)
            V.append(13/200*x*y)
            V.append(15/200*x*y)
            V.append(17/200*x*y)
            V.append(19/200*x*y)
            V.append(19/200*h2*LL)
            V.append(17/200*h2*LL)
            V.append(15/200*h2*LL)
            V.append(13/200*h2*LL)
            V.append(11/200*h2*LL)
            V.append(9/200*h2*LL)
            V.append(7/200*h2*LL)
            V.append(5/200*h2*LL)
            V.append(3/200*h2*LL)
            V.append(1/200*h2*LL)

            for i in range(20):
                if WL > Level:
                    self.Fs.set(format(0, '.3f'))
                    self.Result.set(format("Groundwater Level cant be higher than the streambank"))
                else: 
    # HYDROSTATIC FORCE               
                    P_top=0
                    P_Bot=(WL)*p*g
                    Fw = (P_top+P_Bot)/2 * WL
    # UPLIFTING FORCE              
                    U[0]=(WL-H+y/20)*Yw*L[0]*g
                    U[1]=(WL-H+y*3/20)*Yw*L[1]*g
                    U[2]=(WL-H+y*5/20)*Yw*L[2]*g
                    U[3]=(WL-H+y*7/20)*Yw*L[3]*g
                    U[4]=(WL-H+y*9/20)*Yw*L[4]*g
                    U[5]=(WL-H+y*11/20)*Yw*L[5]*g
                    U[6]=(WL-H+y*13/20)*Yw*L[6]*g
                    U[7]=(WL-H+y*15/20)*Yw*L[7]*g
                    U[8]=(WL-H+y*17/20)*Yw*L[8]*g
                    U[9]=(WL-H+y*19/20)*Yw*L[9]*g
                    U[10]=(WL-H+h/20)*Yw*L[10]*g
                    U[11]=(WL-H+h*3/20)*Yw*L[11]*g
                    U[12]=(WL-H+h*5/20)*Yw*L[12]*g
                    U[13]=(WL-H+h*7/20)*Yw*L[13]*g
                    U[14]=(WL-H+h*9/20)*Yw*L[14]*g
                    U[15]=(WL-H+h*11/20)*Yw*L[15]*g
                    U[16]=(WL-H+h*13/20)*Yw*L[16]*g
                    U[17]=(WL-H+h*15/20)*Yw*L[17]*g
                    U[18]=(WL-H+h*17/20)*Yw*L[18]*g
                    U[19]=(WL-H+h*19/20)*Yw*L[19]*g
                    print (U)
                Bulkdensity = Yw*(Gs+e*S)/(1+e)
                Weight = (V[i]* g * Bulkdensity)
                Normal_force= Weight/math.cos(Beta[l])
                Si=(1/Fs[0])*(L[i]*c+Normal_force*math.tan(Y)-U[i]*math.tan(Yb))
                Ks = (c*L[i]+Si*math.tan(Yb)-U[i]*math.tan(Y))/Fs[0]
                Kss = math.sin(Beta[l])-math.cos(Beta[l])*math.tan(Y)/Fs[0]
                if i==0:
                    INJ = 0 - math.cos(Beta[l])*Ks + Normal_force * Kss
                else:
                    INJ = I[i-1] - math.cos(Beta[l])*Ks+Normal_force * Kss
                ISJ = 0.4* INJ*math.sin((math.pi*(L[i]/L_tol))*math.pi/180)
                #print (Normal_force)
                #print (Ks)
                #print(Beta)
                if i==0:
                    Normal_Force = (Weight-ISJ+0-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                else:
                    Normal_Force = (Weight+Is[i-1]-ISJ-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                W.append(Weight)
                N.append(Normal_Force)
                K.append(Ks)
                Is.append(ISJ)
                I.append(INJ)
                SS.append(Si)
                #print(P)
                #print(U)
                #print(W)
                #print(Kss)
                #print(N)
                #print(Is)
                #print(I)
                #print(SS)
                Sum1 = c*L[i]+SS[i]*math.tan(Yb)+(Normal_force-U[i])*math.tan(Y)
                Sum2 = N[i]
                Sum_tol1+= Sum1
                Sum_tol2+= Sum2
                
            Fos = math.cos(Beta[l])*(Sum_tol1)/(math.sin(Beta[l])*Sum_tol2-Fw)
            Sum_tol2=0
            Sum_tol1=0
            #print(Fos)
            #print (Sum_tol1)
            #print(Sum_tol2)
            #print(Sum_tol3)
    #main loop, condition: error less than 0.1%, if the results cant meet the requiremnet, it will continue running
            while abs((Fos-Fs[0])/Fs[0])>0.001:
                #print(Sum_tol1)
                Fs[0] = Fos

                for k in range (20):
                    Si=(1/Fs[0])*(L[k]*c+N[k]*math.tan(Y)-U[k]*math.tan(Yb))
                    Ks = (c*L[k]+Si*math.tan(Yb)-U[k]*math.tan(Y))/Fs[0]
                    Kss = math.sin(Beta[l])-math.cos(Beta[l])*math.tan(Y)/Fs[0]
                    if k==0:
                        INJ = 0 - math.cos(Beta[l])*Ks + N[k] * Kss
                    else:
                        INJ = I[k-1] - math.cos(Beta[l])*Ks+N[k] * Kss
                    ISJ = 0.4* INJ*math.sin((math.pi*(L[k]/L_tol))*math.pi/180)
                    if k==0:
                        Normal_Force = (W[k]-ISJ+0-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                    else:
                        Normal_Force = (W[k]+Is[k-1]-ISJ-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                    Is[k]=ISJ
                    I[k]=INJ
                    SS[k] = Si
                    Sum1 = c*L[k]+math.cos(Beta[l])+SS[k]*math.tan(Yb)+(N[k]-U[k])*math.tan(Y)
                    Sum2 = N[k]
                    Sum_tol1+= Sum1
                    Sum_tol2+= Sum2
                    N[k]=Normal_Force
                    #print (Sum_tol1)
                Fos = math.cos(Beta[l])*(Sum_tol1)/(math.sin(Beta[l])*Sum_tol2-Fw)
                Sum_tol2=0
                Sum_tol1=0
                jj+=1
                if jj >1000:
                    break    
                #print (jj)
                #print(Fs)
            Fsf.append(Fos)
            print (Fsf)
            print(Beta)
#Find the lowest Fs with Beta
        if Fsf[1]<Fsf[0] and Fsf[1]<Fsf[2]:
            a = ((Fsf[1]-Fsf[0])*(Beta[2]-Beta[1])-(Fsf[2]-Fsf[1])*(Beta[1]-Beta[0]))/((Beta[1]*Beta[1]-Beta[0]*Beta[0])*(Beta[2]-Beta[1])-(Beta[2]*Beta[2]-Beta[1]*Beta[1])*(Beta[1]-Beta[0]))
            b = (Fsf[1]-Fsf[0]-a*(Beta[1]*Beta[1]-Beta[0]*Beta[0]))/(Beta[1]-Beta[0])
            c = Fsf[0]-Beta[0]*Beta[0]*a-Beta[0]*b
            x_low = -b/(2*a)
            #print(a,b,c,x_low)
            y_low = (4*a*c-b*b)/(4*a)
            #print(y_low)
            Beta_results = x_low /math.pi*180
        elif Fsf[2]> Fsf[1] and Fsf[1]>Fsf[0]:
            y_low = Fsf[0]
            Beta_results = Beta[0]/math.pi*180
        elif Fsf[1]>Fsf[2] and Fsf[0]>Fsf[1]:
            y_low = Fsf[2]
            Beta_results = Beta[2]/math.pi*180
# OUTPUT
        if (y_low > 1):
            self.Fs.set(format(y_low, '.3f'))
            self.Result.set(format("The Streambank is Safe"))
            self.Beta_notice.set(format("The angle of the failure plane is"))
            self.Beta_result.set(format(Beta_results, '.3f'))
        elif (y_low< 1):
            self.Fs.set(format(y_low, '.3f'))
            self.Result.set(format("This Streambank is Unsafe"))
            self.Beta_result.set(format(Beta_results, '.3f'))
            self.Beta_notice.set(format("The angle of the failure plane is"))
        else: 
            self.Fs.set(format(y_low, '.3f'))
            self.Result.set(format("This Streambank will Fail soon without any intervention"))
            self.Beta_result.set(format(Beta_results, '.3f'))
            self.Beta_notice.set(format("The angle of the failure plane is"))
# select a file:
    #def browsefunc():
        #filename=askopenfile()
    #def open_file(self):
        #txt_file = askopenfile(title = "Select a file")
    def open_file(self):
        file = (filedialog.askopenfilename(title = 'Select a *.pm file',filetypes=[('text files', '*.txt'),
        ('All files', '*.*')]))
        return file
    def open_file2(self):
        file = (filedialog.askopenfilename(title = 'Select a *.olf file',filetypes=[('text files', '*.txt'),
        ('All files', '*.*')]))
        return file

# need a formatted input file   
    def read_variables(self):
        """
        read data from txt
        :return:
        """
        txt_file = self.open_file()
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()

        vars = re.findall('# [a-z A-Z\(\)\d]+', content)
        values = re.split('# [a-z A-Z\(\)\d]+', content)[1:]
        assert len(vars) == len(values)
        new_values = []
        for value in values:
            value = re.sub('[\n ]', ' ', value).strip().split()
            value = [float(v) for v in value]
            new_values.append(value.copy())

        return vars, new_values, value

# Calculate the whole file:
    def calculate_2(self):
        file = open ("C:/Program_Files/model_test.txt", 'a', encoding='utf-8')
        var_names, var_values, value = self.read_variables()
        X_cor = var_values[0]
        Y_cor = var_values[1]
        Z_cor = var_values[2]
        S =var_values[5]
        depth = var_values[6]

        length = len(value)
        g = eval(self.g.get()) 
        e = eval(self.void_ratio.get())
        Gs= eval(self.specific_gravity.get())
        Ybb  = eval(self.Yb.get()) 
        c = eval(self.Effective_cohension.get()) 
        YY = eval(self.Y.get())
        T= eval(self.T.get())
        H  = eval(self.H.get())
        Yb = Ybb/180*math.pi
        Y = YY/180*math.pi
        Theta = T/180*math.pi
        if (Y+math.pi/2)/2 < Theta-0.17:
            Beta = [Y/2, (Y+math.pi/2)/2, Theta-0.17]
        else:
            Beta = [Y/2, (Y/2+Theta-0.17)/2, Theta-0.17]
        p=997
        Yw=p
        U =[0,0,0,0,0]
        N=[0,0,0,0,0]
        I=[0,0,0,0,0]
        Fs=[1]
        Is=[0,0,0,0,0]
        Fss = []
        Bett=[]
        Fsf1 = [-1000000]
        Fsf=[0,0,0]
        W=[0,0,0,0,0]
        K=[0,0,0,0,0]
        SS=[0,0,0,0,0]
        P=[0,0,0,0,0]
        Sum_tol1 = 0
        Sum_tol2 = 0
        Sum_tol3 = 0

#first loop(different normal force)
        for j in range (0, length):
            WL = depth[j]
            for l in range (0,3):
                LL =H/math.tan(Theta)
                h = LL* math.tan(Beta[l])
                h2 = H-h
                #kkk=0
                jj=0
                Level =H
                x = (h2/3)/math.tan(Beta[l])
                y = h2/3
                L1 = h2/math.sin(Beta[l])
                L2 = h/math.sin(Beta[l])
                L= [L1/3,L1/3,L1/3,L2/2,L2/2]
                L_tol = L[0]+L[1]+L[2]+L[3]+L[4]
                V =[1/2*x*y,3/2*y*x,5/2*x*y,3/8*h2*LL,1/8*h2*LL]
                for i in range(5):
    # HYDROSTATIC FORCE               
                    P_top=0
                    P_Bot=(WL)*p*g
                    Fw = (P_top+P_Bot)/2 * WL
    # UPLIFTING FORCE              
                    U[0]=(WL-H+y/2)*Yw*L[0]*g
                    U[1]=(WL-H+1.5*y)*Yw*L[1]*g
                    U[2]=(WL-H+2.5*y)*Yw*L[2]*g
                    U[3]=(WL-0.75*h)*Yw*L[3]*g
                    U[4]=(WL-0.25*H)*Yw*L[4]*g

                    Bulkdensity = Yw*(Gs+e*S[j])/(1+e)
                    Weight = (V[i]* g * Bulkdensity)
                    Normal_force= Weight/math.cos(Beta[l])
                    Si=(1/Fs[0])*(L[i]*c+Normal_force*math.tan(Y)-U[i]*math.tan(Yb))
                    Ks = (c*L[i]+Si*math.tan(Yb)-U[i]*math.tan(Y))/Fs[0]
                    Kss = math.sin(Beta[l])-math.cos(Beta[l])*math.tan(Y)/Fs[0]
                    if i==0:
                        INJ = 0 - math.cos(Beta[l])*Ks + Normal_force * Kss
                    else:
                        INJ = I[i-1] - math.cos(Beta[l])*Ks+Normal_force * Kss
                    ISJ = 0.4* INJ*math.sin((math.pi*(L[i]/L_tol))*math.pi/180)

                    if i==0:
                        Normal_Force = (Weight-ISJ+0-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                    else:
                        Normal_Force = (Weight+Is[i-1]-ISJ-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                    W[i] = Weight
                    N[i] = Normal_Force
                    K[i]=Ks
                    Is[i] = ISJ
                    I[i] = INJ
                    SS[i] = Si
                    Sum1 = c*L[i]+SS[i]*math.tan(Yb)+(Normal_force-U[i])*math.tan(Y)
                    Sum2 = N[i]
                    Sum_tol1+= Sum1
                    Sum_tol2+= Sum2
                    
                Fos = math.cos(Beta[l])*(Sum_tol1)/(math.sin(Beta[l])*Sum_tol2-Fw)
                Sum_tol2=0
                Sum_tol1=0
    #main loop, condition: error less than 0.1%, if the results cant meet the requiremnet, it will continue running
                while abs((Fos-Fs[0])/Fs[0])>0.001:
                    #print(Sum_tol1)
                    Fs[0] = Fos
                    for k in range (5):
                        Si=(1/Fs[0])*(L[k]*c+N[k]*math.tan(Y)-U[k]*math.tan(Yb))
                        Ks = (c*L[k]+Si*math.tan(Yb)-U[k]*math.tan(Y))/Fs[0]
                        Kss = math.sin(Beta[l])-math.cos(Beta[l])*math.tan(Y)/Fs[0]
                        if k==0:
                            INJ = 0 - math.cos(Beta[l])*Ks + N[k] * Kss
                        else:
                            INJ = I[k-1] - math.cos(Beta[l])*Ks+N[k] * Kss
                        ISJ = 0.4* INJ*math.sin((math.pi*(L[k]/L_tol))*math.pi/180)
                        if k==0:
                            Normal_Force = (W[k]-ISJ+0-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                        else:
                            Normal_Force = (W[k]+Is[k-1]-ISJ-math.sin(Beta[l])*Ks)/(math.cos(Beta[l])+math.tan(Y)*math.sin(Beta[l])/Fs[0])
                        Is[k]=ISJ
                        I[k]=INJ
                        SS[k] = Si
                        Sum1 = c*L[k]+math.cos(Beta[l])+SS[k]*math.tan(Yb)+(N[k]-U[k])*math.tan(Y)
                        Sum2 = N[k]
                        Sum_tol1+= Sum1
                        Sum_tol2+= Sum2
                        N[k]=Normal_Force
                        #print (Sum_tol1)
                    Fos = math.cos(Beta[l])*(Sum_tol1)/(math.sin(Beta[l])*Sum_tol2-Fw)
                    Sum_tol2=0
                    Sum_tol1=0
                    jj+=1
                    if jj >1000:
                        break    
                Fsf[l] = Fos
#Find the lowest Fs with Beta
            if Fsf[1]<Fsf[0] and Fsf[1]<Fsf[2] and Fsf[1] >0:
                a = ((Fsf[1]-Fsf[0])*(Beta[2]-Beta[1])-(Fsf[2]-Fsf[1])*(Beta[1]-Beta[0]))/((Beta[1]*Beta[1]-Beta[0]*Beta[0])*(Beta[2]-Beta[1])-(Beta[2]*Beta[2]-Beta[1]*Beta[1])*(Beta[1]-Beta[0]))
                b = (Fsf[1]-Fsf[0]-a*(Beta[1]*Beta[1]-Beta[0]*Beta[0]))/(Beta[1]-Beta[0])
                c = Fsf[0]-Beta[0]*Beta[0]*a-Beta[0]*b
                x_low = -b/(2*a)
                #print(a,b,c,x_low)
                y_low = (4*a*c-b*b)/(4*a)
                #print(y_low)
                Beta_results = x_low /math.pi*180
            elif Fsf[2]> Fsf[1] and Fsf[1]>Fsf[0] and Fsf[0] >0:
                y_low = Fsf[0]
                Beta_results = Beta[0]/math.pi*180
            elif Fsf[1]>Fsf[2] and Fsf[0]>Fsf[1] and Fsf[2] >0:
                y_low = Fsf[2]
                Beta_results = Beta[2]/math.pi*180
            else: 
                y_low = 0
                Beta_results = 0
            Fss.append(y_low)
            Bett.append(Beta_results)
        file.write('\n'+"# Fs"+'\n')
        le = len(Fss)
        for m in range (le):
            if (m+1)%5 !=0:
                file.write(str(Fss[m])+'       ')
            else: 
                file.write(str(Fss[m])+'\n') 
            j+=1
            print (j)
        wk=xlwt.Workbook(encoding='utf-8',style_compression=0)
        sht = wk.add_sheet("sheet1",cell_overwrite_ok=True)
        sht.write(0,0,'X')
        sht.write(0,1,'Y')
        sht.write(0,2,'Z')
        sht.write(0,3,'Saturation')
        sht.write(0,4,'Fs')
        sht.write(0,5,'Beta')
        for m in range (le):
            sht.write (m+1,0,X_cor[m])
            sht.write (m+1,1,Y_cor[m])
            sht.write (m+1,2,Z_cor[m])
            sht.write (m+1,3,S[m])
            sht.write (m+1,4,Fss[m])
            sht.write (m+1,5,Bett[m])
        wk.save('C:/Users/Administrator/Desktop/Thesis/test/output.xlt')
        self.Notice.set(format("Finshed, file location:C:/Program_Files/output_file"))


#Menu
def about():
    dialog.showinfo(title='About', message = "This is a software for calculting the factor of safety, Author: Quan Wei, Version 4.0" )
def help():
    dialog.showinfo(title='Help', message = "Please read carefully: if you want to use it as an individual calculation, please use the top frame, and if you want to calculate the whole file, please use the excel format provided and use the lower frame" )
menubar = Menu(window)

menubar.add_command(label="About",command=about)
menubar.add_command(label="Help",command=help)
menubar.add_command(label="Quit",command=window.quit)
window.config(menu=menubar)

if __name__ == '__main__':
    Calculator()
    pass

