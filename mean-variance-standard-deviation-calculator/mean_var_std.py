import numpy as np

def calculate(li):
    if(len(li))!=9:
        raise ValueError("List must contain nine numbers.")
    _x=np.matrix([li[:3] ,li[3:6], li[6:9]])
    calculations={
        'mean': [_x.mean(0)[0].tolist()[0],[k.tolist()[0][0] for k in _x.mean(1)],_x.mean()],
        'variance': [_x.var(0)[0].tolist()[0],[k.tolist()[0][0] for k in _x.var(1)],_x.var()],
        'standard deviation': [_x.std(0)[0].tolist()[0],[k.tolist()[0][0] for k in _x.std(1)],_x.std()],
        'max': [_x.max(0)[0].tolist()[0],[k.tolist()[0][0] for k in _x.max(1)],_x.max()],
        'min': [_x.min(0)[0].tolist()[0],[k.tolist()[0][0] for k in _x.min(1)],_x.min()],
        'sum': [_x.sum(0)[0].tolist()[0],[k.tolist()[0][0] for k in _x.sum(1)],_x.sum()]
        }
    return calculations
print(calculate([0,1,2,3,4,5,6,7,8]))
print(calculate([0,1,2,3,4,5,3,7,9]))