#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import math
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import math
get_ipython().run_line_magic('matplotlib', 'inline')
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy import stats
from IPython.display import Image, display
import ipywidgets as widgets
import ipywidgets as widgets
from IPython.display import Image, display
from ipywidgets import Button, Layout
from chemlib import electrolysis
from chemlib import Galvanic_Cell


# ## #Initial Rate Method

# In[2]:


#Initial Rate Method
###################################################################################
print('" The method of initial rates allows the values of these reaction orders to be found by running the reaction multiple times under controlled conditions and measuring the rate of the reaction in each case. All variables are held constant from one run to the next, except for the concentration of one reactant. The order of that reactant concentration in the rate law can be determined by observing how the reaction rate varies as the concentration of that one reactant is varied. This method is repeated for each reactant until all the orders are determined.Citition Source: chem.libretexts.org"')
#The previos information is cited from :https://chem.libretexts.org/Ancillary_Materials/Laboratory_Experiments/Wet_Lab_Experiments/General_Chemistry_Labs/Online_Chemistry_Lab_Manual/Chem_12_Experiments/01%3A_Chemical_Kinetics_-_The_Method_of_Initial_Rates_(Experiment)#:~:text=The%20method%20of%20initial%20rates%20allows%20the%20values%20of%20these,the%20concentration%20of%20one%20reactant.
listOfImageNames = ["rat1.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

print('\nR1 and R2 are the rate constant')
print('\nA1 and A2 are initial concentration of reactant')

########################Initial Rate Method#########################################
def t( R1,A1,R2,A2):
    try:
        R1 =float((R1))
        A1=float((A1))
        R2=float((R2))
        A2=float((A2))
        A1 and A2 and R1 and R2 >=0
        a=math.log(R1/R2)
        t=math.log((A1)/(A2))
        n=1+(t/a)
        return ("Your reactant order is", n)
    except:
        print('Fill all requirement boxes , if this massage still appears meaning there is mistake in your details')

interact(t,  R1='Type only number', A1="Type only number",R2='Type only number', A2='Type only number');
#################################################################################
btn = widgets.Button(description='Click here to find antoher reactant order by Initial Rate Method ', layout=Layout(width='90%', height='80px'))
display(btn)
def my_event_handler(btn_object):
    w=widgets.Text(value='Initial Rate Method', disabled=True)
    display(w)

    interact(t, R1='1', A1="1",R2='5', A2='5');
    
btn.on_click(my_event_handler)
#Reference:
#https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Book%3A_Physical_Chemistry_(Fleming)/11%3A_Chemical_Kinetics_I/11.07%3A_The_Method_of_Initial_Rates
#https://chem.libretexts.org/Ancillary_Materials/Laboratory_Experiments/Wet_Lab_Experiments/General_Chemistry_Labs/Online_Chemistry_Lab_Manual/Chem_12_Experiments/01%3A_Chemical_Kinetics_-_The_Method_of_Initial_Rates_(Experiment)#:~:text=The%20method%20of%20initial%20rates%20allows%20the%20values%20of%20these,the%20concentration%20of%20one%20reactant.


# # # # # # #Interactive Graphical Method

# In[2]:


#############################################################################
################################################################################    
#Interactive Graphical Method
#############################################################################
w=widgets.Text(value='Interactive Graphical Method', disabled=True)
display(w)

print('The graphical method makes use of the concentrations of reactants. It is most useful when one reactant is isolated by having the others in large excess. A series of standards is used to make a Beers Law plot, the best-fit equation of which is used to determine the concentration of the isolated reactant. To test for the order of reaction with regard to that reactant, three plots are made. The first is concentration of the isolated reactant versus time. The second is of inverse concentration versus time, while the third is of the natural log of concentration versus time. These graphs, respectively, show zero, first, and second order dependence on the specific reactant. The graph that is most linear shows the order of the reaction with regard to that reactant.''Source: chem.libretexts.org')
print('\nCx= reactant concentration ')
print('\ntx= time when it is found Cx reactant concentration ')

listOfImageNames = [ "rate.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))




###############The graphical method 
def G(C1,t1,C2,t2,C3,t3,C4,t4,C5,t5, Time_Unite='Sec', Concenteration_Unite='Mole'):
# we make several  empty lists to store time (T) and con.   for zeroth equation and (C) for first order (c1)for second order c2 for third order
# to plot data
    try:
        
        C=[]
        T=[]
    # we need at list 
        c=[]
        c1=[]
        c2=[]
        r=[]
        t=[]
        a=[]
        k=[]


        C1 =float(C1)
    # for zeroth we need just C1.
        c.append(C1)
    #for first order we need log(C1)   
        C.append(math.log(C1))
    # for 2 order we need 1/C1  
        c1.append(1/C1)
    # FOR THIRD ORDER we need 1/(C1**2)
        c2.append((1)/(C1**2))



        t1= float(t1)
        T.append(t1)

        C2=float((C2))
        c.append(C2)

        C.append(math.log(C2))
        c1.append(1/C2)
        c2.append((1)/(C2**2))





        t2=float((t2))
        T.append(t2)

        C3 =float((C3))
        c.append(C3)

        C.append(math.log(C3))
        c1.append(1/C3)
        c2.append((1)/(C3**2))


        t3=float((t3))
        T.append(t3)
        C4=float((C4))
        c.append(C4)

        C.append(math.log(C4))
        c1.append(1/C4)
        c2.append((1)/(C4**2))


        t4=float((t4))
        T.append(t4)
        C5=float((C5))
        c.append(C5)

        C.append(math.log(C5))
        c1.append(1/C5)
        c2.append((1)/(C5**2))


        t5=float((t5))
        T.append(t5)
        Time_Unite= str(Time_Unite)
        Concenteration_Unite= str(Concenteration_Unite)
        if C1 and t1 and C2 and t2 and C3 and t3 and C4 and t4 and C5 and t5>=0:

            #n=1+(t/a)
            plt.figure()
            plt.xlabel(Time_Unite)
            plt.ylabel( Concenteration_Unite)

            plt.plot(c, T )
            plt.title('Zero order reaction')

            plt.figure()
            plt.xlabel("Minutes")
            plt.ylabel("Ln(a-x)")

            plt.plot(C, T )
            plt.title('\nFirst order reaction')

            plt.figure()
            plt.plot(c1, T )
            plt.title('\nSecond order reaction')
            plt.xlabel("Minutes")
            plt.ylabel("1/(a-x)")
            plt.figure()

            plt.plot(c2, T )
            plt.title('Third order reaction')
            plt.xlabel("Minutes")
            plt.ylabel("1/((a-x)**2)")
            slope, intercept, r_value0, p_value, std_err = stats.linregress(c,T)
            r0=abs(r_value0)
            r.append(r0)
            a0= abs(intercept)
            a.append(a0)
            consentrate0= slope
            k.append(consentrate0)
            t0=(a0)/(2*consentrate0)
            t.append(t0)


            slope, intercept, r_value1, p_value, std_err = stats.linregress(C,T)
            r1= abs(r_value1)
            r.append(r1)

            a1= math.exp(intercept)
            a.append(a1)

            consentrate1= -slope
            k.append(consentrate1)

            t1=(0.693)/consentrate1
            t.append(t1)

            slope, intercept, r_value2, p_value, std_err = stats.linregress(c1,T)
            r2= abs(r_value2)
            r.append(r2)

            consentrate2= float(slope)
            k.append(consentrate2)
            a2= (1/intercept)
            a.append(a2)
            t2=float((1)/(float(consentrate2))*(float(a2)))
            t.append(t2)

            slope, intercept, r_value3, p_value, std_err = stats.linregress(c2,T)
            r3= abs(r_value3)
            consentrate3= float(slope/2)
            k.append(consentrate3)
            a3=1/intercept
            a3=math.sqrt(abs(a3))
            a.append(a3)



            max_value = max(r)


            max_index = r.index(max_value)

            n=max_index 
            t=t[n]
            a=a[n]
            k=k[n]
            z= ("The reactant order is", n,' and the reaction half-life is ',t ," ", Time_Unite,  ' and the Constant rate is ', k )
            print(z)
        return (" ")
    except:
        print('Fill all requirement boxes , if this massage still appears meaning there is mistake in your details')

interact(G, C1='Type only number', t1="Type only number",C2='Type only number', t2='Type only number', C3='Type only number', t3="Type only number",C4='Type only number', t4='Type only number', C5='Type only number', t5='Type only number',Time_Unite='Sec', Concenteration_Unite='Mole');
#####################################################
btnnnn = widgets.Button(description='Click here to find antoher reactant order by Interactive Graphical Method', layout=Layout(width='90%', height='80px'))
display(btnnnn)

def my_event3_handler(btnnnn_object):
    w=widgets.Text(value='Interactive Graphical Method', disabled=True)
    display(w)

    interact(G, C1='1', t1="1",C2='5', t2='5', C3='2', t3="1",C4='5', t4='5', C5='5', t5='5',Time_Unite='Sec', Concenteration_Unite='Mole');
btnnnn.on_click(my_event3_handler)
    

#Reference:
#https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Kinetics/05%3A_Experimental_Methods/5.01%3A_Determining_Reaction_Order#:~:text=The%20graphical%20method%20makes%20use,concentration%20of%20the%20isolated%20reactant.


# ## #Half-Life Method

# In[4]:


#Half-Life Method
##############################################################################
w=widgets.Text(value='Half-Life Method', disabled=True)
display(w)

print('\nThe Method of Half-Lives for determining the order of a reaction is to examine the behavior of the half-life as the reaction progresses. The half-life can be defined as the time it takes for the concentration of a reactant to fall to half of its original value. The method of half-lives involved measuring the half-life’s dependence on concentration. The expected behavior can be predicted using the integrated rate laws. Source:  Patrick Fleming ,Assistant Professor (Chemistry and Biochemistry) at California State University East Bay ')
print('\na1 and a2 are the reactant concentration first and second  intial reactant concentration, respectively')
print('\nt1 and t2 are the half-life’s dependence on first and second  concentration, respectively')
print('\nInmportant note: all other factor may affect on the reaction should be constant during this wothed')
listOfImageNames = ["t.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

def H(a1,t1,a2,t2):
    try:
        a1 =float((a1))
        t1=float((t1))
        a2=float((a2))
        t2=float((t2))
        a=math.log(a1/a2)
        a1 and t1 and a2 and t2>=1
        t=math.log((t1)/(t2))
        n=1+(t/a)
        return ("Your reaction order is", n)
    except:
        print('Fill all requirement boxes , if this massage still appears meaning there is mistake in your details')


interact(H, a1='type reactant concentration EX:5 ', t1="type first half_live EX:5",a2='type reactant concentration EX:5 ', t2="type second half_live EX:5");



###############
#Half-Life Method
btnn = widgets.Button(description='Click here to find anothr reactant order by Half-Life Method', layout=Layout(width='90%', height='80px'))
display(btnn)

def my_eventt_handler(btnn_object):

    w=widgets.Text(value='Half-Life Method', disabled=True)
    display(w)


    interact(H, a1='1', t1="1",a2='5', t2='5');

btnn.on_click(my_eventt_handler)

#reference: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Kinetics/02%3A_Reaction_Rates/2.04%3A_Half-lives


# # #Vant Hoff Differential Method
# 

# In[5]:


#Vant Hoff Differential Method
w=widgets.Text(value='Vant Hoff Differential Method', disabled=True)
display(w)

print("\n1)The rate of a reaction varies as the nth power of the concentration of the reactant where (n) is the order of the reaction.\n2)Thus, for two different initial concentrations C1 and C2, equations can be written in the form")
print('\nThus,for two different initial concentrations C1 and C2, equations can be written in the form')
print('\nC1 and C2 are initial  Concentration of reactant  ')
print('\nR1 and R2 are two rate reaction thus all other reactant and reaction enviroment constant except the reactor which wat to know its order ')

listOfImageNames = ["Vt.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))


def v(C1_1,C1_2,t1_1,t1_2,C2_1,C2_2,t2_1,t2_2 ):
    try:    
    
        C1_1 =float((C1_1))
        C1_2=float((C1_2))
        t1_1=float((t1_1))
        t1_2=float((t1_2))
        C2_1 =float((C2_3))
        C2_2=float((C2_2))
        t2_1=float((t2_1))
        t2_2=float((t2_2))


        C1 and R1 and C2 and R2>=1
        R1=math.log((C2-C1)/(t2-t1))
        R1=math.log((C4-C3)/(t4-t3))
        t=math.log((t1)/(t3))
        n=math.log((R1)/(R2)/(t))
        return ("Your reaction order is", n)
    except:
        print('Fill all requirement boxes , if this massage still appears meaning there is mistake in your details')
interact(v,C1_1='initial concentrations C1',C1_2='concentrations C1 after t1_2 time ',t1_1='time before reaction satrt ',t1_2='time when C1_2 is found',C2_1='initial concentrations C2',C2_2='concentrations C2 after t1_2 time' ,t2_1='time before reaction satrt' ,t2_2='time when C2_2 is found'  );
#Van't Hoff Differential Method
btnv = widgets.Button(description='Click here to find antoher reactant order by Vant Hoff Differential Method', layout=Layout(width='90%', height='80px'))
display(btnv)

def my_eventv_handler(btnv_object):
    w=widgets.Text(value='Vant Hoff Differential Method', disabled=True)
    display(w)

    interact(v,C1_1='initial concentrations C1',C1_2='concentrations C1 after t1_2 time ',t1_1='time before reaction satrt ',t1_2='time when C1_2 is found',C2_1='initial concentrations C2',C2_2='concentrations C2 after t1_2 time' ,t2_1='time before reaction satrt' ,t2_2='time when C2_2 is found'  );
btnv.on_click(my_eventv_handler)
################################################################


#https://www.askiitians.com/iit-jee-physical-chemistry/chemical-kinetics/methods-for-determination-of-order-of-reaction.aspx


# # #Zero Reaction Order

# In[6]:


#Zero Reaction Order
###########################################################
w=widgets.Text(value='Zero  Reaction Order', disabled=True)
display(w)

print('\nThis Zero-order reaction means that has a rate that is independent of the concentration of the reactant(s).\n')
listOfImageNames = [ "zeroth.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))
print('\nC1, C2, C3, and C4 represent [A] of the reactant which is wanted to find its order ')
print('\nt1, t2, t3, and t4 represent time [t] from begining reaction until the trial to find rest concenteration ')

def Z(unite_time,unite_con,C1,t1,C2,t2,C3,t3,C4,t4):
# we need two empty list to draw zeroth equation T for time and C for concenteration
    try:
        C=[]
        T=[]

        C1 =float(C1)   
        C.append((C1))
        t1= float(t1)
        T.append(t1)

        C2=float((C2))
        C.append((C2))              
        t2=float((t2))
        T.append(t2)

        C3 =float((C3))
        C.append((C3))
        t3=float((t3))
        T.append(t3)

        C4=float((C4))
        C.append((C4))
        t4=float((t4))
        T.append(t4)
        slope, intercept, r_value, p_value, std_err = stats.linregress(T,C)
        a=(intercept)
        k=slope
        t=(a)/(k)
        unite_con= (unite_con)# for zero
        unite_time= (unite_time)# for zero
        unit_k=(unite_con,'/',unite_time)
        unit_k= ((''.join(unit_k)))

        plt.figure()
        plt.xlabel(unite_time)
        plt.ylabel(unite_con)

        plt.plot(T, C )
        plt.title('Zero order reaction')
        print("The rate constant is", k,' ',unit_k, '\nThe half-life is ', t," ", unite_time,'\nThe initial conccenteration is ', a,' ', unite_con,'\nThe cofficent correlation is ',r_value,'\nthe stander deviation is ', std_err)


        return
    except:
        print('Fill all requirement boxes , if this massage still appears meaning there is mistake in your details')

interact(Z,unite_time= "Type time unite",unite_con= 'Type concenteration unite',  C1='Type only number',t1='Type only number',C2='Type only number',t2='Type only number',C3='Type only number',t3='Type only number',C4='Type only number',t4='Type only number');

    ######################################################## zero ORDER
    
################################################################
btnZ = widgets.Button(description='Click for another zeroth Reaction Order', layout=Layout(width='90%', height='80px'))
display(btnZ)


def my_eventZ_handler(btnZ_object):

    w=widgets.Text(value='Zero  Reaction Order', disabled=True)
    display(w)
    interact(Z,unite_time= "Type time unite",unite_con= 'Type concenteration unite',  C1='Type only number',t1='Type only number',C2='Type only number',t2='Type only number',C3='Type only number',t3='Type only number',C4='Type only number',t4='Type only number');

btnZ.on_click(my_eventZ_handler)






################################################################


# # First Reaction Order

# In[7]:


#First Reaction Order
######################################
w=widgets.Text(value='First  Reaction Order', disabled=True)
display(w)


print('\nA first-order reaction means that proceeds at a rate that depends linearly on only one reactant concentration   \n')
listOfImageNames = [ "first.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))
print('\nC1, C2, C3, and C4 represent[A] of the reactant which is wanted to find its order ')
print('\nt1, t2, t3, and t4 represent time [t] from begining reaction until the trial to find rest concenteration ')

def ff(unite_con, unite_time, C1,t1,C2,t2,C3,t3,C4,t4 ):
    # we need two empty list to draw zeroth equation T for time and C for concenteration
    try:
        C=[]
        T=[]
        C1 =float(C1)   
    # we need to take log concenteration 
        C.append(math.log(C1))
        t1= float(t1)
        T.append(t1)

        C2=float((C2))
        C.append(math.log(C2))              
        t2=float((t2))
        T.append(t2)

        C3 =float((C3))
        C.append(math.log(C3))
        t3=float((t3))
        T.append(t3)

        C4=float((C4))
        C.append(math.log(C4))
        t4=float((t4))
        T.append(t4)
        unite_con= str(unite_con)# for first
        unite_time= str(unite_time)# for first
        unit_k=('1/',(unite_time))
        unit_k= ((''.join(unit_k)))

        
        if C1 and t1 and C2 and t2  and C3 and t3 and C4 and t4>=1:
            slope, intercept, r_value, p_value, std_err = stats.linregress(T,C)
            a=math.exp(intercept)
            k=-slope
            t=(math.log(2))/(k)
            unite= (u'min\u207B\u00B9')# first 

            plt.figure()
            plt.xlabel(unite_time)
            plt.ylabel(unite_con)

            plt.plot(T, C )
            plt.title('First order reaction')
            plt.figure()
            
            print("The rate constant is", k,' ',unit_k, '\nThe half-life is ', t," ", unite_time,'\nThe initial conccenteration is ', a,' ', unite_con,'\nThe cofficent correlation is ',r_value,'\nThe stander deviation is ', std_err)


            return
    except:
        
        print('Fill all requirement boxes , if this massage still appears meaning there is mistake in your details')

interact(ff,unite_con='mol',unite_time='s', C1='Type only number',t1='Type only number',C2='Type only number',t2='Type only number',C3='Type only number',t3='Type only number',C4='Type only number',t4='Type only number');
############################################################SECOND ORDER

################################################################
btnff = widgets.Button(description='Click here for another first Reaction Order', layout=Layout(width='90%', height='80px'))
display(btnff)
def my_eventff_handler(btnff_object):
    
    w=widgets.Text(value='First  Reaction Order', disabled=True)
    display(w)

    interact(ff,unite_con='mol',unite_time='s', C1='Type only concentration number',t1='Type only time number',C2='Type only concentration number',t2='Type only time number',C3='Type only concentration number',t3='Type only time number',C4='Type only concentration number',t4='Type only time number');



btnff.on_click(my_eventff_handler)



# # Second Reaction Order

# In[8]:


#Second Reaction Order

w=widgets.Text(value='Second  Reaction Order', disabled=True)
display(w)

print('\nThe simplest kind of second-order reaction is one whose rate is proportional to the square of the concentration of one reactant. These generally have the form 2A → products. A second kind of third-order reaction has a reaction rate that is proportional to the product of the concentrations of two reactants.   \n')
listOfImageNames = [ "second.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

print('\nC1, C2, C3, and C4 represent[A] of the reactor which is wanted to find its order and their units must be Mole  in this program')
print('\nt1, t2, t3, and t4 represent time[t] from begining reaction until the trial to find rest concenteration  and their units must be Minutes  in this program')
print('\nIf the reaction has two reactors it must be costant one of these reactor or they have same concentration ')


################################################################
def Sc(unite_con,unite_time,C1,t1,C2,t2,C3,t3,C4,t4):
    try:
        C=[]
        T=[]

        C1 =float(C1)   
        C.append(1/(C1))
        t1= float(t1)
        T.append(t1)

        C2=float((C2))
        C.append(1/(C2))              
        t2=float((t2))
        T.append(t2)

        C3 =float((C3))
        C.append(1/(C3))
        t3=float((t3))
        T.append(t3)

        C4=float((C4))
        C.append(1/(C4))
        t4=float((t4))
        T.append(t4)
        unite_con= str(unite_con)# for first
        unite_time= str(unite_time)# for first
        unit_k=('1/',unite_time,'*', unite_con)
        unit_k= ((''.join(unit_k)))


        if C1 and t1 and C2 and t2 and C3 and t3 and C4 and t4>=1:
            slope, intercept, r_value, p_value, std_err = stats.linregress(T,C)
            a=1/(intercept)
            k=slope
            t=(1)/(k*a)

            plt.figure()
            plt.xlabel(unite_time)
            plt.ylabel(unite_con)
  
            plt.plot(T, C )
            plt.title('Second order reaction')

            
            print("The rate constant is", k,' ',unit_k, '\nThe half-life is ', t," ", unite_time,'\nThe initial conccenteration is ', a,' ', unite_con,'\nThe cofficent correlation is ',r_value,'\nThe stander deviation is ', std_err)



    except:
        
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")

interact(Sc,unite_con='mol',unite_time='s', C1='Type only concentration number',t1='Type only time number',C2='Type only concentration number',t2='Type only time number',C3='Type only concentration number',t3='Type only time number',C4='Type only concentration number',t4='Type only time number');
###################################################
btnSc = widgets.Button(description='Second Reaction Order(all the same reactant affecting on rate constant have same concenteration)', layout=Layout(width='90%', height='80px'))
display(btnSc)

def my_eventSc_handler(btnSc_object):
    w=widgets.Text(value='Second  Reaction Order', disabled=True)
    display(w)


    interact(Sc,unite_con='type concentration unit',unite_time='type unite time', C1='Type only number',t1='2',C2='Type only number',t2='Type only number',C3='Type only number',t3='Type only number',C4='Type only number',t4='Type only number');

btnSc.on_click(my_eventSc_handler)


# # Second Order Reaction with multiple reactants

# In[9]:


#333333333333333two reactants
w=widgets.Text(value='Second Order Reaction with multiple reactants', disabled=True)
display(w)
listOfImageNames = [ "secondm.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

print('k_A and k_B indicate to a and b costant rate for A and B raectant, respectively ')
print('A_0 and B_0 indicate to [A0] and[B0] initial concenteration of A and B reactants, respectively')
print('C_Ax and C_Bx inidcate to [A] and [B] concentration of A and B in time tx thus x indicates to trial number')

def Scc(n,unite_con, unite_time, k_A,k_B,A_0,B_0, C_A1,C_B1,t1,C_A2,C_B2,t2,C_A3,C_B3,t3,C_A4,C_B4,t4):
    try:
        T=[]
        b=[]
        y=[]

        B=[]#C.B
        B1=[]#1/C
        T=[]
        n=float((n))
        k_A=float((k_A))
        k_B=float((k_A))
        A_0=float(A_0)
        A_10=1/A_0
        B_0=float(B_0)
        B_0=1/B_0
        CC=((k_B*A_0)-(k_B*A_0))
        CC0=math.log(A_0/B_0)

        C_A1 =float(C_A1) 
        C_B1 =float(C_B1)
        x1= math.log(float(C_A1/C_B1))
        b.append(x1)
        t1= float(t1)
        T.append((t1))
#####################################
        C_A2=float((C_A2))
        C_B2 =float(C_B2)  
        B.append(1/(C_B2))
        x2= math.log(C_A2/C_B2)    
        b.append(x2)

        t2=float(((t2)))
        T.append(t2)
                 
####################################################################
     
        C_A3 =float((C_A3))
        C_B3 =float(C_B3)   
        x3= math.log(C_A3/C_B3)    
        b.append(x3)
        t3=float((t3))
        T.append((n-1)*t3)
     ################################################################   
        
        C_A4=float((C_A4))
        C_B4 =float(C_B4)   
        x4= math.log(C_A4/C_B4) 
        b.append(x4)
                 
        t4=float((t4))
                 

##########################################
        T.append((n-1)*t4)
        for i in T:
            i=i*CC0
            y.append(i)
        unite_con= str(unite_con)# for first
        unite_time= str(unite_time)# for first

                #slope, intercept, r_value1, p_value, std_err = stats.linregress(F,T)
        slope, intercept, r_value1, p_value, std_err = stats.linregress(b,y)

        r1= (r_value1)

        k= float(slope)

            
        t3=float(((2-((k_B)*(A_0)))/(k_A*(B_0))))
        t3=math.log(abs(t3))
        t33 = float(k_B)*(float(t3))
        
        t=float(t3/t2)
        

        plt.figure()
        plt.xlabel(unite_time)
        plt.ylabel(unite_con)

        plt.plot(b, y )
        plt.title('Second order reaction')

        unit_k=('1/',unite_time+unite_con)
        unit_k= ((''.join(unit_k)))

        print("The rate constant is", k,' ',unit_k, '\nThe half-life is ', t," ", unite_time,' ','\nThe cofficent correlation is ',r1,'\nThe stander deviation is ', std_err)

    
        return 
    except:
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")

interact(Scc,n='Type chemical order > 2', unite_con='type reactant concenteration unite', unite_time='type time unite', k_A='Type A reactant constant rate', k_B='Type B reactant constant rate',A_0='Type A initial concenteration',B_0='Type B initial concenteration', C_A1='Type A reactant concenteration', C_B1='Type A reactant concenteration',t1='Type time',C_A2='Type A reactant concenteration', C_B2='Type B reactant concenteration',t2='Type time',C_A3='Type A reactant concenteration',C_B3='Type B reactant concenteration',t3='Type time',C_A4='Type A reactant concenteration', C_B4='Type B reactant concenteration',t4='Type time');


#########################Type only number####THIRD ORDER
btnScc = widgets.Button(description='Click here for another second Reaction Order(two reactants affecting on rate constant have different concenteration)', layout=Layout(width='90%', height='80px'))
display(btnScc)

def my_eventScc_handler(btnScc_object):

    w=widgets.Text(value='Second Order Reaction with multiple reactants', disabled=True)
    display(w)

    interact(Scc,n='2', unite_con='type reactant concenteration unite', unite_time='type time unite', k_A='Type A reactant constant rate', k_B='Type B reactant constant rate',A_0='Type A initial concenteration',B_0='Type B initial concenteration', C_A1='Type A reactant concenteration', C_B1='Type B reactant concenteration',t1='Type time',C_A2='Type A reactant concenteration', C_B2='Type B reactant concenteration',t2='Type time',C_A3='Type A reactant concenteration',C_B3='Type B reactant concenteration',t3='Type time',C_A4='Type A reactant concenteration', C_B4='Type B reactant concenteration',t4='Type time');

btnScc.on_click(my_eventScc_handler)

#https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Kinetics/02%3A_Reaction_Rates/2.08%3A_Second-Order_Reactions


# # Third  Reaction Order

# In[10]:


listOfImageNames = [ "third.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

print('\nC1, C2, C3, and C4 indicate to [A]t  concentration of the reactant which is wanted to find its order and their units must be Mole  in this program')
print('\nt1, t2, t3, and t4 indicate to (t) time from begining reaction until the trial to find rest concenteration  and their units must be Minutes  in this program')


#########################Type only number####THIRD ORDER

def RDd(C1,t1,C2,t2,C3,t3,C4,t4):
    try:
        C=[]
        T=[]

        C1 =float(C1)   
        C.append(1/(C1**2))
        t1= float(t1)
        T.append(t1)

        C2=float((C2))
        C.append(1/(C2**2))              
        t2=float((t2))
        T.append(t2)

        C3 =float((C3))
        C.append(1/(C3**2))
        t3=float((t3))
        T.append(t3)

        C4=float((C4))
        C.append(1/(C4**2))
        t4=float((t4))
        T.append(t4)
        if  C1 and t1 and C2 and t2 and C3 and t3 and C4 and t4>=1:

            slope, intercept, r_value, p_value, std_err = stats.linregress(T,C)
            a=1/(intercept)
            a=math.sqrt(a)
            k=2*slope
            t=(3)/(k*(a**2))
            unite= (u'Mol\u207B\u00B2'  u'min\u207B\u00B9')# third

            plt.figure()
            plt.xlabel("Minutes")
            plt.ylabel("1/(a-x)")

            plt.plot(T, C )
            plt.title('Third order reaction')


            print("The rate constant is", k,'', unite, '\nThe half-life is ', t,'min \nThe initial conccenteration is ', a, 'Mol \nTthe cofficent correlation is',r_value,'\nThe stander deviation is ', std_err)
        return 
    except:
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")

interact(RDd,unite_con='mol',unite_time='s', C1='Type only concentration number',t1='Type only time number',C2='Type only concentration number',t2='Type only time number',C3='Type only concentration number',t3='Type only time number',C4='Type only concentration number',t4='Type only time number');

##################Nth Order 
################################################################
btnrdd = widgets.Button(description='Click here for another third Reaction Order(all the  reactant affecting on rate constant have same concenteration)', layout=Layout(width='90%', height='80px'))
display(btnrdd)

def my_eventrd_handler(btnrd_object):

    w=widgets.Text(value='Third  Reaction Order', disabled=True)
    display(w)
    print('\nThe simplest kind of third-order reaction is one whose rate is proportional to the power three of the concentration of one reactant. A second kind of third-order reaction has a reaction rate that is proportional to the product of the concentrations of three reactants. \n')

    interact(RDd,unite_con='mol',unite_time='s', C1='Type only concentration number',t1='Type only time number',C2='Type only concentration number',t2='Type only time number',C3='Type only concentration number',t3='Type only time number',C4='Type only concentration number',t4='Type only time number');

btnrdd.on_click(my_eventrd_handler)
#####################################


# # Third  Reaction Order two reactants hacing different concentration affect on its rate

# In[11]:


########################################
w=widgets.Text(value='Third  Reaction Order', disabled=True)
display(w)

print('k_A and k_B indicate to costant rate for A and B raector, respectively ')
print('A_0 and B_0 indicate to initial concenteration of A and B reactants, respectively')
print('C_Ax and C_Bx inidcate to A and B concentration of A and B in time tx thus x indicates to trial number')

print('\nThe simplest kind of third-order reaction is one whose rate is proportional to the power three of the concentration of one reactant. A second kind of third-order reaction has a reaction rate that is proportional to the product of the concentrations of three reactants. \n')

def THt(n,conc_unit,time_unit, k_A,k_B,A_0,B_0, C_A1,C_B1,t1,C_A2,C_B2,t2,C_A3,C_B3,t3,C_A4,C_B4,t4):
    try:
        
       
        C0=[]
        C=[]#C.A
        C1=[]#1/C
        C2=[]
        B0=[]
        F=[]
        x=[]

        B=[]#C.B
        B1=[]#1/C
        T=[]
        n=float((n))
        time_unit=str(time_unit)
        conc_unit=str(conc_unit)
        k_A=float((k_A))
        k_B=float((k_A))
        A_0=float(A_0)
        A_10=1/A_0
        B_0=float(B_0)
        B_0=1/B_0
        CC=((k_A*B_0)-(k_B*A_0)**2)
        CC0=((k_A*B_0)-(k_B*A_0))

        C_A1 =float(C_A1) 
        C0.append(C_A1)
        m= (1/(C_A1))
        p=m-A_10
        f1=p/CC0
        
        C_B1 =float(C_B1) 
        B0.append(C_B1)
        B.append(1/(C_B1))

        ####################################
        b=(C_A1*B_0)/(C_B1*A_0)
        b=math.log(b)
        b=f1+(k_B*b)
        x.append(b)


        t1= float(t1)
        T.append((n-1)*t1)
#####################################
        C_A2=float((C_A2))
        C0.append(C_A2)
        C.append(1/(C_A2))
        m= (1/(C_A2))
        p=m-A_10
        f2=p/CC0

        C_B2 =float(C_B2)  
        B0.append(C_B2)
        B.append(1/(C_B2))

        b=(C_A2*B_0)/(C_B2*A_0)
        b=math.log(b)
        b=f2+(k_B*b)
        x.append(b)

####################################################################
        t2=float(((t2)))
        T.append((n-1)*t2)

        C_A3 =float((C_A3))
        C0.append(C_A3)
        m= (1/(C_A3))
        p=m-A_10
        f3=p/CC0


        C.append(1/(C_A3))
        
        C_B3 =float(C_B3)   
        B.append(1/(C_B3))
        B0.append(C_B3)
        b=(C_A3*B_0)/(C_B3*A_0)
        b=math.log(b)
        b=f3+(k_B*b)
        x.append(b)


     ################################################################   
        t3=float((t3))
        T.append((n-1)*t3)

        C_A4=float((C_A4))
        C0.append(C_A4)
        m= (1/(C_A4))
        p=m-A_10
        f4=p/CC0

        C.append(1/(C_A4))
        
        C_B4 =float(C_B4)   
        B.append(1/(C_B4))
        B0.append(C_B4)
        b=(C_A4*B_0)/(C_B4*A_0)
        b=math.log(b)
        b=f4+(k_B*b)
        x.append(b)
        t4=float((t4))
        T.append((n-1)*t4)
        
                
        #slope, intercept, r_value1, p_value, std_err = stats.linregress(F,T)
        slope, intercept, r_value1, p_value, std_err = stats.linregress(x,T)

        r1= (r_value1)

        k= float(slope)

        t1=float(k*(A_0)*(B_0*k_A)-(A_0*k_B))
        t1=1/t1
            
        t2=float(((k*((k_A*(B_0)-k_B*(A_0))**2))))
        t3=float(((2-k_B)*(A_0))/(k_A*(B_0)))
        t3=math.log(abs(t3))
        t3=k_B*t3
        
        t=float(t3/t2)
        t=float(t1-t)

        plt.figure()
        plt.xlabel(time_unit)
        plt.ylabel(conc_unit)

        plt.plot(x, T )
        plt.title('nth order reaction')

        print ("The rate constant is", k , '\nThe Half-Life is ', t,' min \nThe cofficent correlation is',r1,' \nThe stander deviation is ', std_err)
    
        return  
    except:
        
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")

interact(THt,n='3',conc_unit='mol', time_unit='sec', k_A='Type A reactant constant rate', k_B='Type B reactant constant rate',A_0='Type A initial concenteration',B_0='Type B initial concenteration', C_A1='Type A reactant concenteration', C_B1='Type A reactant concenteration',t1='Type time',C_A2='Type A reactant concenteration', C_B2='Type B reactant concenteration',t2='Type time',C_A3='Type A reactant concenteration',C_B3='Type B reactant concenteration',t3='Type time',C_A4='Type A reactant concenteration', C_B4='Type B reactant concenteration',t4='Type time');

btnTht = widgets.Button(description='Click here for another third Reaction Order(two reactants affecting on rate constant have different concenteration)', layout=Layout(width='90%', height='80px'))

display(btnTht)

def my_eventTht_handler(btnTht_object):

    w=widgets.Text(value='Third  Reaction Order', disabled=True)
    display(w)

    interact(THt,n='3',conc_unit='mol', time_unit='sec', k_A='Type A reactant constant rate', k_B='Type B reactant constant rate',A_0='Type A initial concenteration',B_0='Type B initial concenteration', C_A1='Type A reactant concenteration', C_B1='Type A reactant concenteration',t1='Type time',C_A2='Type A reactant concenteration', C_B2='Type B reactant concenteration',t2='Type time',C_A3='Type A reactant concenteration',C_B3='Type B reactant concenteration',t3='Type time',C_A4='Type A reactant concenteration', C_B4='Type B reactant concenteration',t4='Type time');

btnTht.on_click(my_eventTht_handler)


# # nTH order 

# In[12]:


print('\nThis for  Reaction order  which is bigger than first order to calculate rate constant, Half-life time, correlation coefficient, and standard deviation    \n')
print('\nC1, C2, C3, and C4 represent rest concentration of the reactor which is wanted to find its order and their units must be Mole  in this program')
print('\nt1, t2, t3, and t4 represent time from begining reaction until the trial to find rest concenteration  and their units must be Minutes  in this program')

def TH(n, C1,t1,C2,t2,C3,t3,C4,t4):
    try:
        C=[]
        T=[]
        n=float((n))
        C1 =float(C1)   
        C.append(1/(C1**(n-1)))
        t1= float(t1)
        T.append((n-1)*t1)

        C2=float((C2))
        C.append(1/(C2**(n-1)))              
        t2=float(((t2)))
        T.append((n-1)*t2)

        C3 =float((C3))
        C.append(1/(C3**(n-1)))
        t3=float((t3))
        T.append((n-1)*t3)

        C4=float((C4))
        C.append(1/(C4**(n-1)))
        t4=float((t4))
        T.append((n-1)*t4)
        if C1 and t1 and C2 and t2 and C3 and t3 and C4 and t4>=1:

            slope, intercept, r_value, p_value, std_err = stats.linregress(T,C)
            a=(1/intercept)
            a=math.exp(a)
            a=(n-1)*a
            k=(n-1)*slope
            t=((2**(n-1))-1)/((n-1)*(k)*(a**(n-1)))

            plt.figure()
            plt.xlabel("Minutes")
            plt.ylabel("(a-x)")

            plt.plot(T, C )
            plt.title('nth order reaction')

            print ("The rate constant is", k , '\nThe Half-Life is ', t,' min \nThe initial conccenteration is ', a, 'Mol \nThe cofficent correlation is',r_value,' \nThe stander deviation is ', std_err)
    
            return 
    except:
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")
        
interact(TH,n='Type only number', C1='Type only number',t1='Type only number',C2='Type only number',t2='Type only number',C3='Type only number',t3='Type only number',C4='Type only number',t4='Type only number');


btnNTH = widgets.Button(description='NTH  Reaction Order\n(all the same reactant affecting on rate constant have same concenteration)', layout=Layout(width='90%', height='80px'))
display(btnNTH)



def my_eventFF_handler(btnNTH_object):

    w=widgets.Text(value='Click here for another nTH  Reaction Order', disabled=True)
    display(w)

    interact(TH,n='2', C1='1',t1='2',C2='3',t2='4',C3='4',t3='5',C4='5',t4='5');

btnNTH.on_click(my_eventFF_handler)


# # actiation energy activation energy arrhenius equation with two temoerature and two constant rates points 

# In[13]:


print(' Activation Energy is the energy difference between the reactants and the activated complex, also known as transition state. In a chemical reaction, the transition state is defined as the highest-energy state of the system. If the molecules in the reactants collide with enough kinetic energy and this energy is higher than the transition state energy, then the reaction occurs and products form. In other words, the higher the activation energy, the harder it is for a reaction to occur and vice versa.')
listOfImageNames = [ "ea2.png"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

print('\nk1,k2 are constant rate of reaction which occured in different temperatures degres')
print('\nT1,T2 are temperatures degrees in kelvin degree')

def Ea(k1,T1,k2,T2):

    try:
        k1=float((k1))
        T1=float((T1))
        k2=float((k2))
        T2=float((T2))
        k1 and T1 and k2 and T2>1
        k=math.log(k2/k1)
        t=(1/T1)-(1/T2)
        Ea=float((k/t)*(8.314))
        return ('The actiavtion energy for this reaction is', Ea,'KJ/mol')
    except:
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")


interact(Ea,k1="Type only number",T1="Type only number",k2="Type only number",T2="Type only number");








btnEa = widgets.Button(description='"Two-Point Form" of the Arrhenius Equation', layout=Layout(width='90%', height='80px'))
display(btnEa)
def my_eventEa_handler(btnEa_object):


    
        w=widgets.Text(value='Activation Energy', disabled=True)
        display(w)

        print('\nThis will calculate actiavation energy \n')
    
        interact(Ea,k1="1",T1="2",k2="3",T2="4");

btnEa.on_click(my_eventEa_handler)




# # actiation energy activation energy arrhenius equation with four  temoerature and four constant rates points 

# In[14]:


print('Activation Energy is the energy difference between the reactants and the activated complex, also known as transition state. In a chemical reaction, the transition state is defined as the highest-energy state of the system. If the molecules in the reactants collide with enough kinetic energy and this energy is higher than the transition state energy, then the reaction occurs and products form. In other words, the higher the activation energy, the harder it is for a reaction to occur and vice versa.')
listOfImageNames = [ "ea.JPG"]
for imageName in listOfImageNames:
    display(Image(filename=imageName))

print('\nk1,k2,k3,4 are constant rate of reaction which occured in different temperatures degres')
print('\nT1,T2,T3,T4 are temperatures degrees in kelvin degree')
def Eaa(k1,T1,k2,T2, k3,T3,k4,T4):
    
    try:
        
        T0=[]
        k0=[]
        T=[]
        k=[]

        k1=float((k1))
        k1=math.log(k1)
        k0.append(k1)
        T1=float((T1))
        T1=(1/T1)
        T0.append(T1)


        k2=float((k2))
        k2=math.log(k2)
        k0.append(k2)
        T2=float((T2))
        T2=(1/T2)
        T0.append(T2)



        k3=float((k3))
        k3=math.log(k3)
        k0.append(k3)
        
        T3=float((T3))
        T3=(1/T3)
        T0.append(T3)


        k4=float((k4))
        k4=math.log(k4)
        k0.append(k4)
        
        T4=float((T4))
        T4=(1/T4)
        T0.append(T4)


        

            
        slope, intercept, r_value, p_value, std_err = stats.linregress(T0,k0)
        Ea= slope*8.314
        plt.figure()

        plt.xlabel("1/T")
        plt.ylabel("Ln(k)")
        plt.plot(T0, k0)
        plt.title('The Arrhenius Equation')


        print('The actiavtion energy for this reaction is', Ea,'KJ/mol')
        
        return 
    except:
        print("Fill all requirement boxes , if this massage still appears meaning there is mistake in your details")
interact(Eaa,k1="Type only number",T1="Type only number",k2="Type only number",T2="Type only number", k3="Type only number",T3="Type only number",k4="Type only number",T4="Type only number");
btnEaa = widgets.Button(description='"Variation of the rate constant with temperature" of the Arrhenius Equation', layout=Layout(width='90%', height='80px'))
display(btnEaa)
def my_eventEaa_handler(btnEaa_object):


        print('The activation energy ( Ea ) is the energy difference between the reactants and the activated complex, also known as transition state Source: chem.libretexts')
    
        w=widgets.Text(value='Activation Energy', disabled=True)
        display(w)

        print('\nThis will calculate actiavation energy \n')
    
        interact(Eaa,k1="1",T1="2",k2="3",T2="4", k3="1",T3="2",k4="3",T4="4");

btnEaa.on_click(my_eventEaa_handler)


# # find how much current is used to produce specific amount of specific metal  in Galvanic Cell

# In[15]:


w=widgets.Text(value='find period time to electroplate a flute', disabled=True)
display(w)

print("This program will find how much current is used to produce specific amount of specific metal  in Galvanic Cell.")
print("\nch_element box: The symbol of a chemical element. " )   
print("\nmoles_tr box:  The moles of electrons transferred. " )   
print("\nAmount_gram box: type amount of chemcial material in gram unit. " ) 
print("\nTime box: type time in second unit. " )   


def GTV( ch_element,  Amount_gm,moles_tr, time):


    try:
        ch_element=str(ch_element)
        moles_tr= float(moles_tr)
        Amount_gm = float(Amount_gm )
        time=float(time)
        #chemlib.electrochemistry.electrolysis(element: str, n: int, **kwargs)
        z= electrolysis(ch_element, float(moles_tr),  grams= float(Amount_gm) , seconds =float(time))

        return   z

    except:
        print("Fill all requirement boxes with their requirements , if this massage still appears meaning there is mistake in your details")
interact(GTV,ch_element='Cu', moles_tr= '2', time= '25 ', Amount_gm= '600');
btnelecttGTV = widgets.Button(description='click here to Find how much current is used to produce specific amount of  metal  in Galvanic Cell', layout=Layout(width='90%', height='80px'))
display(btnelecttGTV)
def my_eventbtnelecttGTV_handler(btnelecttGTV_object):


    
        w=widgets.Text(value='find period time to electroplate a flute', disabled=True)
        display(w)
    
        interact(GTV,ch_element='Cu', moles_tr= '2', time= '25 ', Amount_gm= '600');

btnelecttGTV.on_click(my_eventbtnelecttGTV_handler)
# Reference: https://chemlib.readthedocs.io/en/latest/electrochemistry.html#galvanic-voltaic-cells


# # #This program will find period time to electroplate a flute
# 

# In[16]:


#This program will find period time to electroplate a flute
from chemlib import electrolysis
from chemlib import Galvanic_Cell
from ipywidgets import interact, interactive, fixed, interact_manual
w=widgets.Text(value='find period time to electroplate a flute', disabled=True)
display(w)

print("This program will find period time to electroplate a flute")
print("\nch_element box: The symbol of a chemical element. " )   
print("\nmoles_tr box:  The moles of electrons transferred. " )   
print("\nAmount_gram box: type amount of chemcial material in gram unit. " )   

def GTt( ch_element,moles_tr, applying_current, Amount_gm):

    try:
        ch_element=(str(ch_element))
        moles_tr= float(moles_tr)
        applying_current =float(applying_current)
        Amount_gm = float(Amount_gm )
        #chemlib.electrochemistry.electrolysis(element: str, n: int, **kwargs)
         
        return   electrolysis(ch_element, float(moles_tr), amps = float(applying_current), grams= float(Amount_gm ))

    except:
        print("Fill all requirement boxes with Integer numbers , if this massage still appears meaning there is mistake in your details")


interact(GTt,ch_element='Cu', moles_tr= '2', applying_current= '100', Amount_gm = '600');
btnelectt = widgets.Button(description='Find period time to electroplate a flute', layout=Layout(width='90%', height='80px'))
display(btnelectt)
def my_eventbtnelectt_handler(btnelectt_object):


    
        w=widgets.Text(value='Click here to find period time to electroplate ', disabled=True)
        display(w)
    
        interact(GTt,ch_element='Cu', moles_tr= '2', applying_current= '100', Amount_gm = '600');

btnelectt.on_click(my_eventbtnelectt_handler)
# Reference: https://chemlib.readthedocs.io/en/latest/electrochemistry.html#galvanic-voltaic-cells


# # all these previous pictures from google 
