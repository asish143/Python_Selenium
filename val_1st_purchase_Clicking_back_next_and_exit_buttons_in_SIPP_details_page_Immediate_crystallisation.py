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
from PIL import Image


login_element_sheet,mfa_element_sheet,Global_Search_element_sheet,Member_Search_element_sheet,User_Search_element_sheet,adhoc_adviser_charge_element_sheet,manage_investment_income_element_sheet,equity_trading_element_sheet,viewquote_element_sheet,Search_element_sheet,Quotes_applications_element_sheet=common_call.get_element_sheet()

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_1st_purchase_Clicking_back_next_and_exit_buttons_in_SIPP_details_page_Immediate_crystallisation')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_1st_purchase_Clicking_back_next_and_exit_buttons_in_SIPP_details_page_Immediate_crystallisation_input.csv",encoding='cp1252')
print(input_df)

def val_1st_purchase_Clicking_back_next_and_exit_buttons_in_SIPP_details_page_Immediate_crystallisation():
	driver.implicitly_wait(10)
	search_result=[]
	driver.maximize_window()

	#Click Add new client
	Create_new_client=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[21,'accessbility_id']))
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	common_call.highlight_element(Create_new_client, 2, 5)
	print(Create_new_client.text)
	Create_new_client.click()
	print('Click Sucess')

	#radio Button Select
	driver.implicitly_wait(30)
	Radio_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[22,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Radio_Button);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	common_call.highlight_element(Radio_Button, 2, 5)
	time.sleep(5)
	Radio_Button.click()

	#Click Start Button
	Start_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[24,'accessbility_id']))
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	common_call.highlight_element(Radio_Button, 2, 5)
	time.sleep(5)
	Start_Button.click()

	#Client Type Selection
	ClientTyperadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[84,'accessbility_id']))
	ClientTyperadiobutton.click()
	# for client in ClientTyperadiobutton:
	# 	print(client.text)
	# 	time.sleep(8)
	# 	if client.text == 'Individual':
	# 		print(client.text)
	# 		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	# 			common_call.highlight_element(client, 2, 5)
	# 		print(client.text)
	# 	time.sleep(13)
	# 	client.click()
	#

	time.sleep(5)

	#Personal Details selection
	First_Name=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[27,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", First_Name);
	time.sleep(5)
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(First_Name, 2, 5)
	First_Name.click()
	First_Name.send_keys('TestUser')
	time.sleep(3)


	Last_Name=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[28,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Last_Name);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):

	common_call.highlight_element(Last_Name, 2, 5)
	Last_Name.click()
	Last_Name.send_keys('Testuser')
	time.sleep(3)


	DOB=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[29,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", DOB);
	time.sleep(4)
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(DOB, 2, 5)
	DOB.click()
	DOB.send_keys('22/07/1991')

	time.sleep(5)

	genderradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[81,'accessbility_id']))
	genderradiobutton.click()
	# for gender in genderradiobutton:
	# 	print(gender.text)
	# 	if gender.text == 'Male':
	# 		print(gender.text)
	# 		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	# 			common_call.highlight_element(gender, 2, 5)
	# 		print(gender.text)
	# 		time.sleep(3)
	# 		gender.click()
	# 	time.sleep(5)

	residentradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[82,'accessbility_id']))
	residentradiobutton.click()
	# for resident in residentradiobutton:
	# 	if resident.text == 'Yes':
	# 		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
	# 			common_call.highlight_element(resident, 2, 5)
	# 			print(resident.text)
	# 		time.sleep(5)
	# 		resident.click()



	#Start quote button click
	startquote=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[26,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", startquote);
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(startquote, 2, 5)
	startquote.click()
	time.sleep(3)


	#Adviser button click
	adviseradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[83,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", adviseradiobutton);
	time.sleep(3)
	adviseradiobutton.click()
	time.sleep(3)

	# SIPP Product Select
	productadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[105,'accessbility_id']))
	time.sleep(5)
	#if(device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(productadiobutton, 2, 5)
	print(productadiobutton.text)
	productadiobutton.click()

	#Your client wants to fully crystallise their pension
	crystalization =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[151,'accessbility_id']))
	time.sleep(5)
	#if(device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(crystalization, 2, 5)
	print(crystalization.text)
	search_result.append(crystalization.text)
	crystalization.click()

	#Warning message immideate crystalization
	warning =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[152,'accessbility_id']))
	time.sleep(5)
	common_call.highlight_element(warning, 2, 5)
	print(warning.text)
	#search_result.append(warning.text)
	time.sleep(3)
	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Single Contribution
	contribution =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[106,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", contribution);
	common_call.highlight_element(contribution, 2, 5)
	print(contribution.text)
	driver.implicitly_wait(20)
	contribution.click()
	time.sleep(7)

	contributioninput =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[136,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", contributioninput);
	common_call.highlight_element(contributioninput, 2, 5)
	contributioninput.send_keys('44444')

	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Client Type Selection
	Q1 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[153,'accessbility_id']))
	print(Q1.text)
	driver.implicitly_wait(20)
	Q1.click()
	time.sleep(7)

	Q2 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[155,'accessbility_id']))
	print(Q2.text)
	driver.implicitly_wait(20)
	Q2.click()
	time.sleep(7)

	Addbenifit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[161,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Addbenifit);
	common_call.highlight_element(Addbenifit, 2, 5)
	print(Addbenifit.text)
	search_result.append(Addbenifit.text)
	driver.implicitly_wait(20)
	Addbenifit.click()
	time.sleep(3)

	Datecrystalized =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[162,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Datecrystalized);
	common_call.highlight_element(Datecrystalized, 2, 5)
	print(Datecrystalized.text)
	driver.implicitly_wait(20)
	Datecrystalized.send_keys('06/06/2022')
	time.sleep(3)

	LTAused =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[163,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", LTAused);
	common_call.highlight_element(LTAused, 2, 5)
	print(LTAused.text)
	driver.implicitly_wait(20)
	LTAused.click()
	LTAused.send_keys('2')
	time.sleep(3)

	save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[66,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", save);
	common_call.highlight_element(LTAused, 2, 5)
	save.click()
	time.sleep(5)

	Back =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[34,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Back);
	common_call.highlight_element(Back, 2, 5)
	print(Back.text)
	Back.click()
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	Exit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[35,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Exit);
	common_call.highlight_element(Exit, 2, 5)
	Exit.click()

	time.sleep(5)

	SaveExit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[46,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", SaveExit);
	common_call.highlight_element(SaveExit, 2, 5)
	print(SaveExit.text)
	search_result.append(SaveExit.text)
	SaveExit.click()
	time.sleep(3)



















	return search_result

functional_common_call.login_quick(Username,Password,driver,web_address)
search_result = val_1st_purchase_Clicking_back_next_and_exit_buttons_in_SIPP_details_page_Immediate_crystallisation()

session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)

driver.quit()
common_call.stop_local()