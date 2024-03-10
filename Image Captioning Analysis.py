import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px

#Ignore warnings
import warnings
warnings.filterwarnings('ignore')



import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('train.csv')
df.head(20)

df['captions'][15]

from PIL import Image
import io
import ast # this is
def convert_bytes_to_Image(byte_array) :
 return Image.open(io.BytesIO((ast.literal_eval(byte_array)['bytes'])))
image1_byte_array = df['image'][15]
PIL_image = convert_bytes_to_Image(image1_byte_array)
max_size = (300, 300)
resized_image = PIL_image.resize(max_size)
display(resized_image )

import pandas as pd
from PIL import Image
df.shape

df['filename'][15]

df['filename'] = df['filename'].str[13:] #
df['filename'][15]
row_num = 15
l_captions = df['captions'][row_num].replace('[','').replace(']','')
list_captions=[element.strip() for element in l_captions.split('\n')]
[k for k in list_captions]
