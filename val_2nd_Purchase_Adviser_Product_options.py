import os, sys, json

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
print("Current Directory",parentddir)

pov_automation= os.path.dirname(parentddir)
print(pov_automation)
common_direc_path = os.path.join(pov_automation, 'common')
print(common_direc_path)
helpers_direc_path = os.path.join(pov_automation, 'pyscripts/helpers')
print(helpers_direc_path)

from selenium import webdriver
import sys
sys.path.insert(0, common_direc_path)
sys.path.insert(0, helpers_direc_path)
import common_call
import functional_common_call
import pandas as pd
import numpy as np
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from browserstack.local import Local
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


login_element_sheet,mfa_element_sheet,Global_Search_element_sheet,Member_Search_element_sheet,User_Search_element_sheet,adhoc_adviser_charge_element_sheet,manage_investment_income_element_sheet,equity_trading_element_sheet,viewquote_element_sheet,Search_element_sheet,Quotes_applications_element_sheet=common_call.get_element_sheet()

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_2nd_Purchase_Adviser_Product_options')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_2nd_Purchase_Adviser_Product_options_input.csv",encoding='cp1252')
print(input_df)

def val_2nd_Purchase_Adviser_Product_options():
	driver.implicitly_wait(10)
	search_result=[]
	driver.maximize_window()

	#Click on the Manage quotes button
	Managequotes_button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[0,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Managequotes_button);
	common_call.highlight_element(Managequotes_button, 2, 5)
	Managequotes_button.click()
	time.sleep(3)

	#Click on the search button
	Searchbutton=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[118,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Searchbutton);
	common_call.highlight_element(Searchbutton, 2, 5)
	Searchbutton.click()
	time.sleep(3)

	#Enter values in the input bar
	Input=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[119,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Input);
	common_call.highlight_element(Input, 2, 5)
	Input.click()
	Input.send_keys('21276783')
	time.sleep(3)

	#Click on the submit button
	Submit=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[120,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Submit);
	common_call.highlight_element(Submit, 2, 5)
	Submit.click()
	time.sleep(3)

	#Click on the client ID
	Link=driver.find_element(by=By.PARTIAL_LINK_TEXT, value=('Ind127358FirstName'))
	common_call.highlight_element(Link, 2, 5)
	print(Link.text)
	Link.click()
	time.sleep(20)

	#Buy product button click
	Buyproduct=driver.find_element(by=By.LINK_TEXT, value=('Buy product'))
	driver.execute_script("arguments[0].scrollIntoView()", Buyproduct);
	common_call.highlight_element(Buyproduct, 2, 5)
	print(Buyproduct.text)
	search_result.append(Buyproduct.text)
	Buyproduct.click()
	time.sleep(3)



	#Link an adviser
	adviserdropdown=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[121,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", adviserdropdown);
	common_call.highlight_element(adviserdropdown, 2, 5)
	print(adviserdropdown.text)
	search_result.append(adviserdropdown.text)
	time.sleep(5)
	adviserdropdown.click()
	time.sleep(4)
	WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,Search_element_sheet.loc[124, 'accessbility_id'])))
	Selectbranchfromoptions =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[124,'accessbility_id']))
	common_call.highlight_element(Selectbranchfromoptions, 2, 5)
	print(Selectbranchfromoptions.text)
	Selectbranchfromoptions.click()
	time.sleep(3)


	#Click Start Button
	Start_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[24,'accessbility_id']))
	common_call.highlight_element(Start_Button, 2, 5)
	time.sleep(5)
	Start_Button.click()
	time.sleep(3)

	#Uk resident yes button
	residentradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[125,'accessbility_id']))
	residentradiobutton.click()
	time.sleep(3)

	#Adviser button click
	adviseradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[83,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", adviseradiobutton);
	common_call.highlight_element(adviseradiobutton, 2, 5)
	time.sleep(3)
	adviseradiobutton.click()
	time.sleep(3)

	time.sleep(3)
	#Product Select
	productadiobutton =driver.find_elements(by=By.XPATH, value=(Search_element_sheet.loc[127,'accessbility_id']))
	for product in productadiobutton:
		print(product.text)
		search_result.append(product.text)
		# if product.text == 'One Retirement (drawdown) - transfer in only':
		# 	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
		# 		common_call.highlight_element(product, 2, 5)
		# 	#search_result.append(Radiobutton.text)
		# 	time.sleep(5)
		# 	product.click()
	time.sleep(9)






	return search_result

functional_common_call.login_quick(Username,Password,driver,web_address)
search_result = val_2nd_Purchase_Adviser_Product_options()

session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)

driver.quit()
common_call.stop_local()