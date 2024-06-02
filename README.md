
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

Data columns (total 21 columns):
 #   Column                            Non-Null Count  Dtype         
---  ------                            --------------  -----         
 0   Fuel Type Code                    1210 non-null   object        
 1   City                              1210 non-null   object        
 2   State                             1210 non-null   object        
 3   ZIP                               1210 non-null   object        
 4   EV Level2 EVSE Num                1051 non-null   float64       
 5   EV DC Fast Count                  205 non-null    float64       
 6   EV Network                        1210 non-null   object        
 7   Geocode Status                    1210 non-null   object        
 8   Latitude                          1210 non-null   float64       
 9   Longitude                         1210 non-null   float64       
 10  Date Last Confirmed               1208 non-null   datetime64[ns]
 11  ID                                1210 non-null   int64         
 12  Updated At                        1210 non-null   object        
 13  Owner Type Code                   617 non-null    object        
 14  Open Date                         1208 non-null   datetime64[ns]
 15  EV Connector Types                1210 non-null   object        
 16  Country                           1210 non-null   object        
 17  Groups With Access Code (French)  1210 non-null   object        
 18  Access Code                       1210 non-null   object        
 19  Facility Type                     562 non-null    object        
 20  EV Pricing                        579 non-null    object 
   






---
Google. (03.24.). Google cloud platform. https://console.cloud.google.com/apis
Kaggle. (03.24.). https://www.kaggle.com/datasets
