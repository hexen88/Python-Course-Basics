import pandas as pd
import numpy as np

listaval = np. random.randint(0,100,50).reshape(5,10)
# se puede hacer también listaval.resize(5,10)
print(listaval)

df= pd.DataFrame(listaval)

print(df[df > 50])