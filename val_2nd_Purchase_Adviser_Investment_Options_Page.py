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

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_2nd_Purchase_Adviser_Investment_Options_Page')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_2nd_Purchase_Adviser_Investment_Options_Page_input.csv",encoding='cp1252')
print(input_df)

def val_2nd_Purchase_Adviser_Investment_Options_Page():
	driver.implicitly_wait(10)
	search_result=[]
	driver.maximize_window()

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
	Input.send_keys('ind')
	time.sleep(3)

	#Click on the submit button
	Submit=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[120,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Submit);
	common_call.highlight_element(Submit, 2, 5)
	Submit.click()
	time.sleep(3)

	#Click on the client ID
	Clientname=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[139,'accessbility_id']))
	common_call.highlight_element(Clientname, 2, 5)
	print(Clientname.text)
	Clientname.click()
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

	time.sleep(9)
	#product selection (Sipp)
	SIPP =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[122,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", SIPP);
	common_call.highlight_element(SIPP, 2, 5)
	print(SIPP.text)
	search_result.append(SIPP.text)
	SIPP.click()
	time.sleep(3)
	# #product selection (Sipp)
	# SIPPdrawdown =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[132,'accessbility_id']))
	# driver.execute_script("arguments[0].scrollIntoView()", SIPPdrawdown);
	# common_call.highlight_element(SIPPdrawdown, 2, 5)
	# print(SIPPdrawdown.text)
	# SIPPdrawdown.click()
	# time.sleep(3)
	#product selection (Sipp)
	GIA =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[133,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", GIA);
	common_call.highlight_element(GIA, 2, 5)
	print(GIA.text)
	GIA.click()
	time.sleep(3)


	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	search_result.append(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Single Employer Contribution
	Empcontribution =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[106,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Empcontribution);
	common_call.highlight_element(Empcontribution, 2, 5)
	print(Empcontribution.text)
	search_result.append(Empcontribution.text)
	driver.implicitly_wait(20)
	Empcontribution.click()
	time.sleep(7)

	#Enter single contribution
	Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[136,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Amount);
	common_call.highlight_element(Amount, 2, 5)
	Amount.click()
	Amount.send_keys('4000')
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Sipp heading
	heading =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[134,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", heading);
	common_call.highlight_element(heading, 2, 5)
	print(heading.text)
	search_result.append(heading.text)
	time.sleep(7)

	#Retirement age
	Retirement=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[137,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Retirement);
	common_call.highlight_element(Retirement, 2, 5)
	Retirement.clear()
	time.sleep(3)
	Retirement.click()
	time.sleep(3)
	Retirement.send_keys('14')

	time.sleep(5)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()

	time.sleep(7)

	#Retirement age Error
	Retirementerror=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[138,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Retirementerror);
	common_call.highlight_element(Retirementerror, 2, 5)
	print(Retirementerror.text)
	search_result.append(Retirementerror.text)

	#Retirement age input
	Age=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[137,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Age);
	common_call.highlight_element(Age, 2, 5)
	Age.click()
	Age.clear()
	Age.send_keys('121')
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Retirement age Error2
	Retirementerror2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[138,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Retirementerror2);
	common_call.highlight_element(Retirementerror2, 2, 5)
	print(Retirementerror2.text)
	search_result.append(Retirementerror2.text)
	time.sleep(3)

	#Retirement age input
	Age2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[137,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Age2);
	common_call.highlight_element(Age2, 2, 5)
	Age2.clear()
	Age2.send_keys('65')
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Investment option page
	Selectplatform=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[87,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Selectplatform);
	common_call.highlight_element(Selectplatform, 2, 5)
	time.sleep(7)
	print(Selectplatform.text)
	search_result.append(Selectplatform.text)
	Selectplatform.click()

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	# #Asset search
	# AssetSearch = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[88,'accessbility_id']))
	# AssetSearch.send_keys('7IM AAP Balanced C Inc')
	# time.sleep(15)
	#
	# Factsheet=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[144,'accessbility_id']))
	# driver.execute_script("arguments[0].scrollIntoView()",Factsheet)
	# print(Factsheet.text)
	#
	# Asset_validation = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[143,'accessbility_id']))
	# common_call.highlight_element(Asset_validation, 2, 5)
	# print(Asset_validation.text)
	#
	#
	# #asseet Add
	# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Search_element_sheet.loc[89, 'accessbility_id'])))
	# AddButton = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[89,'accessbility_id']))
	# #driver.execute_script("arguments[0].scrollIntoView()",AddButton)
	# common_call.highlight_element(AddButton, 2, 5)
	# print(AddButton.text)
	# #err_results.append(AddButton.text)
	# AddButton.click()
	# time.sleep(5)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Percentage allocation
	Allocate_percentage_asset = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[109,'accessbility_id']))
	Allocate_percentage_asset.clear()
	Allocate_percentage_asset.send_keys('100')
	time.sleep(5)

	RebalancingOption = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[93,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", RebalancingOption);
	time.sleep(15)
	print(RebalancingOption.text)
	RebalancingOption.click()
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)
	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Enter single contribution
	check=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[106,'accessbility_id']))
	check.click()
	Amount2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[145,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Amount2);
	common_call.highlight_element(Amount2, 2, 5)
	Amount2.click()
	Amount2.send_keys('4000')
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Investment option page
	Selectplatform2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[140,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Selectplatform2);
	common_call.highlight_element(Selectplatform2, 2, 5)
	time.sleep(7)
	print(Selectplatform2.text)
	search_result.append(Selectplatform2.text)
	Selectplatform2.click()
	time.sleep(3)

	#Select Model Catagory
	Selectmodelcatagory=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[141,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Selectmodelcatagory);
	common_call.highlight_element(Selectmodelcatagory, 2, 5)
	time.sleep(7)
	print(Selectmodelcatagory.text)
	Selectmodelcatagory.click()
	time.sleep(3)
	DFM=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[146,'accessbility_id']))
	print(DFM.text)
	search_result.append(DFM.text)
	DFM.click()

	#Select Model protofolio
	Selectmodelprotofolio=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[142,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Selectmodelprotofolio);
	common_call.highlight_element(Selectmodelprotofolio, 2, 5)
	time.sleep(3)
	print(Selectmodelprotofolio.text)
	Selectmodelprotofolio.click()
	time.sleep(3)
	result=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[147,'accessbility_id']))
	print(result.text)
	search_result.append(result.text)
	result.click()

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	RebalancingOption2 = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[93,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", RebalancingOption2);
	time.sleep(15)
	print(RebalancingOption2.text)
	RebalancingOption2.click()
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)















	return search_result

functional_common_call.login_quick(Username,Password,driver,web_address)
search_result = val_2nd_Purchase_Adviser_Investment_Options_Page()

session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)

driver.quit()
common_call.stop_local()