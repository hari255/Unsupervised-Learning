
# Strategic expansion planning for ElectrifyAmerica's EV charging stations in Virginia, USA.
---

## Description

This case study utilizes `Python`, `K-means clustering`, `Geoencoding API` and `NaturalEarth Shape file` to identify and display optimal locations for future Electrify America charging stations in Virginia.  I've integrated Google Cloud Platform's GeoCoding API for precise location display on my plots. The approach offers strategic insights to support Electrify America's expansion efforts, promoting EV adoption in Virginia.

https://hari255.github.io/Electrify_America/

## Data collection 

Extratcted this dataset from Kaggle.
https://www.kaggle.com/datasets/saketpradhan/electric-and-alternative-fuel-charging-stations

**Dataset Description**

 + After performing data cleading from on the dataset, I've used only few columns that are required to build this model, I've also filtered the data to only include stations in Virginia.
 + This  dataset include information about various EV charging providers in USA, like Telsa, EVgo, Electrify America etc.
 + Dataset consists of 1210 records and 21 columns.


 |  Column                           |  Non-Null  Count  |Dtype  |       
 | ---------------------------------:| ----------------:|------:|                                  
 |   Fuel Type Code                  | 1210 non-null  |  object  |        
 |   City                            |  1210 non-null |  object  |     
 |   State                           | 1210 non-null  | object   |     
 |   ZIP                             |  1210 non-null |  object  |      
 |   EV Level2 EVSE Num              | 1051 non-null  | float64  |     
 |   EV DC Fast Count                |  205 non-null  |  float64 |      
 |   EV Network                      |  1210 non-null |  object  |      
 |   Geocode Status                  |  1210 non-null |  object   |     
 |   Latitude                        |  1210 non-null |  float64   |    
 |   Longitude                       |  1210 non-null |  float64   |    
 |  Date Last Confirmed              | 1208 non-null  | datetime64[ns]|
 |  ID                               | 1210 non-null  | int64        | 
 |  Updated At                       | 1210 non-null  | object  |      
 |  Owner Type Code                  | 617 non-null   | object   |     
 |  Open Date                        | 1208 non-null  | datetime64[ns]|
 |  EV Connector Types               | 1210 non-null  | object|        
 |  Country                          | 1210 non-null  | object |       
 |  Groups With Access Code (French) | 1210 non-null  | object  |      
 |  Access Code                      | 1210 non-null  | object|        
 |  Facility Type                    | 562 non-null   | object |       
 |  EV Pricing                       | 579 non-null   | object |


## Natural Earth shape file

``` py
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


```

**By using above code, I've created the interactive ploty visualizations, I was able to create that map with the help of shape file downloaded from `Natural Earth` that enables to hover and view each charging station at deatils about it.**

![image](https://github.com/hari255/Electrify_America/assets/59302293/31d31a8a-6a23-4d0e-8139-2e5a20922b32)



## Google Geo Encoding API

``` py
################################# Initialize geolocator with Google Maps Geocoding API key #################################

geolocator = GoogleV3(api_key='*************************')

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

```

**The geo-coding API helps us with the address for the locations our model suggested, I've added this to enhance the visualization, when we hover mouse on each dot, it displays information related to that location.**

![image](https://github.com/hari255/Electrify_America/assets/59302293/28678472-287f-4280-9da2-a7c5ab6fba78)


---
Google. (03.24.). Google cloud platform. https://console.cloud.google.com/apis
Kaggle. (03.24.). https://www.kaggle.com/datasets
