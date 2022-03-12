import pandas as pd
from tkinter import *
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
from PIL import ImageTk,Image

warnings.filterwarnings('ignore')

### Reading the file to build the model - if you have a bigger dataset its better to train dataset seprate and just upload the model to system to avoid taking to long to predict  ###

df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

## Logistic Regreission only takes numerical values so we have to switch outcome (Attrition into numbers) ##

df['Attrition2'] = df.Attrition.replace({'Yes': 1,'No':0})

### Using outcome Attrition into outcome and using Age , ETC ... for predicting ### 

y = df['Attrition2']

X = df[['Age','DistanceFromHome','EnvironmentSatisfaction','HourlyRate','JobSatisfaction','PerformanceRating']]

X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.30, random_state=42)

log_mod = LogisticRegression()

log_mod.fit(X_train, y_train)
    
### function that will run on button click ###

def predicting():
    try :
        Age = int(e1.get())
        DistanceFromHome = int(e2.get())
        EnvironmentSatisfaction = int(e3.get())
        HourlyRate = int(e4.get())
        JobSatisfaction = int(e5.get())
        PerformanceRating = int(e6.get())
        Test_conf = log_mod.predict_proba([[Age,DistanceFromHome,EnvironmentSatisfaction,HourlyRate,JobSatisfaction,PerformanceRating]])
        ix = Test_conf.argmax(1).item()
        if ix == 0:
            myLabel = Label(root,text = f'Predicted Employee Will most Likely Not Leave and confidence = {Test_conf[0,ix]:.2%}')
            myLabel.pack()
        elif ix == 1:
            myLabel2 = Label(root,text = f'Predicted Employee Will most Likely Leave and confidence = {Test_conf[0,ix]:.2%}')
            myLabel2.pack()
    except:
        myLabel3 = Label(root,text = 'Please fill input boxes first')
        myLabel3.pack()


### Creating our canvas ###

root = Tk()
root.title('Predicting Employee Churn using Logistic Regression')
root.geometry("400x600")

### uncomment and add your img if you need to add an img was resized to fit the geometry of the canvas ###
# my_img = Image.open("insert your img path here")
# resized_image= my_img.resize((400,205), Image.ANTIALIAS)
# New_img = ImageTk.PhotoImage(resized_image)
# my_label = Label(image = New_img)
# my_label.pack()


## Creating the boxes for X input that will be running the prediction on ##

Box1 = tk.Label(root,text = "Enter Employee Age")
Box1.pack()

e1 = tk.Entry(root)
e1.pack()

Box2 = tk.Label(root,text = "Distance From Home")
Box2.pack()

e2 = tk.Entry(root)
e2.pack()

Box3 = tk.Label(root,text = "EnvironmentSatisfaction")
Box3.pack()

e3 = tk.Entry(root)
e3.pack()

Box4 = tk.Label(root,text = "HourlyRate")
Box4.pack()

e4 = tk.Entry(root)
e4.pack()

Box5 = tk.Label(root,text = "JobSatisfaction")
Box5.pack()

e5 = tk.Entry(root)
e5.pack()

Box6 = tk.Label(root,text = "PerformanceRating")
Box6.pack()

e6 = tk.Entry(root)
e6.pack()
    
## button that will fire the predicting function ##

myButton2 = Button(root,command = predicting,text = "Print output")
myButton2.pack()

root.mainloop()
