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

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('val_1st_purchase_Changes_to_Initial_adviser_charges_Immediate_Crystallization')
BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)


#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE
driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
#common_call.connect_BS_hub(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps)


functional_common_call.maximize_driver_window(driver)
input_df= pd.read_csv(input_file+"val_1st_purchase_Changes_to_Initial_adviser_charges_Immediate_Crystallization_input.csv",encoding='cp1252')
print(input_df)

def val_1st_purchase_Changes_to_Initial_adviser_charges_Immediate_Crystallization():
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

	residentradiobutton =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[82,'accessbility_id']))
	residentradiobutton.click()


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

	#Client Question Selection
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
	driver.implicitly_wait(2)
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

	Q3=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[158,'accessbility_id']))
	print(Q3.text)
	driver.implicitly_wait(20)
	Q3.click()
	time.sleep(7)

	Q4=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[160,'accessbility_id']))
	print(Q4.text)
	driver.implicitly_wait(20)
	Q4.click()
	time.sleep(7)

	Pension_Protection=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[165,'accessbility_id']))
	print(Pension_Protection.text)
	driver.implicitly_wait(20)
	Pension_Protection.click()
	time.sleep(7)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	heading =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[166,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", heading);
	common_call.highlight_element(heading, 2, 5)
	print(heading.text)
	search_result.append(heading.text)
	time.sleep(5)

	Avialable_LTA=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[167,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Avialable_LTA);
	common_call.highlight_element(Avialable_LTA, 2, 5)
	mis_text = Avialable_LTA.text[-6:]
	print(mis_text)
	search_result.append(mis_text)
	time.sleep(5)

	LTAUsed_Before=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[168,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", LTAUsed_Before);
	common_call.highlight_element(LTAUsed_Before, 2, 5)
	LTA_Bef=LTAUsed_Before.text[-5: ]
	print(LTA_Bef)
	search_result.append(LTA_Bef)
	time.sleep(5)

	LTAUsed_After=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[169,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", LTAUsed_After);
	common_call.highlight_element(LTAUsed_After, 2, 5)
	LTA_AFT=LTAUsed_After.text[-5: ]
	print(LTA_AFT)
	search_result.append(LTA_AFT)
	time.sleep(5)

	PCLS_Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", PCLS_Amount);
	common_call.highlight_element(PCLS_Amount, 2, 5)
	print(PCLS_Amount.text)
	#search_result.append(LTA_AFT)
	time.sleep(5)


	PCLS_Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[170,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", PCLS_Amount);
	PCLS_Amount.clear()
	time.sleep(3)

	Set_MaximumPCLS_Amount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[171,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Set_MaximumPCLS_Amount);
	common_call.highlight_element(Set_MaximumPCLS_Amount, 2, 5)
	Set_MaximumPCLS_Amount.click()

	time.sleep(3)

	Total_to_Crystalized=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[172,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Total_to_Crystalized);
	common_call.highlight_element(Total_to_Crystalized, 2, 5)
	Crystalized=Total_to_Crystalized.text[-5: ]
	print(Crystalized)
	#search_result.append(Crystalized)
	time.sleep(5)

	Pcls_Amount2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[173,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Pcls_Amount2);
	common_call.highlight_element(Pcls_Amount2, 2, 5)
	Amount=Pcls_Amount2.text[-5: ]
	print(Amount)
	#search_result.append(Amount)
	time.sleep(5)

	Total_Drawdown=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[174,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Total_Drawdown);
	common_call.highlight_element(Total_Drawdown, 2, 5)
	Total=Total_Drawdown.text[-5: ]
	print(Total)
	#search_result.append(Total)
	time.sleep(5)

	Back =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[34,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Back);
	common_call.highlight_element(Back, 2, 5)
	print(Back.text)
	Back.click()
	time.sleep(3)

	Q3_Back=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[157,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Q3_Back);
	print(Q3_Back.text)
	driver.implicitly_wait(20)
	Q3_Back.click()
	time.sleep(7)

	Add_Payment=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[175,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Add_Payment);
	print(Add_Payment.text)
	driver.implicitly_wait(20)
	Add_Payment.click()
	time.sleep(7)

	Q3_LTAused=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[176,'accessbility_id']))
	print(Q3_LTAused.text)
	driver.implicitly_wait(20)
	Q3_LTAused.send_keys('30')
	time.sleep(7)

	save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[85,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", save);
	common_call.highlight_element(save, 2, 5)
	save.click()
	time.sleep(5)


	Q4_Back=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[159,'accessbility_id']))
	print(Q4_Back.text)
	driver.implicitly_wait(20)
	Q4_Back.click()
	time.sleep(7)

	Add_Transfer=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[177,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Add_Transfer);
	print(Add_Transfer.text)
	driver.implicitly_wait(20)
	Add_Transfer.click()
	time.sleep(7)


	Date_of_Transfer=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[178,'accessbility_id']))
	print(Date_of_Transfer.text)
	driver.implicitly_wait(20)
	Date_of_Transfer.send_keys('09/09/2006')
	time.sleep(7)

	Name_of_Scheme=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[179,'accessbility_id']))
	print(Name_of_Scheme.text)
	driver.implicitly_wait(20)
	Name_of_Scheme.click()
	Name_of_Scheme.send_keys('Ujwala')
	time.sleep(7)

	Transferamount=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[180,'accessbility_id']))
	print(Transferamount.text)
	driver.implicitly_wait(20)
	Transferamount.send_keys('1200')
	time.sleep(7)


	save =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[86,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", save);
	common_call.highlight_element(save, 2, 5)
	save.click()
	time.sleep(5)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(8)


	Avialable_LTA2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[167,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Avialable_LTA2);
	common_call.highlight_element(Avialable_LTA2, 2, 5)
	mis_text2 = Avialable_LTA2.text[-6:]
	print(mis_text2)
	search_result.append(mis_text2)
	time.sleep(5)

	LTAUsed_Before2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[168,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", LTAUsed_Before2);
	common_call.highlight_element(LTAUsed_Before2, 2, 5)
	LTA_Bef2=LTAUsed_Before2.text[-5: ]
	print(LTA_Bef2)
	search_result.append(LTA_Bef2)
	time.sleep(5)

	LTAUsed_After2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[169,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", LTAUsed_After2);
	common_call.highlight_element(LTAUsed_After2, 2, 5)
	LTA_AFT2=LTAUsed_After2.text[-5: ]
	print(LTA_AFT2)
	search_result.append(LTA_AFT2)
	time.sleep(5)

	Total_to_Crystalized2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[172,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Total_to_Crystalized2);
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


	time.sleep(2)
	IncludeincomeNo=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[185,'accessbility_id']))
	IncludeincomeNo.click()
	time.sleep(5)

	#Investment option page
	Selectplatform=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[87,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Selectplatform);
	common_call.highlight_element(Selectplatform, 2, 5)
	time.sleep(7)
	print(Selectplatform.text)
	Selectplatform.click()
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

	Header = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[130,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Header);
	time.sleep(2)
	print(Header.text)
	search_result.append(Header.text)
	time.sleep(3)



	#charges page check box selection
	chargecheckbox =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[96,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", chargecheckbox);
	common_call.highlight_element(chargecheckbox, 2, 5)
	print(chargecheckbox.text)
	chargecheckbox.click()
	time.sleep(3)

	Info = driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[189,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Info)
	common_call.highlight_element(Info, 2, 5)
	time.sleep(2)
	print(Info.text)
	search_result.append(Info.text)
	time.sleep(3)


	#charges percentage
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
	#Scenario 1 for error
	percantage1=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[98,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", percantage1);
	common_call.highlight_element(percantage1, 2, 5)
	percantage1.clear()
	percantage1.send_keys('11')
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Error 1
	Error1 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[192,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Error1);
	common_call.highlight_element(Error1, 2, 5)
	print(Error1.text)
	search_result.append(Error1.text)
	time.sleep(7)

	#Scenario 2 for error
	percantage2=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[98,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", percantage2);
	common_call.highlight_element(percantage2, 2, 5)
	percantage2.clear()
	time.sleep(3)

	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)

	#Error 2
	Error2 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[192,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Error2);
	common_call.highlight_element(Error2, 2, 5)
	print(Error2.text)
	search_result.append(Error2.text)
	time.sleep(7)

	#Fixed amount
	Fixedamount =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[190,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Fixedamount);
	common_call.highlight_element(Fixedamount, 2, 5)
	print(Fixedamount.text)
	Fixedamount.click()
	time.sleep(3)

	#Fixed amount input box
	FIXinput=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[191,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", FIXinput);
	common_call.highlight_element(FIXinput, 2, 5)
	FIXinput.clear()
	time.sleep(3)
	#Next Button Click
	Next_button =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[32,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Next_button);
	common_call.highlight_element(Next_button, 2, 5)
	print(Next_button.text)
	driver.implicitly_wait(20)
	Next_button.click()
	time.sleep(7)
	#Error 3
	#if (device == 'Safari/15'):
	Error2 =driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[192,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", Error2);
	common_call.highlight_element(Error2, 2, 5)
	ER=Error2.text.lstrip()
	print(ER)
	search_result.append(ER.rstrip())
	time.sleep(7)

	#Fixed amount input box
	FIXinput=driver.find_element(by=By.XPATH, value=(Search_element_sheet.loc[191,'accessbility_id']))
	driver.execute_script("arguments[0].scrollIntoView()", FIXinput);
	common_call.highlight_element(FIXinput, 2, 5)
	FIXinput.clear()
	FIXinput.send_keys('234')
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
search_result = val_1st_purchase_Changes_to_Initial_adviser_charges_Immediate_Crystallization()

session_id=common_call.get_session_id(driver)
print(session_id)
time.sleep(10)
actual_result_list=search_result
output_df=common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)

driver.quit()
common_call.stop_local()