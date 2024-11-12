import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import json
import Global as gl
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Set a seed for reproducibility
seed_value = gl.seed_value
np.random.seed(seed_value)
#________________________________________________
eps=gl.eps
h=gl.h
step=gl.step
x1,x2,x3,x4=gl.x_0
#In minutes
macrostep=gl.macrostep
#In seconds
microstep=gl.microstep 
#________________________________________________

#microscopic operator
#tau = ((1+k)*30*60)/eps
def Oe(Y_0,A,w,k):
    tau = k/eps
    X_0 = np.array([[np.cos(tau),-np.sin(tau), 0 ,0],
                   [np.sin(tau),np.cos(tau), 0 ,0],
                   [0,0, 1 ,0],
                   [0,0, 0 ,1]]) 
    result =X_0@(w*Y_0+(1-w)*A) +\
          eps * np.array([np.sin(tau),
                        1 - np.cos(tau),
                        x1 * np.sin(tau) + x2 * (np.cos(tau) - 1),
                        x1 * (1 - np.cos(tau)) + x2 * np.sin(tau)]) +\
            (eps**2)*np.array([
                0,
                0,
                1-np.cos(tau),
                tau -np.sin(tau)
            ])
    
    return result
def Xe_Forecast(X,A,w,k,microstep):
    return np.array([Oe(X,A,w,k+step*i) for i in range(int(microstep/step))])

x1,x2,x3,x4 = 0,0,1,1
Y_0 = [0,0,1,1]
A=[0,0,0,0]
w=1
k=1800

file_path1 = 'GenData/Noised/Cut/'+gl.model_name+'.json'  # Replace 'your_file.json' with the actual file path
with open(file_path1, 'r') as file1:
    data1 = json.load(file1)

def Xe_Forecast(X,A,w,k,microstep):
    return np.array([Oe(X,A,w,k+step*i) for i in range(int(microstep/step))])
print(Xe_Forecast(Y_0,A,w,k,0.1).shape)