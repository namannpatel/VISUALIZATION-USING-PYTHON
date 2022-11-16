import pandas as pd
import matplotlib.pyplot as plt
dframe = pd.read_csv("Covid_Vaccine.csv")
doses = (dframe['Total Doses Administered'].head(10))
states = (dframe['State/UT'].head(10))
plt.title("Vaccine Adminstrated")
X=range(len(doses))
plt.bar(X, states)
plt.show()
print(dframe)
