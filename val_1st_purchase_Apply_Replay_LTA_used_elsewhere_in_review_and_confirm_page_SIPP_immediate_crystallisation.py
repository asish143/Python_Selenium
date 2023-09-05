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
from selenium.webdriver.support.select import Select


login_element_sheet,mfa_element_sheet,Global_Search_element_sheet,Member_Search_element_sheet,User_Search_element_sheet,adhoc_adviser_charge_element_sheet,manage_investment_income_element_sheet,equity_trading_element_sheet,viewquote_element_sheet,Search_element_sheet,Quotes_applications_element_sheet=common_call.get_element_sheet()

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_1st_purchase_Apply_Replay_LTA_used_elsewhere_in_review_and_confirm_page_SIPP_immediate_crystallisation')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_1st_purchase_Apply_Replay_LTA_used_elsewhere_in_review_and_confirm_page_SIPP_immediate_crystallisation_input.csv",encoding='cp1252')
print(input_df)

def val_1st_purchase_Apply_Replay_LTA_used_elsewhere_in_review_and_confirm_page_SIPP_immediate_crystallisation():
	#driver.implicitly_wait(10)
	search_result=[]
	driver.maximize_window()

	#Click Add new client
	functional_common_call.find_element(driver,Search_element_sheet.loc[21,'accessbility_id'])
	Create_new_client=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[21,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Create_new_client)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Create_new_client.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Create_new_client);
		time.sleep(3)
		common_call.highlight_element(Create_new_client, 2, 5)
	print(Create_new_client.text)
	Create_new_client.click()
	print('Create new client Click Sucess')

	#radio Button Select
	functional_common_call.find_element(driver,Search_element_sheet.loc[22,'accessbility_id'])
	Radio_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[22,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Radio_Button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Radio_Button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Radio_Button);
		time.sleep(3)
		common_call.highlight_element(Radio_Button, 2, 5)
	time.sleep(5)
	Radio_Button.click()
	print(" ARC radio button click successfully")

	#Click Start Button
	functional_common_call.find_element(driver,Search_element_sheet.loc[24,'accessbility_id'])
	Start_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[24,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Start_Button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Start_Button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Start_Button);
		time.sleep(3)
		common_call.highlight_element(Start_Button, 2, 5)
	time.sleep(5)
	Start_Button.click()
	print("Journey started")

	#Client Type Selection
	functional_common_call.find_element(driver,Search_element_sheet.loc[84,'accessbility_id'])
	ClientTyperadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[84,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,ClientTyperadiobutton)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		ClientTyperadiobutton.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", ClientTyperadiobutton);
		time.sleep(3)
		common_call.highlight_element(ClientTyperadiobutton, 2, 5)
	ClientTyperadiobutton.click()


	time.sleep(5)

	#Personal Details selection
	functional_common_call.find_element(driver,Search_element_sheet.loc[27,'accessbility_id'])
	First_Name=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[27,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,First_Name)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		First_Name.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", First_Name);
		time.sleep(3)
	First_Name.click()
	First_Name.send_keys('TestUser')
	time.sleep(3)

	functional_common_call.find_element(driver,Search_element_sheet.loc[28,'accessbility_id'])
	Last_Name=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[28,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Last_Name)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Last_Name.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Last_Name);
		time.sleep(3)
		common_call.highlight_element(Last_Name, 2, 5)
	Last_Name.click()
	Last_Name.send_keys('Testuser')
	time.sleep(3)

	functional_common_call.find_element(driver,Search_element_sheet.loc[29,'accessbility_id'])
	DOB=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[29,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,DOB)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		DOB.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", DOB);
		time.sleep(3)
		common_call.highlight_element(DOB, 2, 5)
	DOB.click()
	DOB.send_keys('22/07/1998')

	time.sleep(5)

	functional_common_call.find_element(driver,Search_element_sheet.loc[81,'accessbility_id'])
	genderradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[81,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,genderradiobutton)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		genderradiobutton.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", genderradiobutton);
		time.sleep(3)
		common_call.highlight_element(genderradiobutton, 2, 5)
	genderradiobutton.click()

	functional_common_call.find_element(driver,Search_element_sheet.loc[82,'accessbility_id'])
	residentradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[82,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,residentradiobutton)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		residentradiobutton.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", residentradiobutton);
		time.sleep(3)
		common_call.highlight_element(residentradiobutton, 2, 5)
	residentradiobutton.click()


	#Start quote button click
	functional_common_call.find_element(driver,Search_element_sheet.loc[26,'accessbility_id'])
	startquote=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[26,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,startquote)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		startquote.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", startquote);
		time.sleep(3)
		common_call.highlight_element(startquote, 2, 5)
	startquote.click()
	time.sleep(3)


	#Adviser button click
	functional_common_call.find_element(driver,Search_element_sheet.loc[83,'accessbility_id'])
	adviseradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[83,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,adviseradiobutton)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		adviseradiobutton.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", adviseradiobutton);
		time.sleep(3)
		common_call.highlight_element(adviseradiobutton, 2, 5)
	time.sleep(3)
	adviseradiobutton.click()
	time.sleep(3)

	# SIPP Product Select
	functional_common_call.find_element(driver,Search_element_sheet.loc[105,'accessbility_id'])
	productadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[105,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,productadiobutton)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		productadiobutton.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", productadiobutton);
		time.sleep(3)
		common_call.highlight_element(productadiobutton, 2, 5)
	time.sleep(5)
	print(productadiobutton.text)
	productadiobutton.click()

	#Your client wants to fully crystallise their pension
	functional_common_call.find_element(driver,Search_element_sheet.loc[151,'accessbility_id'])
	crystalization =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[151,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,crystalization)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		crystalization.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", crystalization);
		time.sleep(3)
		common_call.highlight_element(crystalization, 2, 5)
	print(crystalization.text)
	search_result.append(crystalization.text)
	crystalization.click()

	#Warning message immideate crystalization
	functional_common_call.find_element(driver,Search_element_sheet.loc[152,'accessbility_id'])
	warning =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[152,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,warning)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		warning.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", warning);
		time.sleep(3)
		common_call.highlight_element(warning, 2, 5)
	time.sleep(5)
	print(warning.text)
	#search_result.append(warning.text)
	time.sleep(3)
	#Next Button Click
	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Single Contribution
	functional_common_call.find_element(driver,Search_element_sheet.loc[106,'accessbility_id'])
	contribution =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[106,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,contribution)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		contribution.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", contribution);
		time.sleep(3)
		common_call.highlight_element(contribution, 2, 5)
	print(contribution.text)
	#driver.implicitly_wait(20)
	contribution.click()
	time.sleep(7)

	functional_common_call.find_element(driver,Search_element_sheet.loc[136,'accessbility_id'])
	contributioninput =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[136,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,contributioninput)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		contributioninput.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", contributioninput);
		time.sleep(3)
		common_call.highlight_element(contributioninput, 2, 5)
	contributioninput.send_keys('2222')

	time.sleep(3)

	#Next Button Click
	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Client Question Selection
	functional_common_call.find_element(driver,Search_element_sheet.loc[204,'accessbility_id'])
	Q1 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[204,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Q1)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Q1.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Q1);
		time.sleep(3)
		common_call.highlight_element(Q1, 2, 5)
	print(Q1.text)
	Q1.click()
	time.sleep(7)

	functional_common_call.find_element(driver,Search_element_sheet.loc[208,'accessbility_id'])
	Q2 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[208,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Q2)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Q2.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Q2);
		time.sleep(3)
		common_call.highlight_element(Q2, 2, 5)
	print(Q2.text)
	#driver.implicitly_wait(20)
	Q2.click()
	time.sleep(7)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(7)

	#nclude income
	Include_Income =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[204,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Include_Income)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Include_Income.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Include_Income);
		time.sleep(3)
		common_call.highlight_element(Include_Income, 2, 5)
	print(Include_Income.text)
	#driver.implicitly_wait(20)
	time.sleep(2)
	Include_Income.click()
	time.sleep(10)

	# #Taxable income field
	# functional_common_call.find_element(driver,Search_element_sheet.loc[186,'accessbility_id'])
	# Taxable_Income =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[186,'accessbility_id']))
	# if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
	# 	time.sleep(3)
	# 	common_call.scroll_into_element(driver,Taxable_Income)
	# if (device == 'iPhone 14/16'):
	# 	time.sleep(3)
	# 	Taxable_Income.location_once_scrolled_into_view
	# if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
	# 	time.sleep(3)
	# 	driver.execute_script("arguments[0].scrollIntoView()", Taxable_Income);
	# 	time.sleep(3)
	# 	common_call.highlight_element(Taxable_Income, 2, 5)
	# time.sleep(3)
	# Taxable_Income.send_keys("2")
	# time.sleep(3)
	#
	# #Payment Frequency
	# functional_common_call.find_element(driver,Search_element_sheet.loc[209,'accessbility_id'])
	# Paymentfrequency =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[209,'accessbility_id']))

	# if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
	# 	common_call.scroll_into_element(driver,Paymentfrequency)
	# 	time.sleep(2)
	# 	# Paymentfrequency.click()
	# 	drp=Select(Paymentfrequency)
	# 	# select by visible text
	# 	sesion=drp.select_by_visible_text('Quarterly')
	# 	print(sesion)
	#
	# if (device == 'iPhone 14/16'):
	# 	time.sleep(3)
	# 	Paymentfrequency.location_once_scrolled_into_view
	# 	time.sleep(2)
	# 	# Paymentfrequency.click()
	# 	drp=Select(Paymentfrequency)
	# 	# select by visible text
	# 	sesion=drp.select_by_visible_text('Quarterly')
	# 	print(sesion)


	# if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
	# 	driver.execute_script("arguments[0].scrollIntoView()", Paymentfrequency);
	# 	time.sleep(2)
	# 	common_call.highlight_element(Paymentfrequency, 2, 5)
	# 	time.sleep(2)
	# 	Paymentfrequency.click()
	# 	time.sleep(3)
	# 	functional_common_call.find_element(driver,Search_element_sheet.loc[214,'accessbility_id'])
	# 	Quaterly_dropdown =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[214,'accessbility_id']))
	# 	common_call.highlight_element(Quaterly_dropdown,2,5)
	# 	driver.execute_script("arguments[0].click()", Quaterly_dropdown);
	# 	#driver.execute_script("arguments[0].setAttribute('style','visibility:visible;')", Quaterly_dropdown);
	# 	Quaterly_dropdown.click()

		# drp=Select(Paymentfrequency)
		# #select by visible text
		# sesion=drp.select_by_visible_text('Quarterly')
		# print(sesion)


	# #Payment Date
	# functional_common_call.find_element(driver,Search_element_sheet.loc[210,'accessbility_id'])
	# Paymentdate =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[210,'accessbility_id']))
	# if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
	# 	time.sleep(3)
	# 	common_call.scroll_into_element(driver,Paymentdate)
	# if (device == 'iPhone 14/16'):
	# 	time.sleep(3)
	# 	Paymentdate.location_once_scrolled_into_view
	# if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
	# 	time.sleep(3)
	# 	driver.execute_script("arguments[0].scrollIntoView()", Paymentdate);
	# 	time.sleep(3)
	# 	common_call.highlight_element(Paymentdate, 2, 5)
	# print(Paymentdate.text)
	# # Paymentdate.click()
	# drp=Select(Paymentdate)
	# # select by visible text
	# sesion=drp.select_by_visible_text('18')
	# print(sesion)
	# time.sleep(5)

	#Select investment
	functional_common_call.find_element(driver,Search_element_sheet.loc[87,'accessbility_id'])
	Selectinvestment =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[87,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Selectinvestment)
		Selectinvestment.click()
	if (device == 'iPhone 14/16'):
		time.sleep(5)
		Selectinvestment.location_once_scrolled_into_view
		print(Selectinvestment.text)
		#driver.execute_script("arguments[0].click()", Selectinvestment);
		Selectinvestment.click()
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Selectinvestment);
		time.sleep(3)
		common_call.highlight_element(Selectinvestment, 2, 5)
		Selectinvestment.click()


	time.sleep(3)
	#Next Button Click
	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(15)

	time.sleep(3)
	#Next Button Click
	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
		time.sleep(3)
		# driver.execute_script("arguments[0].click()", Next_button);
		# Next_button.click()
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
		# Next_button.click()
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
		# Next_button.click()
	print(Next_button.text)
	driver.execute_script("arguments[0].click()", Next_button);
	#driver.implicitly_wait(20)
	time.sleep(3)

	#Percentage allocation
	functional_common_call.find_element(driver,Search_element_sheet.loc[109,'accessbility_id'])
	Allocate_percentage_asset = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[109,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Allocate_percentage_asset)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Allocate_percentage_asset.location_once_scrolled_into_view
		time.sleep(3)
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Allocate_percentage_asset);
		time.sleep(3)
		common_call.highlight_element(Allocate_percentage_asset, 2, 5)
	Allocate_percentage_asset.clear()
	time.sleep(3)
	Allocate_percentage_asset.send_keys('100')
	time.sleep(5)

	functional_common_call.find_element(driver,Search_element_sheet.loc[93,'accessbility_id'])
	RebalancingOption = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[93,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,RebalancingOption)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		RebalancingOption.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", RebalancingOption);
		time.sleep(3)
		common_call.highlight_element(RebalancingOption, 2, 5)
	print(RebalancingOption.text)
	time.sleep(3)
	RebalancingOption.click()
	time.sleep(3)

	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(15)

	#charges page check box selection
	functional_common_call.find_element(driver,Search_element_sheet.loc[96,'accessbility_id'])
	chargecheckbox =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[96,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,chargecheckbox)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		chargecheckbox.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", chargecheckbox);
		time.sleep(3)
		common_call.highlight_element(chargecheckbox, 2, 5)
	print(chargecheckbox.text)
	chargecheckbox.click()
	time.sleep(3)
	#charges percentage
	chargetype =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[97,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,chargetype)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		chargetype.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", chargetype);
		time.sleep(3)
		common_call.highlight_element(chargetype, 2, 5)
	print(chargetype.text)
	chargetype.click()
	time.sleep(3)

	#Enter percentage value
	percantage=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[98,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,percantage)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		percantage.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", percantage);
		time.sleep(3)
		common_call.highlight_element(percantage, 2, 5)
	percantage.clear()
	percantage.send_keys('4')
	time.sleep(3)
	#ongoiing adviser charge yes radio button selection
	Ongoingadviser = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[94,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		common_call.scroll_into_element(driver,Ongoingadviser)
	if (device == 'iPhone 14/16'):
		Ongoingadviser.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		driver.execute_script("arguments[0].scrollIntoView()", Ongoingadviser);
		common_call.highlight_element(Ongoingadviser, 2, 5)
	#if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Safari/15'):
	common_call.highlight_element(Ongoingadviser, 2, 5)
	print(Ongoingadviser.text)
	Ongoingadviser.click()

	#charge type
	Chargetype = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[95,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		common_call.scroll_into_element(driver,Chargetype)
	if (device == 'iPhone 14/16'):
		Chargetype.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		driver.execute_script("arguments[0].scrollIntoView()", Chargetype);
		common_call.highlight_element(Chargetype, 2, 5)
	print(Chargetype.text)
	Chargetype.click()

	#Enter percentage value
	percantage1=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[99,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		common_call.scroll_into_element(driver,percantage1)
	if (device == 'iPhone 14/16'):
		percantage1.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		driver.execute_script("arguments[0].scrollIntoView()", percantage1);
		common_call.highlight_element(percantage1, 2, 5)
	percantage1.clear()
	percantage1.send_keys('2')
	time.sleep(3)

	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(15)

	#click on the Apply Button
	functional_common_call.find_element(driver,Search_element_sheet.loc[150,'accessbility_id'])
	Apply_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[150,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Apply_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Apply_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Apply_button);
		time.sleep(3)
		common_call.highlight_element(Apply_button, 2, 5)
	print(Apply_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Apply_button.click()
	time.sleep(3)

	 #Adviser Button
	functional_common_call.find_element(driver,Search_element_sheet.loc[212,'accessbility_id'])
	Discretionary =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[212,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Discretionary)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Discretionary.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Discretionary);
		time.sleep(3)
		common_call.highlight_element(Discretionary, 2, 5)
	print(Discretionary.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Discretionary.click()

	#tiltle
	functional_common_call.find_element(driver,Search_element_sheet.loc[215,'accessbility_id'])
	Title =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[215,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		common_call.scroll_into_element(driver,Title)
		time.sleep(2)
		# Paymentfrequency.click()
		drp=Select(Title)
		# select by visible text
		sesion=drp.select_by_visible_text('Mr')
		print(sesion)

	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Title.location_once_scrolled_into_view
		time.sleep(2)
		# Paymentfrequency.click()
		drp=Select(Title)
		# select by visible text
		sesion=drp.select_by_visible_text('Mr')
		print(sesion)
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Title);
		time.sleep(3)
		common_call.highlight_element(Title, 2, 5)
		drp=Select(Title)
		# select by visible text
		sesion=drp.select_by_visible_text('Mr')
		print(sesion)

	#Add nationality
	functional_common_call.find_element(driver,Search_element_sheet.loc[216,'accessbility_id'])
	Add_Nationality =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[216,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Add_Nationality)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Add_Nationality.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Add_Nationality);
		time.sleep(3)
		common_call.highlight_element(Add_Nationality, 2, 5)
	print(Add_Nationality.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Add_Nationality.click()
	#Save
	functional_common_call.find_element(driver,Search_element_sheet.loc[66,'accessbility_id'])
	Save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[66,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Save)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Save.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Save);
		time.sleep(3)
		common_call.highlight_element(Save, 2, 5)
	print(Save.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Save.click()

	#Enter insure number
	functional_common_call.find_element(driver, Search_element_sheet.loc[219,'accessbility_id'])
	Insurance_Num =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[219,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Insurance_Num)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Insurance_Num.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Insurance_Num);
		time.sleep(3)
		common_call.highlight_element(Insurance_Num, 2, 5)
	print(Insurance_Num.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Insurance_Num.send_keys("BA216725C")

	functional_common_call.find_element(driver,Search_element_sheet.loc[220,'accessbility_id'])
	Addresidential_Address =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[220,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Addresidential_Address)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Addresidential_Address.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Addresidential_Address);
		time.sleep(3)
		common_call.highlight_element(Addresidential_Address, 2, 5)
	print(Addresidential_Address.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Addresidential_Address.click()

	functional_common_call.find_element(driver,Search_element_sheet.loc[221,'accessbility_id'])
	Property =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[221,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Property)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Property.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Property);
		time.sleep(3)
		common_call.highlight_element(Property, 2, 5)
	print(Property.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Property.send_keys('My home')

	functional_common_call.find_element(driver,Search_element_sheet.loc[222,'accessbility_id'])
	Property_number =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[222,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Property_number)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Property_number.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Property_number);
		time.sleep(3)
		common_call.highlight_element(Property_number, 2, 5)
	print(Property_number.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Property_number.send_keys('7787')

	functional_common_call.find_element(driver,Search_element_sheet.loc[223,'accessbility_id'])
	Street =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[223,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Street)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Street.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Street);
		time.sleep(3)
		common_call.highlight_element(Street, 2, 5)
	print(Street.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Street.send_keys('Khandagiri')

	functional_common_call.find_element(driver,Search_element_sheet.loc[224,'accessbility_id'])
	City =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[224,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,City)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		City.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", City);
		time.sleep(3)
		common_call.highlight_element(City, 2, 5)
	print(City.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	City.send_keys('Patia')


	functional_common_call.find_element(driver,Search_element_sheet.loc[225,'accessbility_id'])
	postcode =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[225,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,postcode)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		postcode.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", postcode);
		time.sleep(3)
		common_call.highlight_element(postcode, 2, 5)
	print(postcode.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	postcode.send_keys('aw09ae')

	#Save
	functional_common_call.find_element(driver,Search_element_sheet.loc[85,'accessbility_id'])
	Save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[85,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Save)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Save.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Save);
		time.sleep(3)
		common_call.highlight_element(Save, 2, 5)
	print(Save.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Save.click()

	#Click yes
	functional_common_call.find_element(driver,Search_element_sheet.loc[197,'accessbility_id'])
	Yes =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[197,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Yes)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Yes.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Yes);
		time.sleep(3)
		common_call.highlight_element(Yes, 2, 5)
	print(Yes.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Yes.click()

	#Enter Email
	functional_common_call.find_element(driver, Search_element_sheet.loc[217,'accessbility_id'])
	Email =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[217,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Email)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Email.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Email);
		time.sleep(3)
		common_call.highlight_element(Email, 2, 5)
	print(Email.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Email.send_keys("asish@gmail.com")

	#Platform Access
	functional_common_call.find_element(driver, Search_element_sheet.loc[218,'accessbility_id'])
	View_only =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[218,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,View_only)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		View_only.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", View_only);
		time.sleep(3)
		common_call.highlight_element(View_only, 2, 5)
	print(View_only.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	View_only.click()

	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(15)

	#Employeement Status
	functional_common_call.find_element(driver,Search_element_sheet.loc[226,'accessbility_id'])
	Emp_status =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[226,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Emp_status)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Emp_status.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Emp_status);
		time.sleep(3)
		common_call.highlight_element(Emp_status, 2, 5)
	print(Emp_status.text)
	#Element.click()
	drp=Select(Emp_status)
	# select by visible text
	sesion=drp.select_by_visible_text('Employed')
	print(sesion)
	time.sleep(5)

	#yes In sipp details page
	functional_common_call.find_element(driver,Search_element_sheet.loc[197,'accessbility_id'])
	Yes1 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[197,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Yes1)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Yes1.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Yes1);
		time.sleep(3)
		common_call.highlight_element(Yes1, 2, 5)
	print(Yes1.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Yes1.click()

	#yes In sipp details page
	functional_common_call.find_element(driver,Search_element_sheet.loc[198,'accessbility_id'])
	Yes2 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[198,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Yes2)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Yes2.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Yes2);
		time.sleep(3)
		common_call.highlight_element(Yes2, 2, 5)
	print(Yes2.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Yes2.click()

	#yes In sipp details page
	functional_common_call.find_element(driver,Search_element_sheet.loc[202,'accessbility_id'])
	Yes3 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[202,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Yes3)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Yes3.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Yes3);
		time.sleep(3)
		common_call.highlight_element(Yes3, 2, 5)
	print(Yes3.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Yes3.click()

	functional_common_call.find_element(driver,Search_element_sheet.loc[229,'accessbility_id'])
	MPAA_date =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[229,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,MPAA_date)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		MPAA_date.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", MPAA_date);
		time.sleep(3)
		common_call.highlight_element(MPAA_date, 2, 5)
	print(MPAA_date.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	MPAA_date.send_keys('09/08/2022')
	time.sleep(3)

	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(15)

	#Add Bank Transfer
	functional_common_call.find_element(driver,Search_element_sheet.loc[227,'accessbility_id'])
	Bank_Transfer =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[227,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Bank_Transfer)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Bank_Transfer.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Bank_Transfer);
		time.sleep(3)
		common_call.highlight_element(Bank_Transfer, 2, 5)
	print(Bank_Transfer.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Bank_Transfer.click()

	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Next_button.click()
	time.sleep(15)

	Money_out =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[40,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Money_out)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Money_out.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Money_out);
		time.sleep(3)
		common_call.highlight_element(Money_out, 2, 5)
	print(Money_out.text)
	#driver.implicitly_wait(20)
	search_result.append(Money_out.text)
	time.sleep(15)

	#Bank details
	functional_common_call.find_element(driver,Search_element_sheet.loc[231,'accessbility_id'])
	Name =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[231,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Name)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Name.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Name);
		time.sleep(3)
		common_call.highlight_element(Name, 2, 5)
	print(Name.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Name.send_keys('John')
	time.sleep(3)

	#account number
	functional_common_call.find_element(driver,Search_element_sheet.loc[232,'accessbility_id'])
	Account_Number =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[232,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Account_Number)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Account_Number.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Account_Number);
		time.sleep(3)
		common_call.highlight_element(Account_Number, 2, 5)
	print(Account_Number.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Account_Number.send_keys('10025030')
	time.sleep(3)

	#Sort Code
	#account number
	functional_common_call.find_element(driver,Search_element_sheet.loc[233,'accessbility_id'])
	Sort_Code =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[233,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Sort_Code)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Sort_Code.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Sort_Code);
		time.sleep(3)
		common_call.highlight_element(Sort_Code, 2, 5)
	print(Sort_Code.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Sort_Code.send_keys('600430 ')
	time.sleep(3)

	#Add account details
	functional_common_call.find_element(driver,Search_element_sheet.loc[234,'accessbility_id'])
	Add_Account_details =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[234,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Add_Account_details)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Add_Account_details.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Add_Account_details);
		time.sleep(3)
		common_call.highlight_element(Add_Account_details, 2, 5)
	print(Add_Account_details.text)
	#driver.implicitly_wait(20)
	time.sleep(3)
	Add_Account_details.click()
	time.sleep(3)


	SIPP_details =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[228,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,SIPP_details)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		SIPP_details.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", SIPP_details);
		time.sleep(3)
		common_call.highlight_element(SIPP_details, 2, 5)
	print(SIPP_details.text)
	#driver.implicitly_wait(20)
	search_result.append(SIPP_details.text)
	time.sleep(15)

	#Next Button Click
	functional_common_call.find_element(driver,Search_element_sheet.loc[32,'accessbility_id'])
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Next_button)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Next_button.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Next_button);
		time.sleep(3)
		common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	#driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Pension Benifit
	functional_common_call.find_element(driver,Search_element_sheet.loc[235,'accessbility_id'])
	Pension_Benifit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[235,'accessbility_id']))
	if (device == 'Samsung Galaxy S9 Plus/8.0') or ('Samsung Galaxy S21/11'):
		time.sleep(3)
		common_call.scroll_into_element(driver,Pension_Benifit)
	if (device == 'iPhone 14/16'):
		time.sleep(3)
		Pension_Benifit.location_once_scrolled_into_view
	if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/latest-1') or (device == 'Edge/latest-1') or (device == 'Safari/latest'):
		time.sleep(3)
		driver.execute_script("arguments[0].scrollIntoView()", Pension_Benifit);
		time.sleep(3)
		common_call.highlight_element(Pension_Benifit, 2, 5)
	print(Pension_Benifit.text)
	search_result.append(Pension_Benifit.text)








	return search_result

functional_common_call.login_quick(Username,Password,driver,web_address)
search_result = val_1st_purchase_Apply_Replay_LTA_used_elsewhere_in_review_and_confirm_page_SIPP_immediate_crystallisation()

session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)

driver.quit()
common_call.stop_local()