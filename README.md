# ONDC Invovation Hackathon  

## Problem Statement :
__Challenge 6__ : Create a model (using formal programming language) for non-deterministic inventory
    management to determine the optimal “lot size” to minimize the operational costs related to
    ordering and moving goods through the retail supply chain.
    
We understood the problem of local Kirana store in managing the inventory. The major challenges the Kirana seller has,
    
- __Optimal Lot Size__ - Optimal lot size of a given product for future month.
- __Efficiently manage inventory space__ - Right lot size to ensure the inventory space is efficiently managed for multiple products.
- __Predict products in demand__ - Identify what products will be in demand for upcoming month and their optimal quantity.
- __Predict unforeseen crisis__ - Identify any unforseen instances (Economy crisis, Health crisis , Weather crisis , Regional news sentiment) which might impact future demand and plan accordingly.
- __Maximize profit__ - Seller wants to make maximum profit from his investment made in inventory.    

## Approach :

The team came up with generic , re-usable , scalable Machine Learning model which can help seller address above challenges.

The seller can trained thier specific model with their sales data for last few years and model will be able to predict optimum lot size for next few months. 

The ML model will be customized , trained and deployed seperately for each seller to improve the accuracy based out of seller historical data , demand , weather , economic , regional sentiments.

The ML model will pre-process the data and extract weighted features to ?

The ML model with deployed on Azure Cloud and will be exposed via API endpoint for prediction and re-trained the model.

    
### ML Model :

A non-deterministic ML model which predicts optimal quantity of products for a seller . 
- __Header extraction and parsing__
 
    Key-Hightlights:
      1. Customised prediction for each seller on platform 
      2. Ability to extract required feature i.g : 
      3. Auto-retrain mechanism  over a period of time with live data
      4.
      
Adavantages : 
      1. 
      2.
    
### Technical Detail : 

#### Tech Stack :
    
  **Language and Packages:**
  - Python
  - Panda
  - Skilearn
            
  **Tools and IDE:**
  - Jupyter Notebook
  - VS Code
  - Postman
            
  **Deployment :**
  - FastApi
  - Azure 
            
  **Algorithm :**
  - Random Forest 
            

            
    Re-training:
            1. Shedular re-retrain models with live data every "N" month / year 
            
    API documnentation:
           1. GET : 
                endpoint : /prediction
                payload / body :    {
                                      sellerId: {
                                        "type": string
                                      },
                                      products: {
                                        "type": array,
                                        "items": {
                                          "productName": {
                                            "type": string
                                          }
                                        },
                                      }
                                    }
                 reponse : {
                              "type": array,
                              "items": {
                                "type": "object",
                                "properties": {
                                  "productName": {
                                    "type": string
                                  },
                                  "Quantity": {
                                    "type": float
                                  }
                                }
                              }
                            }
           
    
   
### Reusability : 
    API :
    
### Scalability : 
    API :
    
### Extensibility: 
    API :
    
### Assumptions :
  1. Lot size of every products is 100 
  2. We are doing predcition of requried lots of product on monthly basis.


### Instructions to build & operate the app: 

       
### Future Scope : 

1. We can extend existing logic to predict optimal quatity of lots size of products of newly on-boarded seller based on existing model of seller residing at same place .
2. Logic can be extended to support custom duration [ not necessarily a month starting from 1st, i.e : predictions from 03/02/2022 to 08/04/2022 ] for which a seller wants to stock products.
3. Based on data collected from seller app via our post end point , ML model can be trained to suggest products to sell in an area , to maximise seller's profit .
4. Given data of logistic company provding service in an area , we can provide suggestion of charges of different logistic company to enable seller to provide home delivery with maximum profit.
            NB: Required factors : Weight ,date , distance ; factors which can be derived with our feature extractor : weather ( from date ) , holidays ( from date ) , population density ( from city ) etc.
    5. Sheduler can be in-corporated to re-retrain model with live data to imporve model accuracy over time.
           NB: Scheduler is a piece of code which run after fixed interval [ this interval can be 1 month / 1 year etc. ] 
    


