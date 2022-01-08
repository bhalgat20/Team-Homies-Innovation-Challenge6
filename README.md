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
  2. 


### Instructions to build & operate the app: 

       
### Future Scope : 


