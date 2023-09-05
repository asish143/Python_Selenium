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

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_2nd_Purchase_Adviser_Produce_Illustration_GIA_Page')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_2nd_Purchase_Adviser_Produce_Illustration_GIA_Page_input.csv",encoding='cp1252')
print(input_df)

def val_2nd_Purchase_Adviser_Produce_Illustration_GIA_Page():
	driver.implicitly_wait(10)
	search_result=[]
	driver.maximize_window()

	#Product Select (SIPP Drawdown Transfer )

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
	Input.send_keys('20486569')
	time.sleep(3)

	#Click on the submit button
	Submit=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[120,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Submit);
	common_call.highlight_element(Submit, 2, 5)
	Submit.click()
	time.sleep(3)

	#Click on the client ID
	Clientname=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[139,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Clientname);
	common_call.highlight_element(Clientname, 2, 5)
	print(Clientname.text)
	Clientname.click()
	time.sleep(20)

	#Buy product button click
	Buyproduct=driver.find_element(by=By.LINK_TEXT, value=('Buy product'))
	driver.execute_script("arguments[0].scrollIntoView()", Buyproduct);
	common_call.highlight_element(Buyproduct, 2, 5)
	print(Buyproduct.text)
	Buyproduct.click()
	time.sleep(3)

	#AOR radio Button Select
	driver.implicitly_wait(30)
	Radio_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[22,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Radio_Button);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	common_call.highlight_element(Radio_Button, 2, 5)
	Radio_Button.click()


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

	time.sleep(9)

	productadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[31,'accessbility_id']))
	time.sleep(5)
	#if(device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(productadiobutton, 2, 5)
	print(productadiobutton.text)
	productadiobutton.click()

	time.sleep(9)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)


	#User Info
	UserInfo=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[39,'accessbility_id']))
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(UserInfo, 2, 5)
	print(UserInfo.text)

	#HeDer Money In And Out
	Heardr=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[40,'accessbility_id']))
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Heardr, 2, 5)
	print(Heardr.text)

	#No Button
	No=driver.find_elements(by=By.XPATH, value=(Search_element_sheet.loc[30,'accessbility_id']))
	for nobutton in No:
		if nobutton.text=='No':
			#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
			common_call.highlight_element(nobutton, 2, 5)
		print(nobutton.text)
		nobutton.click()

	time.sleep(5)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)


	DDERROR=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[43,'accessbility_id']))
	print(DDERROR.text)


	#Drawdown Arrangements Yes

	Yes=driver.find_elements(by=By.XPATH, value=(Search_element_sheet.loc[73,'accessbility_id']))
	for yesbutton in Yes:
		if yesbutton.text=='Yes':
			#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
			common_call.highlight_element(yesbutton, 2, 5)
			print(yesbutton.text)
			yesbutton.click()
	time.sleep(5)

	#Add tranche
	Addtranche=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[76,'accessbility_id']))
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Addtranche, 2, 5)
	time.sleep(5)
	print(Addtranche.text)
	Addtranche.click()

	Addtrancheinput=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[77,'accessbility_id']))
	Addtrancheinput.click()
	Addtrancheinput.send_keys("1111")

	#income selection
	No=driver.find_elements(by=By.XPATH, value=(Search_element_sheet.loc[52,'accessbility_id']))
	for Nobutton in No:
		if Nobutton.text=='No':
			#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
			common_call.highlight_element(Nobutton, 2, 5)
			print(Nobutton.text)
			Nobutton.click()
	time.sleep(5)
	Save=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[85,'accessbility_id']))
	Save.click()

	#Enter value to product refrence

	Productrefrence=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[49,'accessbility_id']))
	Productrefrence.click()
	Productrefrence.send_keys('Asish')

	#Transfer Provider
	AddTransfer=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[63,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()",AddTransfer)
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(AddTransfer, 2, 5)
	print(AddTransfer.text)
	AddTransfer.click()

	#Transfer provider Box
	Box=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[74,'accessbility_id']))
	Box.send_keys('w')

	Transferprovider_dropdown=driver.find_elements(by=By.XPATH, value=(Search_element_sheet.loc[75,'accessbility_id']))

	for TP in Transferprovider_dropdown:
		common_call.highlight_element(TP, 2, 5)
		print(TP.text)
		#search_result.append(TP.text)
		TP.click()
		break
		time.sleep(5)

	Save=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[86,'accessbility_id']))
	Save.click()
	time.sleep(5)

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
	Selectplatform.click()

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


	#charges heading
	heading1 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[134,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", heading1);
	common_call.highlight_element(heading1, 2, 5)
	print(heading1.text)
	time.sleep(7)

	#charges page error
	chargeserror=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[148,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", chargeserror);
	common_call.highlight_element(chargeserror, 2, 5)
	print(chargeserror.text)
	time.sleep(3)

	#charges page check box selection
	chargecheckbox =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[96,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", chargecheckbox);
	common_call.highlight_element(chargecheckbox, 2, 5)
	print(chargecheckbox.text)
	chargecheckbox.click()
	time.sleep(3)

	#charges page check box selection
	chargetype =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[97,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", chargetype);
	common_call.highlight_element(chargetype, 2, 5)
	print(chargetype.text)
	chargetype.click()
	time.sleep(3)

	#Enter percentage value
	percantage=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[98,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", percantage);
	common_call.highlight_element(percantage, 2, 5)
	percantage.clear()
	percantage.send_keys('4')
	time.sleep(3)


	#ongoiing adviser charge yes radio button selection
	Ongoingadviser = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[94,'accessbility_id']))
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Ongoingadviser, 2, 5)
	print(Ongoingadviser.text)
	Ongoingadviser.click()

	#charge type
	Chargetype = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[95,'accessbility_id']))
	#driver.execute_script("arguments[0].scrollIntoView()", Chargetype);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Chargetype, 2, 5)
	print(Chargetype.text)
	Chargetype.click()

	time.sleep(7)


	#Enter percentage value
	percantage1=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[99,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", percantage1);
	common_call.highlight_element(percantage1, 2, 5)
	percantage1.clear()
	percantage1.send_keys('2')
	time.sleep(3)

	#Calculating charges by percentage of product value CTA
	CTA= driver.find_element(by=By.PARTIAL_LINK_TEXT, value=("Calculating charges "))
	driver.execute_script("arguments[0].scrollIntoView()", CTA);
	print(CTA.text)
	CTA.click()

	time.sleep(2)
	#Modal Calculation CTA
	calculationcta = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[91,'accessbility_id']))
	print(calculationcta.text)
	calculationcta.click()

	Close= driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[55,'accessbility_id']))
	Close.click()

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Save and Exit Button Click
	Apply =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[150,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Apply);
	common_call.highlight_element(Apply, 2, 5)
	print(Apply.text)

	# Personal Illustration
	WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,Search_element_sheet.loc[149, 'accessbility_id'])))
	Illustration2 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[149,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Illustration2);
	common_call.highlight_element(Illustration2, 2, 5)
	print(Illustration2.text)
	search_result.append(Illustration2.text)
	driver.implicitly_wait(20)
	Illustration2.click()
	time.sleep(7)


	#Exit Button Click
	Exit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[35,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Exit);
	common_call.highlight_element(Exit, 2, 5)
	print(Exit.text)
	driver.implicitly_wait(20)
	Exit.click()
	time.sleep(7)

	#Save and Exit Button Click
	SaveExit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[46,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", SaveExit);
	common_call.highlight_element(Exit, 2, 5)
	print(SaveExit.text)
	driver.implicitly_wait(20)
	SaveExit.click()
	time.sleep(7)







	return search_result

functional_common_call.login_quick(Username,Password,driver,web_address)
search_result = val_2nd_Purchase_Adviser_Produce_Illustration_GIA_Page()

session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)

driver.quit()
common_call.stop_local()