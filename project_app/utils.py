import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config


class SalesData():
    def __init__(self, Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Identifier,
                 Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Item_Identifier, 
                 Item_Type, Outlet_Type):
        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Identifier = Outlet_Identifier
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        
        self.Item_Identifier = "Item_Identifier_" + Item_Identifier
        self.Item_Type = "Item_Type_" + Item_Type
        self.Outlet_Type =  "Outlet_Type_" + Outlet_Type
        
        
    def load_models(self):
        with open (config.MODEL_FILE_PATH, "rb") as f:
            self.lasso_reg_model = pickle.load(f)
            
        with open (config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)
            
    
    def get_predicted_sales(self):
        
        self.load_models()
        
        Item_Identifier_index = list(self.json_data["columns"]).index(self.Item_Identifier)
        Item_Type_index = Item_Type_index = list(self.json_data["columns"]).index(self.Item_Type)
        Outlet_Type_index = Outlet_Type_index = list(self.json_data["columns"]).index(self.Outlet_Type)
        
        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.Item_Weight
        test_array[1] = self.json_data["Item_Fat_Content"][self.Item_Fat_Content]                             
        test_array[2] = self.Item_Visibility    
        test_array[3] = self.Item_MRP
        test_array[4] = self.json_data["Outlet_Identifier"][self.Outlet_Identifier]
        test_array[5] = self.Outlet_Establishment_Year
        test_array[6] = self.json_data["Outlet_Size"][self.Outlet_Size]
        test_array[7] = self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        test_array[Item_Identifier_index] = 1
        test_array[Item_Type_index] = 1
        test_array[Outlet_Type_index] = 1

        print("test_array -->\n", test_array)
        
        sales = round(self.lasso_reg_model.predict([test_array])[0],2)
        return sales
    
if __name__ == "__main__":
    Item_Weight = 9.300
    Item_Fat_Content = "Low Fat"
    Item_Visibility = 0.016047
    Item_MRP = 249.8092
    Outlet_Identifier = "OUT049"
    Outlet_Establishment_Year = 1999
    Outlet_Size = "Medium"
    Outlet_Location_Type = "Tier 1"
    Item_Identifier = "FDA15"
    Item_Type = "Dairy"
    Outlet_Type = "Supermarket Type1"
                
    sales_data = SalesData(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Identifier,
                    Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Item_Identifier, 
                    Item_Type, Outlet_Type)
    sales = sales_data.get_predicted_sales()
    print("Predicted Sales:", sales, "/- Rs.") 