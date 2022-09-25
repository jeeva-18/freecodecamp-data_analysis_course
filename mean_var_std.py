import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  a=np.array(list)
  A = a.reshape(3,3)
  m1 = a.mean()
  v1 = a.var()
  s1 = a.std()
  mn1 = a.min()
  mx1 = a.max()
  sm1 = a.sum()
  m2 = A.mean(axis=0)
  v2 = A.var(axis=0)
  s2 = A.std(axis=0)
  mn2 = A.min(axis=0)
  mx2 = A.max(axis=0)
  sm2 = A.sum(axis=0)
  m3 = A.mean(axis=1)
  v3 = A.var(axis=1)
  s3 = A.std(axis=1)
  mn3 = A.min(axis=1)
  mx3 = A.max(axis=1)
  sm3 = A.sum(axis=1)
  

  calculations = {
  'mean': [m2.tolist(),m3.tolist(),m1],
  'variance': [v2.tolist(),v3.tolist(),v1],
  'standard deviation': [s2.tolist(),s3.tolist(),s1],
  'max': [mx2.tolist(),mx3.tolist(),mx1],
  'min': [mn2.tolist(),mn3.tolist(),mn1],
  'sum': [sm2.tolist(),sm3.tolist(),sm1]
}

  return calculations