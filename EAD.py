#json Module to work with json files and formats

print('Debug EAD Program-Started');

import json
from datetime import date

system_date=date.today()

today=system_date.strftime('%d-%b-%Y')

print(today)

print('Debug EAD Program- Json Module imported');

#Function to Calculate EAD


def fn_EAD(add_on, notinal_amount, mtm_amount):
  if mtm_amount<0:
      mtm_amount=0
  EAD=(mtm_amount+(notinal_amount*add_on))
  return EAD

print('Debug EAD Program- fn_EAD Function created');

# Derivative Data
derivative_data_filename=input("Enter FileName of Derivative Data:");

with open(derivative_data_filename) as f:
     deriv_data=json.load(f)

print('Debug EAD Program- Derivative Json Loaded');

#add-ons Static Data for asset class
asset_class_addon_filename="asset_class_addons.json"


with open(asset_class_addon_filename) as f:
     add_ons_data=json.load(f)

print('Debug EAD Program- Static Data(add-ons)Loaded');

derivative_rec=deriv_data["data"]

output_list=[]

for i in derivative_rec:
     v_id=i["id"]
     v_asset_class=i["asset_class"]
     v_notinal_amount=i["notinal_amount"]
     v_mtm_amount=i["mtm_dirty"]
     v_addon=add_ons_data[v_asset_class]
     
       
       #Calling EAD Calculator
     
     print('Debug EAD Program-  Calculating EAD for '+v_id);

     v_EAD=fn_EAD(v_addon, v_notinal_amount, v_mtm_amount)

     i["EAD"]=v_EAD
 
     output_list.append(i)

derivative_data_EAD_Output={"name":"Derivative_Data","date":today,"data":output_list}

print(derivative_data_EAD_Output)

with open('derivative_data_EAD_Output.json', 'w') as output_file:
    json.dump(derivative_data_EAD_Output, output_file)







     
     




     
    
    
