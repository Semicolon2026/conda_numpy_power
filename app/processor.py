import numpy as np
import pandas as pd

def process_data():
    arr = np.array([10, 20, 30])

    df = pd.DataFrame(arr, columns=["values"])

    print("Numpy version:", np.__version__)
    print(df)
