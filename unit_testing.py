import unittest
import EAD
import json

class TestEAD(unittest.TestCase):


    def test_EAD_Calc(self):

        deriv_data=EAD.derivative_rec
        print('sai')
        print(deriv_data)
        expected_values_filename="Expected_Result.json"
        with open(expected_values_filename) as f:
             expected_values_rec=json.load(f)
             print(expected_values_rec)
        expected_values=expected_values_rec["data"]
        print(expected_values)
        print('---------')

        asset_class_addon_filename="asset_class_addons.json"
        with open(asset_class_addon_filename) as f:
            add_ons_data=json.load(f)
        

        for i in deriv_data:
           for j in expected_values:
              if i["id"]==j["id"]:
                 v_mtm_amount=i["mtm_dirty"]
                 v_notinal_amount=i["notinal_amount"]
                 v_asset_class=i["asset_class"]
                 v_addon=add_ons_data[v_asset_class] 
                 result=EAD.fn_EAD(v_addon, v_notinal_amount, v_mtm_amount)
                 self.assertEqual(result,j["EAD"])
if __name__=='__main__':
      unittest.main()