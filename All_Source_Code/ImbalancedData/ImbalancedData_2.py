from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

features, label = make_blobs(n_samples=[2000,50],\
                             n_features=2,\
                             centers=[(-5,5),(5,5)],\
                             random_state=47,cluster_std=3)
min1, max1 = features[:,0].min()-1,features[:,0].max()+1
min2, max2 = features[:,1].min()-1,features[:,1].max()+1

x1grid = np.arange(min1,max1,.1)
x2grid = np.arange(min2,max2,.1)

xx, yy = np.meshgrid(x1grid,x2grid)
r1,r2 = xx.flatten(), yy.flatten()
r1,r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))
grid = np.hstack((r1,r2))
model = LogisticRegression()
model.fit(features,label)

plt.figure(figsize=(6,3))
yp = model.predict(grid)
zz = yp.reshape(xx.shape)
plt.contourf(xx,yy,zz,cmap='Paired')
for cv in range(2):
    row = np.where(label==cv)
    plt.scatter(features[row,0],features[row,1],cmap = 'Paired')

plt.tight_layout()
plt.savefig('imbalanced_classification.png')
plt.show()