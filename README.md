# ONDC Invovation Hackathon  

### Problem Statement :
    Challenge 6 : Create a model (using formal programming language) for non-deterministic inventory
    management to determine the optimal “lot size” to minimize the operational costs related to
    ordering and moving goods through the retail supply chain.

### Solution :

#### Description :

  A non-deterministic ML model which predicts optimal qantinty of products for a seller . 
 
    key-Hightlights:
      1. Customised prediction for each seller on platform 
      2. Ability to extract required feature i.g : 
      3. Auto-retrain mechanism  over a period of time with live data
      4.
      
Adavantages : 
      1. 
      2.
    
#### Technical Detail : 

    Tech Stack :
    
        Programming Language: 
            1. Python
            
        Tools:
            1. Jupyter Notebook
            2. Vs code
            3. Postman
            
        Major Framework :
            1. Flask
            
    Algorithm :
            1. Random Forest 
            
    Deployment:
            1. On Azure
            
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
           
    
   
#### Reusability : 
    API :
    
#### Scalability : 
    API :
    
#### Extensibility: 
    API :
    
#### Assumptions :
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
    


