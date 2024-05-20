import numpy as np
from sklearn.tree import DecisionTreeRegressor

# copy in your get_features_targets function here
def get_features_targets(data):
  # complete this function
  features=np.zeros((data.shape[0],4))
  features[:,0]=data['u']-data['g']
  features[:,1]=data['g']-data['r']
  features[:,2]=data['r']-data['i']
  features[:,3]=data['i']-data['z']
  targets=data['redshift']
  return features,targets

# load the data and generate the features and targets
data = np.load('sdss_galaxy_colors.npy')
features, targets = get_features_targets(data)
  
# initialize model
dec_tree=DecisionTreeRegressor()
# train the model
dec_tree.fit(features,targets)
# make predictions using the same features
predictions=dec_tree.predict(features)
# print out the first 4 predicted redshifts
print(predictions[:4])
