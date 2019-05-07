import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import cufflinks as cf

#init_notebook_mode(connected=True)
#cf.go_offline()

#----------------

df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
print(df.head())