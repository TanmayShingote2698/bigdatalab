import numpy as np
sales_data = np.array([ [150, 200, 250, 300, 400, 350, 500],[120, 180, 210, 240, 310, 280, 400],[100, 130, 190, 220, 300, 270, 350],[80,  90,  150, 180, 240, 220, 300],[50,  60,  80,  100, 130, 120, 180]])
print("shape of the array is: ",np.shape(sales_data))
print("Dimension of the array is: ",np.ndim(sales_data))
print("datatype of the array is: ",sales_data.dtype)
print("total number of elements in the sales_data array",sales_data.size)
print("total memory (in bytes) used by the sales_data array",sales_data.size* sales_data.itemsize)
print("sales data for Product 3 on Day 4",sales_data[3][3])
print("sales data for Product1  ",sales_data[1])
# print("sales data for Product5",np.)




