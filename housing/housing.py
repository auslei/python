#%%
import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

#%%
def fetch_housing_data(housing_url=HOUSING_URL, housing_path = HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close
fetch_housing_data()

#%%
import pandas as pd
import numpy as np

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()

#%%
#housing.head()
#housing.info()
#housing.ocean_proximity.value_counts()
housing.describe()

#%%
#%matplotlib inline
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))

#%% [markdown]
## Stratified Splits
#%%
from sklearn.model_selection import StratifiedShuffleSplit

housing['income_cat'] = np.ceil(housing["median_income"]/1.5)
housing['income_cat'].where(housing['income_cat']<5, 5, inplace=True)

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

for set_ in (strat_test_set, strat_train_set):
    set_.drop('income_cat', axis=1, inplace=True)
#%%

#%% [markdown]
## Visualisation

#%%
housing = strat_train_set.copy()
housing.plot(kind = 'scatter', x = 'longitude', y = 'latitude', alpha=0.1)

#%%
# a bit more complicated data
housing.plot(kind = 'scatter', x = 'longitude', y = 'latitude', alpha=0.4,
s = housing['population']/100, label = 'population', figsize=(10,7),
c = "median_house_value", cmap=plt.get_cmap('jet'), colorbar=True)
plt.legend()

#%% [markdown]
## Corrlation Matrix

#%%
corr_matrix = housing.corr()
corr_matrix['median_house_value'].sort_values(ascending=False)

#%%
from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))

#%%
housing.plot(kind='scatter', x='median_income', y = 'median_house_value', alpha = 0.1)

#%% [markdown]
## feature engineering

#%%
housing['rooms_per_household'] = housing['total_rooms']/housing['households']
housing['bedrooms_per_room'] = housing['total_bedrooms']/housing['total_rooms']
housing['population_per_household'] = housing['population']/housing['households']
corr_matrix = housing.corr()
corr_matrix['median_house_value'].sort_values(ascending=False)

#%%
attributes = ["median_house_value", "median_income", "rooms_per_household", "bedrooms_per_room"]
scatter_matrix(housing[attributes], figsize=(12,8))

#%%
housing= strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set['median_house_value'].copy()

#%% [markdown]
## Imputing values

from sklearn.preprocessing import Imputer

imputer = Imputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis = 1)

imputer.fit(housing_num)
X = imputer.transform(housing_num) #numpy array

#push back to pandas
housing_tr = pd.DataFrame(X, columns=housing_num.columns)

#%% [markdown]
## Catagorical encoding - factorize, can also use LabelEncoder from sklearn

housing_cat = housing['ocean_proximity']
housing_cat_encoded, housing_categories = housing_cat.factorize()

#%% [markdown]
## Onehot Encoding
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()

# apply one hot encode into an efficient sparse matrix where only non-zeros are stored
# to make it into an array, call toarray() methods
housing_category_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))


#%% [markdown]
## Custom transformation
from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

# inheriting BaseEstimator and TransformerMixin
class combinedAttributeAdder(BaseEstimator, TransformerMixin):

    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                        bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
 
attr_adder = combinedAttributeAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)

#%% [markdown]
## Feature Scaling and pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    
    def fit(self, X, y=None):
        return X
    
    def transform(self, X, y=None):
        return x[self.attribute_names].values

num_attributes = list(housing_num)
cat_attributes = ['ocean_proximity']

num_pipeline = Pipeline([
    ('selector', DataFrameSelector(num_attributes))
    ('imputer', Imputer(strategy="median")),
    ('attribs_adder', combinedAttributeAdder()),
    ('std_scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('selector', DataFrameSelector(cat_attributes)),
    ('cat_encoder', OneHotEncoder)
])

housing_num_tr = num_pipeline.fit_transform(housing_num)

#%%
