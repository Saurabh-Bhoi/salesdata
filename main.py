from flask import Flask, jsonify, render_template, request

from project_app.utils import SalesData


#creating instance
app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to the Sales Prediction System")
    return render_template("index.html")


@app.route("/predict_sales", methods = ["POST", "GET"])
def get_sales_data():
    if request.method == "GET":
        print("We are in get method")
        
        Item_Weight = eval(request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = eval(request.args.get("Item_Visibility"))
        Item_MRP = eval(request.args.get("Item_MRP"))
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Establishment_Year = eval(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Item_Identifier = request.args.get("Item_Identifier")
        Item_Type = request.args.get("Item_Type")
        Outlet_Type = request.args.get("Outlet_Type")
    
        sales_data = SalesData(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Identifier,
                        Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Item_Identifier, 
                        Item_Type, Outlet_Type)
        sales = sales_data.get_predicted_sales()
        
        return render_template("index.html", Prediction = sales)
        #return jsonify({"Result" : f"Predicted Sales is {sales} /- Rs."}) 
    
    
print("__name__ -->", __name__)  

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug = False)