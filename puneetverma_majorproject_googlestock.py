
#importing neccessary file to be used

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from statistics import mean
from sklearn import linear_model
google=pd.read_csv("C:\\Users\\Punit Verma\\Desktop\\DESKTOP\\machinelearning\\BCIR-_XEO.csv");         #loading the google stock csv file 
db=pd.DataFrame(google)                                                         #creating dataframe 
print(db.keys())                                                                #it will print the columns name 

#next five line will generating a list of every columnm of csv file 

date=google.Date.tolist()
openn=google.Open.tolist()
high=google.High.tolist()
low=google.Low.tolist()
volume=google.Volume.tolist()


style.use("fivethirtyeight")

#here k will act as a x-axis 
k=[]
for i in range(20):
    k.append(i+1)

#-------------------for the "open" column------------------------------------------------------------------------------------------------------
    
#creating array of columns "open"
xs=np.array(k,dtype=np.float)
ys=np.array(openn,dtype=np.float64)

#this is the function which return the slope and the intercept of the line

def best_fit_slope_and_intercept(xs,ys):
            m=(((mean(xs)*mean(ys))-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs*xs)) )
            b=mean(ys)-m*mean(xs)
            return m,b

m,b=best_fit_slope_and_intercept(xs,ys)                                             # m is the slope and b is the intercept
print(m,b)

regressionline_1=[(m*x)+b for x in xs]                                              #it is creating the line of "open"
predict_x=[]
predict_y=[]
open_p=[]

#this for loop will showthe next fifteen predictive data in a graph with a green color
for i in range(15):
    predict_x.append(i+21)
    predict_y.append((m*predict_x[i])+b)
    plt.scatter(predict_x[i],predict_y[i],color='g')
    
open_p=predict_y                                                                    #creating a copy for making a prediction data frame 
plt.title("open")                                                                   #this will create the title as open 
plt.scatter(xs,ys)                                                                  #defining axis
plt.plot(xs,regressionline_1)
plt.show()                                                                          #display the graph of open 


#-------------------for the "high" column------------------------------------------------------------------------------------------------------

ys=np.array(high,dtype=np.float64)                                                  #creating array of "high" 

m,b=best_fit_slope_and_intercept(xs,ys)                                             # m is the slope and b is the intercept

regressionline_2=[(m*x)+b for x in xs]                                              #it is creating the line of "high"
predict_x2=[]
predict_y2=[]
high_p=[]

#this for loop will showthe next fifteen predictive data in a graph with a green color
for i in range(15):
    predict_x2.append(i+21)
    predict_y2.append((m*predict_x2[i])+b)
    plt.scatter(predict_x2[i],predict_y2[i],color='g')
high_p=predict_y2                                                                   #creating a copy for making a prediction data frame 
plt.title("high")                                                                   #this will create the title as open 
plt.scatter(xs,ys)                                                                  #definig the axis 
plt.plot(xs,regressionline_2)
plt.show()                                                                          #display the "high" graph

#-------------------for the "low" column------------------------------------------------------------------------------------------------------

ys=np.array(low,dtype=np.float64)                                                   #creating array of "low"

m,b=best_fit_slope_and_intercept(xs,ys)                                             # m is the slope and b is the intercept

regressionline_3=[(m*x)+b for x in xs]                                              #it is creating the line of "low"
predict_x3=[]
predict_y3=[]
low_p=[]

#this for loop will showthe next fifteen predictive data in a graph with a green color
for i in range(15):
    predict_x3.append(i+21)
    predict_y3.append((m*predict_x3[i])+b)
    plt.scatter(predict_x3[i],predict_y3[i],color='g')
low_p=predict_y3                                                                    #creating a copy for making a prediction data frame 
plt.title("low")                                                                    #this will create the title as open 
plt.scatter(xs,ys)                                                                  #definig the axis
plt.plot(xs,regressionline_3)
plt.show()                                                                          #display the "high" graph

#-------------------for the "volume" column------------------------------------------------------------------------------------------------------

ys=np.array(volume,dtype=np.float64)                                                #creating array of "low"

m,b=best_fit_slope_and_intercept(xs,ys)                                             # m is the slope and b is the intercept

regressionline_4=[(m*x)+b for x in xs]                                              #it is creating the line of "volume"
predict_x4=[]
predict_y4=[]
volume_p=[]

#this for loop will showthe next fifteen predictive data in a graph with a green color
for i in range(15):
    predict_x4.append(i+21)
    predict_y4.append((m*predict_x4[i])+b)
    plt.scatter(predict_x4[i],predict_y4[i],color='g')
volume_p=predict_y4                                                                      #creating a copy for making a prediction data frame 
plt.title("volume")                                                                 #this will create the title as open 
plt.scatter(xs,ys)                                                                  #definig the axis
plt.plot(xs,regressionline_4)
plt.show()                                                                          #display the "high" graph


#creating a new data frame that show the prediction of the datasets

#creating a dictionary of the predictive data 
prediction={'open':open_p,'high':high_p,'low':low_p,'volume':volume_p}

#data frame is created
google_preiction_stock=pd.DataFrame(prediction)

print("the next fifteen prediction of the data sets is ")
print(google_preiction_stock)                                                       #printing the predictive data of next fifteen days  


