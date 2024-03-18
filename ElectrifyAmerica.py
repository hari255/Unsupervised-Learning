#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


virginia = pd.read_excel("Virginia_EV.xlsx")


# In[3]:


virginia.head()


# In[4]:


#pip install geopandas 

### Geo pandas is a python library handle shape files.


# ### Let's take a look

# In[5]:


import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px

######################################### Load Virginia shapefile   ######################################################

#################### Link to shape file:  https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-1-states-provinces/

virginia_gpd = gpd.read_file('C:\\Users\\Harinath\\Downloads\\ne_110m_populated_places\\ne_110m_populated_places.shp')
virginia = pd.read_excel("Virginia_EV.xlsx")


###################################### Plot EV stations in Virginia using plotly ##############################################
fig = px.scatter_mapbox(virginia, lat='Latitude', lon='Longitude', color='EV Network',
                        color_discrete_map={'Electrify America': 'red', 'Other Providers': 'blue'},
                        hover_data={'EV Network': True},
                        mapbox_style='carto-positron', zoom=6, center={'lat': 38.0037, 'lon': -79.4588})
fig.update_layout(title='EV Stations in Virginia', margin={"r": 0, "t": 30, "l": 0, "b": 0})
fig.show()


# In[6]:


virginia.info()


# ### Preprocessing

# In[7]:


from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min


# In[8]:


#######Let's consider only the J1772 Connector type, since it's the most used and popular##########

virginia['EV Connector Type'] = virginia['EV Connector Types'].map({'J1772': 1})

##### Let's only consider the Hotel, college, shopping mall, parking garae and offices for the facility types. Since, people tend to visit these places often ###############
#############################################################################################################################################################################

virginia['Facility Type'] = virginia['Facility Type'].map({'HOTEL': 1, 'COLLEGE_CAMPUS': 2,'SHOPPING_MALL':3,'PARKING_GARAGE':4, 'OFFICE_BLDG':5})


# In[9]:


features = ['Latitude', 'Longitude', 'EV Connector Types', 'Facility Type']
cluster_data = virginia[features]


# In[10]:


####################### one-hot encoding for categorical variables ###################################
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False)
encoded_features = encoder.fit_transform(virginia[['EV Connector Types', 'Facility Type']])
encoded_feature_names = encoder.get_feature_names_out(['EV Connector Types', 'Facility Type'])


# Combine encoded features with numerical features
features_encoded = pd.DataFrame(encoded_features, columns=encoded_feature_names)
features_encoded[['Latitude', 'Longitude']] = virginia[['Latitude', 'Longitude']]


# #### Transformed DataFrame

# In[11]:


features_encoded


# In[12]:


features_encoded


# In[13]:


######################################    Setting the number of clusters     ##########################################

### Since my data set is very small, I've directly choosed 8 clusters as a starting poinnt, if we have a huge dataset, 
### we can use elbow plot to do the job for us.

kmeans = KMeans(n_clusters=8)


# In[14]:


#############################  Let's asssign the cluster labels to a variable "Cluster"   #############################


virginia['Cluster'] = kmeans.fit_predict(features_encoded)


# In[15]:


############################ Seperating Electrify America's stations  from other providers ####################################


electrify_america = virginia[virginia['EV Network'] == 'Electrify America']
other_providers = virginia[virginia['EV Network'] != 'Electrify America']


# ### ---------------------------------------------------------------******************---------------------------------------------------------------------

# ### Identifying clusters where Electrify America is absent among the clustered charging stations.

# In[16]:


missing_clusters = []
for cluster_id in other_providers['Cluster'].unique():
    cluster_data = other_providers[other_providers['Cluster'] == cluster_id]
    if not any(electrify_america['Cluster'] == cluster_id):
        missing_clusters.append(cluster_id)


# ### Suggesting New Stations

# In[17]:


###################### Generate suggestions for new Electrify America stations within missing clusters  ########################

suggested_stations = []
for cluster_id in missing_clusters:
    cluster_data = other_providers[other_providers['Cluster'] == cluster_id]
    center_lat = cluster_data['Latitude'].mean()
    center_lon = cluster_data['Longitude'].mean()
    suggested_stations.append((center_lat, center_lon))


# In[18]:


print("Suggested new stations for Electrify America:")
for station in suggested_stations:
    print(station)


# In[19]:


len(suggested_stations) ### we can increase this number 


# ### ---------------------------------------------------------------******************---------------------------------------------------------------------

# ### Let's do the reverse geo-coding to idenfiy the new location types (school, shopping center, parking lot etc.)

# In[20]:


#pip install geopy


# In[21]:


# suggested_stations['Facility Type']


# In[22]:


api_key=""


# In[23]:


import geopandas as gpd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import numpy as np
from geopy.geocoders import GoogleV3



ea_stations = virginia[virginia['EV Network'] == 'Electrify America'].copy()
other_stations = virginia[virginia['EV Network'] != 'Electrify America'].copy()


# In[24]:


############################################# Electrify America's Stations #################################################

ea_stations.head(10)


# In[25]:


############################## Below key-value pairs allows us to identify the facility type ###################################

type_mapping = {
    'street_address': 'Street Address',
    'premise': 'Premise',
    'car_repair': 'Car Repair',
    'establishment': 'Establishment',
    'car_dealer': 'Car Dealer'
}


# In[27]:


################################ Perform clustering on other EV network stations ###########################################

kmeans = KMeans(n_clusters=10)  # Increased number of clusters to 10
other_stations['Cluster'] = kmeans.fit_predict(other_stations[['Latitude', 'Longitude']])

################################ Finding the cluster centers for other stations  ###########################################

cluster_centers, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, other_stations[['Latitude', 'Longitude']])

############### Calculating distances from Electrify America stations to cluster centers of other stations #################

ea_distances = pairwise_distances_argmin_min(ea_stations[['Latitude', 'Longitude']], other_stations[['Latitude', 'Longitude']])

########################################### Let's select suggested stations ################################################

################################ Select 15 stations farthest from existing stations ########################################

suggested_indices = np.argsort(ea_distances[1])[-15:]  
suggested_stations = other_stations.iloc[suggested_indices]

################################# Initialize geolocator with Google Maps Geocoding API key #################################

geolocator = GoogleV3(api_key='')

################################## Function to get location details and facility type ######################################

def get_location_details(latitude, longitude):
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if location:
        
        ############## Extract facility type from the types field in the geocoding response ##################
        
        facility_type = next(iter(location.raw.get('types', [])), None)
        facility_description = type_mapping.get(facility_type, facility_type)
        return {
            'Location Details': location.address,
            'Facility Type': facility_type
        }
    else:
        return None
    
########## Apply the function to the DataFrame and expand the result into separate columns for existing stations ############

ea_stations[['Location Details', 'Facility Type']] = ea_stations.apply(
    lambda row: pd.Series(get_location_details(row['Latitude'], row['Longitude'])), axis=1)

######## Apply the function to the DataFrame and expand the result into separate columns for suggested stations #############

suggested_stations[['Location Details', 'Facility Type']] = suggested_stations.apply(
    lambda row: pd.Series(get_location_details(row['Latitude'], row['Longitude'])), axis=1)

####################################### EV stations in Virginia using Plotly Express ########################################

fig = px.scatter_mapbox(virginia, lat='Latitude', lon='Longitude', color='EV Network',
                        color_discrete_map={'Electrify America': 'red', 'Other Providers': 'blue'},
                        hover_data={'EV Network': True, 'Facility Type': True},  # Add 'Facility Type' to hover data
                        mapbox_style='carto-positron', zoom=6, center={'lat': 38.0037, 'lon': -79.4588})

########################## Adding layout to the existing Electrify America stations #########################################

fig.add_trace(go.Scattermapbox(
    lat=ea_stations['Latitude'],
    lon=ea_stations['Longitude'],
    mode='markers',
    marker=dict(size=10, color='red'),
    name='Existing Electrify America Stations',
    hoverinfo='text',
    text=['<b>EV Network</b>: {}<br><b>Facility</b>: {}<br><b>Location Details</b>: {}'.format(ev_network, facility_type, location_details)
          for ev_network, facility_type, location_details in zip(ea_stations['EV Network'], ea_stations['Facility Type'], ea_stations['Location Details'])]
))

########################## Adding layout to the suggested Electrify America stations #########################################

fig.add_trace(go.Scattermapbox(
    lat=suggested_stations['Latitude'],
    lon=suggested_stations['Longitude'],
    mode='markers',
    marker=dict(symbol='circle', size=10, color='blue'),# Change symbol to circle and color to blue
    name='New Electrify America Stations',
    hoverinfo='text',
    text=['<b>EV Network</b>: {}<br><b>Facility</b>: {}<br><b>Location Details</b>: {}'.format(ev_network, facility_type, location_details)
          for ev_network, facility_type, location_details in zip(suggested_stations['EV Network'], suggested_stations['Facility Type'], suggested_stations['Location Details'])]
))

# Updating layout
fig.update_layout(title='EV Stations in Virginia', margin={"r": 0, "t": 30, "l": 0, "b": 0})
fig.show()


# In[ ]:





# In[ ]:




