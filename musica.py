import numpy as np
import pandas as pd

billboard = pd.read_csv('billboard.csv', encoding='ISO-8859-1')
billboard_melt=pd.melt(billboard,id_vars=['year','artist.inverted','track','time','genre','date.entered','date.peaked'],
                       var_name='week',value_name='rank')
billboard_melt['artist.inverted'].unique()
