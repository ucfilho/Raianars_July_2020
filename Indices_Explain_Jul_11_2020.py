def Indices(X,BESTo,FOBESTo,BEST,FOBEST,DIo,MAT_INDo,Fun):
  
  nrow,ncol=X.shape
  FOBESTm=1e99
  Fo=MAT_INDo[0,6]    # VALOR Fo   
  CRo=MAT_INDo[0,7]   # VALOR CRo
  QUANT=17 # quantos indices esta fazendo
  MAT_IND=np.zeros((1,QUANT))

  REF=0.1 # REFERENCIA DE DIFERENCAS ENTRE OS ELEMENTOS
  Fitness = np.asarray([Fun(ind) for ind in X])
  XY,BEST_XY,BEST,FOBEST=AvaliaX(X,Fitness)
  
  soma=0
  for j in range(ncol):
    for i in range(nrow):
        Xj=np.mean(X[:,j])
        soma=soma+(X[i,j]-Xj)**2
  DI=(soma/nrow)**0.5
  DIr=DI/DIo
  MAT_IND[0,0]=DI #dispersao
  MAT_IND[0,1]=DIr # dispersao relativa
  MAT_IND[0,2]=SOMA/TOTAL # fracao relativa

  V1=FOBESTo
  V2=FOBEST
  A=2*V2
  if(V1 > A):
    MAT_IND[0,3]=2 # o valor de fobj torna pelo menos duas vezes melhor
  elif (V2==V1):
    MAT_IND[0,3]=0 # o valor de fobj nao altera
  else:
    MAT_IND[0,3]=1 # o valor de fobj melhora mas menos que duas vezes
  
  # MAT_IND[0,4]  # VELOC X
  DELTA=np.amax(abs(BEST-BESTo))
  if( DELTA >REF):
    MAT_IND[0,4]=2 # difere  for i in range(1,len(PARTIC)):
  elif ( DELTA == 0):
    MAT_IND[0,4]=0 # sem diferenca entre as posicoes do xbest entre duas buscas
  else:
    MAT_IND[0,4]=1 # diferenca entre as posicoes  do xbest menor que ref
  
  MAT_IND[0,5]=nrow  # VALOR NP
  nrow,ncol=XY.shape
  MAT_IND[0,8]=XY[0,(ncol-1)] # VALOR fmin
  MAT_IND[0,9]=XY[(nrow-1),(ncol-1)] # VALOR fmax
  # MAT_IND[0,10] # Valor AD_fmin 
  if abs(MAT_IND[0,8]/MAT_IND[0,8])>1:
    MAT_IND[0,10]=1/abs(MAT_IND[0,8])
  else:
    MAT_IND[0,10]=MAT_IND[0,8]/MAT_IND[0,8]
  # MAT_IND[0,11] # Valor AD_fmax
  if abs(MAT_IND[0,9]/MAT_IND[0,9])>1: # tem que pegar primeira
    MAT_IND[0,11]=1/abs(MAT_IND[0,9]) # tem que pegar primeira
  else:
    MAT_IND[0,11]=MAT_IND[0,9]/MAT_IND[0,9] # tem que pegar do anterior

  # MAT_IND[0,12] # DELTA Fobj
  MAT_IND[0,12]=MAT_IND[0,3]-MAT_IND[0,3]  # tem que pegar do anterior
  

  # MAT_IND[0,13] # DELTA Vx
  MAT_IND[0,13]=MAT_IND[0,4]-MAT_IND[0,4]  # tem que pegar do anterior

  # MAT_IND[0,14] # r_fitness
  Fmin=0.05
  if (MAT_IND[0,8]==0):
    MAT_IND[0,14]=Fmin
  elif (MAT_IND[0,9]==0):
    MAT_IND[0,14]=Fmin
  else:
    if abs(MAT_IND[0,9]/MAT_IND[0,8])<1:
      MAT_IND[0,14]=1-abs(MAT_IND[0,9]/MAT_IND[0,8])
    else:
      MAT_IND[0,14]=1-abs(MAT_IND[0,8]/MAT_IND[0,9])

  MAT_IND[0,6]=Fo
  MAT_IND[0,7]=CRo
