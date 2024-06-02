
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
   

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |




---
Google. (03.24.). Google cloud platform. https://console.cloud.google.com/apis
Kaggle. (03.24.). https://www.kaggle.com/datasets
