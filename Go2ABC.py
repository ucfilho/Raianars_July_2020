# -*- coding: utf-8 -*-
"""ABCOptmi_from_C_language_jul_15_2019.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ucfilho/optim_raianars/blob/master/ABCOptmi_from_C_language_jul_15_2019.ipynb
"""

import numpy as np
from random import randint

def CalcFit(fun):
    result=0
    if(fun>=0):
      result=1/(fun+1)
    else:
      result=1+fabs(fun)
    return result

def function( sol):
  #Schwefel(x):
  x=sol  
  summ=0
  for i in range(len(x)):
    new=x[i]*np.sin((abs(x[i]))**0.5)
    summ=summ+new
    top=(418.9829*len(x)-summ) 
  
  return top;

def BestSource(GlobMin,GlobPars,Foods):
  FoodNumber=len(Foods[:,0])
  D=len(Foods[0,:])
  solution=np.zeros(D)
  for i in range(FoodNumber):
    if (f[i]<GlobMin):
      GlobMin=f[i]
      for j in range(D):
        GlobPars[j]=Foods[i,j]
  return GlobMin,GlobPars,Foods

def init(index,Foods,trial,f,fitness,MIN,MAX):
  D=len(Foods[0,:])
  FoodNumber=len(Foods[:,0])
  solution=np.zeros(D)
  for j in range(D):
    r=np.random.random()
    Foods[index,j]=r*(MAX[j]-MIN[j])+MIN[j]
    solution[j]=Foods[index,j]
    
  f[index]=function(solution)
  fitness[index]=CalcFit(f[index])
  trial[index]=0
  
  return Foods,trial,f,fitness

def initial(fitness,trial,f,Foods,GlobMin,GlobPars,MIN,MAX):
  D=len(Foods[0,:])
  FoodNumber=len(Foods[:,0])
  for i in range(FoodNumber):
    Foods,trial,f,fitness=init(i,Foods,trial,f,fitness,MIN,MAX) 
  GlobMin=f[0]
  for i in range(D):
    GlobPars[i]=Foods[0,i]
  return  f,Foods,GlobMin,GlobPars

def EmployedBees(trial,Foods,MIN,MAX):
  FoodNumber=len(Foods[:,0])
  NP=FoodNumber
  D=len(Foods[0,:])
  solution=np.zeros(D)
  for i in range(FoodNumber):
    r = np.random.random()
    par2chan= int(r*D)
    r = np.random.random()
    neighbour=int(r*D)
    if(neighbour >= NP):
      neighbour=NP-1
      
    while(neighbour==i):
      r = np.random.random()
      neighbour=int(r*FoodNumber)
      if(neighbour >= NP):
        neighbour=NP-1
    for j in range(D):
      solution[j]=Foods[i,j]

    r = np.random.random()
    A=Foods[i,par2chan]
    B=Foods[neighbour,par2chan]
    solution[par2chan]=Foods[i,par2chan]+(A-B)*(r-0.5)*2;
    if (solution[par2chan]<MIN[par2chan]):
      solution[par2chan]=MIN[par2chan]
    if (solution[par2chan]>MAX[par2chan]):
      solution[par2chan]=MAX[par2chan]
    ObjValSol=function(solution)
    FitnessSol=CalcFit(ObjValSol)
    
    if(FitnessSol>fitness[i]):
      trial[i]=0
      for j in range(D):
        Foods[i,j]=solution[j]
      f[i]=ObjValSol
      fitness[i]=FitnessSol
    else:
      trial[i]=trial[i]+1 
      
  return trial,Foods

def CalcProb(fitness,prob):
  FoodNumber=len(fitness)
  maxfit=fitness[0]
  for i in range(1,FoodNumber):    
    if (fitness[i]>maxfit):
      maxfit=fitness[i]
  for i in range(FoodNumber):
    prob[i]=(0.9*(fitness[i]/maxfit))+0.1
  return fitness,prob

def OnlookerBees(trial,Foods,MIN,MAX):
  D=len(Foods[0,:])
  solution=np.zeros(D)
  FoodNumber=len(Foods[:,0])
  i=0
  t=0
  while(t<FoodNumber):
    r = np.random.random()
    if(r<prob[i]): 
      r = np.random.random()
      t=t+1
      par2chan=int(r*D)
      r = np.random.random()
      neighbour=int(r*FoodNumber)

      while(neighbour==i):
        r = np.random.random()
        neighbour=int(r*FoodNumber)
      for j in range(D):
        solution[j]=Foods[i,j]

      r = np.random.random()
      A=Foods[i,par2chan]
      B=Foods[neighbour,par2chan]
      solution[par2chan]=A+(A-B)*(r-0.5)*2

      if (solution[par2chan]<MIN[par2chan]):
              solution[par2chan]=MIN[par2chan]
      if (solution[par2chan]>MAX[par2chan]):
              solution[par2chan]=MAX[par2chan]
      ObjValSol=function(solution)
      FitnessSol=CalcFit(ObjValSol)
              
      if(FitnessSol>fitness[i]):
        trial[i]=0
        for j in range(D):
          Foods[i,j]=solution[j]
        f[i]=ObjValSol
        fitness[i]=FitnessSol
      else:
        trial[i]=trial[i]+1
      i=i+1
      if (i==FoodNumber):
        i=0
  return trial,Foods

def ScoutBees(fitness,f,Foods,trial,MIN,MAX):
  FoodNumber=len(Foods[:,0])
  max_trial=0
  for i in range(1,FoodNumber):
    if (trial[i]>trial[max_trial]):
      max_trial=i
  if(trial[max_trial]>=limit):
    Foods,trial,f,fitness=init(max_trial,Foods,trial,f,fitness,MIN,MAX)
  return trial,Foods


