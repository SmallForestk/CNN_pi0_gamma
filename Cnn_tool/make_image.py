import numpy as np
from tqdm import tqdm

#viewpointによって作成するhitmapの種類を変える
def hitmap(arr, viewpoint=0):
    output_hitmap = []
    for i in tqdm(range(int(arr[:,0].max())+1)):
        arr_tmp = arr[arr[:,0]==i]
        image_tmp = np.full((100, 100), 0)
        if viewpoint==0:# zhitmap
            x_tmp = arr_tmp[:, 2]
            y_tmp = arr_tmp[:, 3]
        elif viewpoint==1:# xhitmap
            x_tmp = arr_tmp[:, 2]
            y_tmp = arr_tmp[:, 1]
        elif viewpoint==2:# yhitmap
            x_tmp = arr_tmp[:, 3]
            y_tmp = arr_tmp[:, 1]
        for n in range(len(arr_tmp)):
            image_tmp[int(x_tmp[n])][int(y_tmp[n])] += arr_tmp[n, 4]
        output_hitmap.append(image_tmp)
    return np.array(output_hitmap)