import numpy

def myfunction(arg1):
    
    return arg1
import networkx as nx
import numpy as np
# pip install numpy tifffile cloud-volume
import numpy as np
import tifffile
from cloudvolume import CloudVolume

vol = CloudVolume(
    "s3://open-neurodata/kasthuri/kasthuri11/image", mip=0, use_https=True
)

# load data into numpy array
cutout = vol[11264:11776, 13312:13824, 912:928]

# save cutout as TIFF
tifffile.imwrite("data.tiff", data=np.transpose(cutout))

print(nx.info(graph))
graph2 = nx.Graph(graph)
nx.average_clustering(graph2)
#global efficiency 
ugraph= nx.to_undirected(graph)
nx.global_efficiency(ugraph)


#Mean Absolute Deviation 
# importing pandas module  
import pandas as pd  
    
# importing numpy module  
import numpy as np  
    
# creating list from degree centrality 
list =[0.05933852140077821,  0.0048638132295719845, 0.009727626459143969, 0.0038910505836575876, 0.014591439688715954, 0.0019455252918287938, 0.14883268482490272, 0.0019455252918287938,
0.0038910505836575876, 0.0029182879377431907, 0.021400778210116732, 0.0019455252918287938, 0.007782101167315175, 0.0009727626459143969, 0.033073929961089495, 0.0009727626459143969, 0.008754863813229572, 0.0019455252918287938, 0.020428015564202335, 0.0019455252918287938, 0.011673151750972763, 0.0038910505836575876, 0.01264591439688716, 0.008754863813229572] 
  
# creating series 
series = pd.Series(list) 
  
# calling .mad() method 
result = series.mad() 
  
# display 
result 




