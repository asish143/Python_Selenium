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

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_1st_purchase_verify_PCLS_amount_for_Immediate_crystallization')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_1st_purchase_PCLS_amount_and_display_only_fields_Immediate_crystallization_input.csv",encoding='cp1252')
print(input_df)

def val_1st_purchase_PCLS_amount_and_display_only_fields_Immediate_crystallization():
	#driver.implicitly_wait(10)
	time.sleep(10)
	search_result=[]
	driver.maximize_window()

	try:
		#Click Add new client
		Create_new_client=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[21,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Create_new_client)
			print(Create_new_client.text)
			Create_new_client.click()
			print('Click Sucess')
		if (device == 'iPhone 14/16'):
			Create_new_client.location_once_scrolled_into_view
			print(Create_new_client.text)
			Create_new_client.click()
			print('Click Sucess')
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Create_new_client)
			common_call.highlight_element(Create_new_client, 2, 5)
			print(Create_new_client.text)
			Create_new_client.click()
			print('Click Sucess')

		try:
			#radio Button Select
			if (device == 'iPhone 14/16'):
				time.sleep(5)
			if (device == 'Samsung Galaxy S9 Plus/8.0'):
				time.sleep(15)
			if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
				WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,Search_element_sheet.loc[22, 'accessbility_id'])))

			Radio_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[22,'accessbility_id']))
			Radio_Button_And=driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[53,'accessbility_id']))
			if (device == 'Samsung Galaxy S9 Plus/8.0'):
				common_call.scroll_into_element(driver,Radio_Button_And)
				time.sleep(5)
				Radio_Button_And.click()
			if (device == 'iPhone 14/16'):
				Radio_Button.location_once_scrolled_into_view
				common_call.highlight_element(Radio_Button, 2, 5)
				time.sleep(5)
				Radio_Button.click()
			if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
				driver.execute_script("arguments[0].scrollIntoView()",Radio_Button)
				common_call.highlight_element(Radio_Button, 2, 5)
				time.sleep(5)
				Radio_Button.click()
		except:
			print('Platform not found')

		try:
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[288, 'accessibility_id'])))
			Selectbranch = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[288, 'accessibility_id'])
			driver.execute_script("arguments[0].scrollIntoView()",Selectbranch)
			common_call.highlight_element(Selectbranch, 2, 5)
			Selectbranch.click()

			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[289, 'accessibility_id'])))
			Selectbranchfromoptions = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[289, 'accessibility_id'])
			driver.execute_script("arguments[0].scrollIntoView()",Selectbranchfromoptions)
			common_call.highlight_element(Selectbranchfromoptions, 2, 5)
			print(Selectbranchfromoptions.text)
			Selectbranchfromoptions.click()
		except:
			print('Branch not found')
			pass

		if (device == 'Samsung Galaxy S9 Plus/8.0') or (device == 'iPhone 14/16'):
			time.sleep(5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Search_element_sheet.loc[24, 'accessbility_id'])))

		#Click Start Button
		Start_Button=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[24,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Start_Button)
		if (device == 'iPhone 14/16'):
			Start_Button.location_once_scrolled_into_view
			common_call.highlight_element(Start_Button, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Start_Button)
			common_call.highlight_element(Start_Button, 2, 5)
		time.sleep(5)
		Start_Button.click()

		#Client Type Selection
		ClientTyperadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[84,'accessbility_id']))
		ClientTyperadiobutton.click()


		time.sleep(5)

		#Personal Details selection
		First_Name=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[27,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,First_Name)
		if (device == 'iPhone 14/16'):
			First_Name.location_once_scrolled_into_view
			common_call.highlight_element(First_Name, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",First_Name)
			common_call.highlight_element(First_Name, 2, 5)
		First_Name.click()
		First_Name.send_keys('TestUser')
		time.sleep(3)


		Last_Name=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[28,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Last_Name)
		if (device == 'iPhone 14/16'):
			Last_Name.location_once_scrolled_into_view
			common_call.highlight_element(Last_Name, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Last_Name)
			common_call.highlight_element(Last_Name, 2, 5)
		Last_Name.click()
		Last_Name.send_keys('Testuser')
		time.sleep(3)


		DOB=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[29,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,DOB)
		if (device == 'iPhone 14/16'):
			DOB.location_once_scrolled_into_view
			common_call.highlight_element(DOB, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",DOB)
			common_call.highlight_element(DOB, 2, 5)
		time.sleep(4)
		DOB.click()
		DOB.send_keys('22/07/1991')

		time.sleep(5)

		genderradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[81,'accessbility_id']))
		genderradiobutton.click()

		residentradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[82,'accessbility_id']))
		residentradiobutton.click()


		#Start quote button click
		startquote=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[26,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,startquote)
		if (device == 'iPhone 14/16'):
			startquote.location_once_scrolled_into_view
			common_call.highlight_element(startquote, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",startquote)
			common_call.highlight_element(startquote, 2, 5)
		startquote.click()
		time.sleep(3)


		#Adviser button click
		adviseradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[83,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,adviseradiobutton)
		if (device == 'iPhone 14/16'):
			adviseradiobutton.location_once_scrolled_into_view
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",adviseradiobutton)
		time.sleep(3)
		adviseradiobutton.click()
		time.sleep(3)

		# SIPP Product Select
		functional_common_call.find_element(driver,Search_element_sheet.loc[211,'accessbility_id'])
		productadiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[211,'accessbility_id']))
		time.sleep(5)
		if (device == 'iPhone 14/16'):
			common_call.highlight_element(productadiobutton, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			common_call.highlight_element(productadiobutton, 2, 5)
		print(productadiobutton.text)
		productadiobutton.click()

		#Your client wants to fully crystallise their pension
		crystalization =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[151,'accessbility_id']))
		time.sleep(5)
		if (device == 'iPhone 14/16'):
			common_call.highlight_element(crystalization, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			common_call.highlight_element(crystalization, 2, 5)
		print(crystalization.text)
		search_result.append(crystalization.text)
		crystalization.click()

		#Warning message immideate crystalization
		warning =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[152,'accessbility_id']))
		time.sleep(5)
		if (device == 'iPhone 14/16'):
			common_call.highlight_element(warning, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			common_call.highlight_element(warning, 2, 5)
		print(warning.text)
		time.sleep(3)
		#Next Button Click
		Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Next_button)
		if (device == 'iPhone 14/16'):
			Next_button.location_once_scrolled_into_view
			common_call.highlight_element(Next_button, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Next_button)
			common_call.highlight_element(Next_button, 2, 5)
		print(Next_button.text)
		time.sleep(5)
		Next_button.click()
		time.sleep(7)

		#Single Contribution
		functional_common_call.find_element(driver,Search_element_sheet.loc[195,'accessbility_id'])
		contribution =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[195,'accessbility_id']))
		contribution_ios =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[195,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,contribution)
			print(contribution.text)
			time.sleep(5)
			contribution.click()
		if (device == 'iPhone 14/16'):
			contribution_ios.location_once_scrolled_into_view
			common_call.highlight_element(contribution_ios, 2, 5)
			print(contribution_ios.text)
			time.sleep(5)
			contribution_ios.click()
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",contribution)
			common_call.highlight_element(contribution, 2, 5)
			print(contribution.text)
			time.sleep(5)
			contribution.click()
		time.sleep(7)

		contributioninput =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[136,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,contributioninput)
		if (device == 'iPhone 14/16'):
			contributioninput.location_once_scrolled_into_view
			common_call.highlight_element(contributioninput, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",contributioninput)
			common_call.highlight_element(contributioninput, 2, 5)
		contributioninput.send_keys('44444')

		time.sleep(3)

		#Next Button Click
		Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Next_button)
		if (device == 'iPhone 14/16'):
			Next_button.location_once_scrolled_into_view
			common_call.highlight_element(Next_button, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Next_button)
			common_call.highlight_element(Next_button, 2, 5)
		print(Next_button.text)
		time.sleep(5)
		Next_button.click()
		time.sleep(7)

		#Client Question Selection
		#Q1 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[153,'accessbility_id']))
		Q1_iOS =driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[46,'accessbility_id']))
		Q1_And =driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[54,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Q1_And)
			print(Q1_And.text)
			time.sleep(5)
			Q1_And.click()
		if (device == 'iPhone 14/16'):
			print(Q1_iOS.text)
			time.sleep(5)
			Q1_iOS.click()
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			print(Q1_iOS.text)
			time.sleep(5)
			Q1_iOS.click()
		time.sleep(7)

		Q2_iOS =driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[47,'accessbility_id']))
		print(Q2_iOS.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Q2_iOS.click()
		time.sleep(7)

		Addbenifit =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[161,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Addbenifit)
		if (device == 'iPhone 14/16'):
			Addbenifit.location_once_scrolled_into_view
			common_call.highlight_element(Addbenifit, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Addbenifit)
			common_call.highlight_element(Addbenifit, 2, 5)
		print(Addbenifit.text)
		search_result.append(Addbenifit.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Addbenifit.click()
		time.sleep(3)

		Datecrystalized =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[162,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Datecrystalized)
			time.sleep(2)
			Datecrystalized.send_keys('06/06/2022')
		if (device == 'iPhone 14/16'):
			Datecrystalized.location_once_scrolled_into_view
			common_call.highlight_element(Datecrystalized, 2, 5)
			time.sleep(2)
			Datecrystalized.send_keys('06/06/2022')
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Datecrystalized)
			common_call.highlight_element(Datecrystalized, 2, 5)
			#print(Datecrystalized.text)
			# driver.implicitly_wait(2)
			time.sleep(2)
			Datecrystalized.send_keys('06/06/2022')
		time.sleep(3)

		LTAused =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[163,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,LTAused)
			time.sleep(2)
			LTAused.click()
			LTAused.send_keys('2')
		if (device == 'iPhone 14/16'):
			LTAused.location_once_scrolled_into_view
			common_call.highlight_element(LTAused, 2, 5)
			time.sleep(2)
			LTAused.click()
			#LTAused.send_keys('2')
			driver.execute_script("arguments[0].value = arguments[1];", LTAused, '2')
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",LTAused)
			common_call.highlight_element(LTAused, 2, 5)
			#print(LTAused.text)
			#driver.implicitly_wait(20)
			time.sleep(2)
			LTAused.click()
			LTAused.send_keys('2')
		time.sleep(3)

		save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[66,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,save)
			save.click()
		if (device == 'iPhone 14/16'):
			save.location_once_scrolled_into_view
			common_call.highlight_element(save, 2, 5)
			save.click()
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",save)
			common_call.highlight_element(save, 2, 5)
			save.click()
		time.sleep(5)

		Q3=driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[48,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Q3)
			print(Q3.text)
			time.sleep(5)
			Q3.click()
		if (device == 'iPhone 14/16'):
			Q3.location_once_scrolled_into_view
			print(Q3.text)
			time.sleep(5)
			Q3.click()
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Q3)
			common_call.highlight_element(Q3, 2, 5)
			print(Q3.text)
			time.sleep(5)
			Q3.click()
		time.sleep(7)

		Q4=driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[49,'accessbility_id']))
		print(Q4.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Q4.click()
		time.sleep(7)

		Pension_Protection=driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[50,'accessbility_id']))
		print(Pension_Protection.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Pension_Protection.click()
		time.sleep(7)

		#Next Button Click
		Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Next_button)
		if (device == 'iPhone 14/16'):
			Next_button.location_once_scrolled_into_view
			common_call.highlight_element(Next_button, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Next_button)
			common_call.highlight_element(Next_button, 2, 5)
		print(Next_button.text)
		# driver.implicitly_wait(20)
		time.sleep(2)
		Next_button.click()
		time.sleep(7)

		heading =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[166,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,heading)
		if (device == 'iPhone 14/16'):
			heading.location_once_scrolled_into_view
			common_call.highlight_element(heading, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",heading)
			common_call.highlight_element(heading, 2, 5)
		print(heading.text)
		search_result.append(heading.text)
		time.sleep(5)

		Avialable_LTA=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[167,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Avialable_LTA)
		if (device == 'iPhone 14/16'):
			Avialable_LTA.location_once_scrolled_into_view
			common_call.highlight_element(Avialable_LTA, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Avialable_LTA)
			common_call.highlight_element(Avialable_LTA, 2, 5)
		mis_text = Avialable_LTA.text[-6:]
		print(mis_text)
		search_result.append(mis_text)
		time.sleep(5)

		LTAUsed_Before=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[168,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,LTAUsed_Before)
		if (device == 'iPhone 14/16'):
			LTAUsed_Before.location_once_scrolled_into_view
			common_call.highlight_element(LTAUsed_Before, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",LTAUsed_Before)
			common_call.highlight_element(LTAUsed_Before, 2, 5)
		LTA_Bef=LTAUsed_Before.text[-5: ]
		print(LTA_Bef)
		search_result.append(LTA_Bef)
		time.sleep(5)

		LTAUsed_After=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[169,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,LTAUsed_After)
		if (device == 'iPhone 14/16'):
			LTAUsed_After.location_once_scrolled_into_view
			common_call.highlight_element(LTAUsed_After, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",LTAUsed_After)
			common_call.highlight_element(LTAUsed_After, 2, 5)
		LTA_AFT=LTAUsed_After.text[-5: ]
		print(LTA_AFT)
		search_result.append(LTA_AFT)
		time.sleep(5)

		PCLS_Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,PCLS_Amount)
		if (device == 'iPhone 14/16'):
			PCLS_Amount.location_once_scrolled_into_view
			common_call.highlight_element(PCLS_Amount, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",PCLS_Amount)
			common_call.highlight_element(PCLS_Amount, 2, 5)
		print(PCLS_Amount.text)
		#search_result.append(LTA_AFT)
		time.sleep(5)


		PCLS_Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,PCLS_Amount)
		if (device == 'iPhone 14/16'):
			PCLS_Amount.location_once_scrolled_into_view
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",PCLS_Amount)
		PCLS_Amount.clear()
		time.sleep(3)

		Set_MaximumPCLS_Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[171,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Set_MaximumPCLS_Amount)
		if (device == 'iPhone 14/16'):
			Set_MaximumPCLS_Amount.location_once_scrolled_into_view
			common_call.highlight_element(Set_MaximumPCLS_Amount, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Set_MaximumPCLS_Amount)
			common_call.highlight_element(Set_MaximumPCLS_Amount, 2, 5)
		Set_MaximumPCLS_Amount.click()

		time.sleep(3)

		Total_to_Crystalized=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[172,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Total_to_Crystalized)
		if (device == 'iPhone 14/16'):
			Total_to_Crystalized.location_once_scrolled_into_view
			common_call.highlight_element(Total_to_Crystalized, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Total_to_Crystalized)
			common_call.highlight_element(Total_to_Crystalized, 2, 5)
		Crystalized=Total_to_Crystalized.text[-5: ]
		print(Crystalized)
		#search_result.append(Crystalized)
		time.sleep(5)

		Pcls_Amount2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[173,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Pcls_Amount2)
		if (device == 'iPhone 14/16'):
			Pcls_Amount2.location_once_scrolled_into_view
			common_call.highlight_element(Pcls_Amount2, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Pcls_Amount2)
			common_call.highlight_element(Pcls_Amount2, 2, 5)
		Amount=Pcls_Amount2.text[-5: ]
		print(Amount)
		#search_result.append(Amount)
		time.sleep(5)

		Total_Drawdown=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[174,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Total_Drawdown)
		if (device == 'iPhone 14/16'):
			Total_Drawdown.location_once_scrolled_into_view
			common_call.highlight_element(Total_Drawdown, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Total_Drawdown)
			common_call.highlight_element(Total_Drawdown, 2, 5)
		Total=Total_Drawdown.text[-5: ]
		print(Total)
		#search_result.append(Total)
		time.sleep(5)

		SIPPDetails =driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[56,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,SIPPDetails)

		Back =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[34,'accessbility_id']))
		Back_And =driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[55,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Back_And)
			print(Back_And.text)
			Back_And.click()
		if (device == 'iPhone 14/16'):
			Back.location_once_scrolled_into_view
			common_call.highlight_element(Back, 2, 5)
			print(Back.text)
			Back.click()
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Back)
			common_call.highlight_element(Back, 2, 5)
			print(Back.text)
			Back.click()
		time.sleep(3)

		Q3_Yes=driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[51,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Q3_Yes)
		if (device == 'iPhone 14/16'):
			Q3_Yes.location_once_scrolled_into_view
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Q3_Yes)
		print(Q3_Yes.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Q3_Yes.click()
		time.sleep(7)

		Add_Payment=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[175,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Add_Payment)
		if (device == 'iPhone 14/16'):
			Add_Payment.location_once_scrolled_into_view
			common_call.highlight_element(Add_Payment, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Add_Payment)
			common_call.highlight_element(Add_Payment, 2, 5)
		print(Add_Payment.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Add_Payment.click()
		time.sleep(7)

		Q3_LTAused=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[176,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Q3_LTAused)
			time.sleep(3)
			Q3_LTAused.click()
			#Q3_LTAused.clear()
			Q3_LTAused.send_keys('30')

			#driver.execute_script("arguments[0].value = arguments[1];", Q3_LTAused, '30')
			#Q3_LTAused.send_keys('30')
		if (device == 'iPhone 14/16'):
			Q3_LTAused.location_once_scrolled_into_view
			time.sleep(3)
			Q3_LTAused.click()
			driver.execute_script("arguments[0].value = arguments[1];", Q3_LTAused, '30')
			#Q3_LTAused.send_keys('30')
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Q3_LTAused)
			common_call.highlight_element(Q3_LTAused, 2, 5)
			time.sleep(3)
			Q3_LTAused.click()
			driver.execute_script("arguments[0].value = arguments[1];", Q3_LTAused, '30')
			#Q3_LTAused.send_keys('30')
		time.sleep(7)

		save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[85,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,save)
		if (device == 'iPhone 14/16'):
			save.location_once_scrolled_into_view
			common_call.highlight_element(save, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",save)
			common_call.highlight_element(save, 2, 5)
		save.click()
		time.sleep(5)


		Q4_Yes=driver.find_element(by=By.XPATH, value=(Member_Search_element_sheet.loc[52,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Q4_Yes)
		if (device == 'iPhone 14/16'):
			Q4_Yes.location_once_scrolled_into_view
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Q4_Yes)
		print(Q4_Yes.text)
		time.sleep(3)
		Q4_Yes.click()
		time.sleep(7)

		Add_Transfer=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[177,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Add_Transfer)
		if (device == 'iPhone 14/16'):
			Add_Transfer.location_once_scrolled_into_view
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Add_Transfer)
		print(Add_Transfer.text)
		#driver.implicitly_wait(20)
		time.sleep(3)
		Add_Transfer.click()
		time.sleep(7)

		Date_of_Transfer=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[178,'accessbility_id']))
		print(Date_of_Transfer.text)
		#driver.implicitly_wait(20)
		time.sleep(3)
		Date_of_Transfer.click()
		Date_of_Transfer.send_keys('09/09/2006')
		time.sleep(7)

		Name_of_Scheme=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[179,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Name_of_Scheme)
			time.sleep(3)
			Name_of_Scheme.click()
			Name_of_Scheme.send_keys('Ujwala')
			#driver.execute_script("arguments[0].value = arguments[1];", Name_of_Scheme, 'Ujwala')
		if (device == 'iPhone 14/16'):
			Name_of_Scheme.location_once_scrolled_into_view
			time.sleep(3)
			Name_of_Scheme.click()
			Name_of_Scheme.send_keys('Ujwala')
			#driver.execute_script("arguments[0].value = arguments[1];", Name_of_Scheme, 'Ujwala')
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Name_of_Scheme)
			common_call.highlight_element(Name_of_Scheme, 2, 5)
			time.sleep(3)
			Name_of_Scheme.click()
			Name_of_Scheme.send_keys('Ujwala')
			#driver.execute_script("arguments[0].value = arguments[1];", Name_of_Scheme, 'Ujwala')
		time.sleep(7)

		Transferamount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[180,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Transferamount)
			time.sleep(3)
			Transferamount.click()
			#driver.execute_script("arguments[0].value = arguments[1];", Transferamount, '1200')
			Transferamount.send_keys('1200')
		if (device == 'iPhone 14/16'):
			Transferamount.location_once_scrolled_into_view
			time.sleep(3)
			Transferamount.click()
			driver.execute_script("arguments[0].value = arguments[1];", Transferamount, '1200')
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Transferamount)
			common_call.highlight_element(Transferamount, 2, 5)
			time.sleep(3)
			Transferamount.click()
			driver.execute_script("arguments[0].value = arguments[1];", Transferamount, '1200')
		time.sleep(7)


		save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[86,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,save)
		if (device == 'iPhone 14/16'):
			save.location_once_scrolled_into_view
			common_call.highlight_element(save, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",save)
			common_call.highlight_element(save, 2, 5)
		save.click()
		time.sleep(5)

		#Next Button Click
		Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Next_button)
		if (device == 'iPhone 14/16'):
			Next_button.location_once_scrolled_into_view
			common_call.highlight_element(Next_button, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Next_button)
			common_call.highlight_element(Next_button, 2, 5)
		print(Next_button.text)
		#driver.implicitly_wait(20)
		time.sleep(5)
		Next_button.click()
		time.sleep(10)

		#Next Button Click
		Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Next_button)
		if (device == 'iPhone 14/16'):
			Next_button.location_once_scrolled_into_view
			common_call.highlight_element(Next_button, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Next_button)
			common_call.highlight_element(Next_button, 2, 5)
		print(Next_button.text)
		#driver.implicitly_wait(20)
		time.sleep(3)
		Next_button.click()
		time.sleep(8)


		Avialable_LTA2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[167,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Avialable_LTA2)
		if (device == 'iPhone 14/16'):
			Avialable_LTA2.location_once_scrolled_into_view
			common_call.highlight_element(Avialable_LTA2, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Avialable_LTA2)
			common_call.highlight_element(Avialable_LTA2, 2, 5)
		mis_text2 = Avialable_LTA2.text[-6:]
		print(mis_text2)
		search_result.append(mis_text2)
		time.sleep(5)

		LTAUsed_Before2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[168,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,LTAUsed_Before2)
		if (device == 'iPhone 14/16'):
			LTAUsed_Before2.location_once_scrolled_into_view
			common_call.highlight_element(LTAUsed_Before2, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",LTAUsed_Before2)
			common_call.highlight_element(LTAUsed_Before2, 2, 5)
		LTA_Bef2=LTAUsed_Before2.text[-5: ]
		print(LTA_Bef2)
		search_result.append(LTA_Bef2)
		time.sleep(5)

		LTAUsed_After2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[169,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,LTAUsed_After2)
		if (device == 'iPhone 14/16'):
			LTAUsed_After2.location_once_scrolled_into_view
			common_call.highlight_element(LTAUsed_After2, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",LTAUsed_After2)
			common_call.highlight_element(LTAUsed_After2, 2, 5)
		LTA_AFT2=LTAUsed_After2.text[-5: ]
		print(LTA_AFT2)
		search_result.append(LTA_AFT2)
		time.sleep(5)

		Total_to_Crystalized2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[172,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Total_to_Crystalized2)
		if (device == 'iPhone 14/16'):
			Total_to_Crystalized2.location_once_scrolled_into_view
			common_call.highlight_element(Total_to_Crystalized2, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Total_to_Crystalized2)
			common_call.highlight_element(Total_to_Crystalized2, 2, 5)
		Crystalized2=Total_to_Crystalized2.text[-5: ]
		print(Crystalized2)
		#search_result.append(Crystalized2)
		time.sleep(5)

		#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Search_element_sheet.loc[170, 'accessibility_id'])))

		# PCLSAMT2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
		# driver.execute_script("arguments[0].scrollIntoView()", PCLSAMT2)
		# PCLSAMT2.click()
		# time.sleep(4)
		# PCLSAMT2.send_keys('1390')
		#
		# Error2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[182,'accessbility_id']))
		# driver.execute_script("arguments[0].scrollIntoView()", Error2);
		# common_call.highlight_element(Error2, 2, 5)
		# print(Error2.text)
		# #search_result.append(Error2.text)
		# time.sleep(4)
		#
		# PCLSAMT3=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
		# driver.execute_script("arguments[0].scrollIntoView()", PCLSAMT3)
		# common_call.highlight_element(PCLSAMT3, 2, 5)
		# PCLSAMT3.click()
		# time.sleep(3)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT.send_keys(Keys.BACKSPACE)
		# PCLSAMT2.send_keys('13111190')
		#
		# Error3=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[183,'accessbility_id']))
		# driver.execute_script("arguments[0].scrollIntoView()", Error3);
		# common_call.highlight_element(Error3, 2, 5)
		# print(Error3.text)
		# #search_result.append(Error3.text)

		PCLSAMT=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,PCLSAMT)
		if (device == 'iPhone 14/16'):
			PCLSAMT.location_once_scrolled_into_view
			common_call.highlight_element(PCLSAMT, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",PCLSAMT)
			common_call.highlight_element(PCLSAMT, 2, 5)
		PCLSAMT.click()
		time.sleep(2)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		PCLSAMT.send_keys(Keys.BACKSPACE)
		time.sleep(2)

		Error1=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[181,'accessbility_id']))
		if (device == 'Samsung Galaxy S9 Plus/8.0'):
			common_call.scroll_into_element(driver,Error1)
		if (device == 'iPhone 14/16'):
			Error1.location_once_scrolled_into_view
			common_call.highlight_element(Error1, 2, 5)
		if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/111') or (device == 'Edge/111') or (device == 'Safari/15'):
			driver.execute_script("arguments[0].scrollIntoView()",Error1)
			common_call.highlight_element(Error1, 2, 5)
		print(Error1.text)
		search_result.append(Error1.text)
		time.sleep(20)
	except:
		return False

	return search_result

functional_common_call.login_quick(Username,Password,driver,web_address)
search_result = val_1st_purchase_PCLS_amount_and_display_only_fields_Immediate_crystallization()
if search_result == False:
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Elements Not found!"}}')
	driver.quit()
session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)
driver.quit()
common_call.stop_local()