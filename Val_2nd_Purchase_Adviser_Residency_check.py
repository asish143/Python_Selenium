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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import string
import random



#Common element sheet
login_element_sheet,mfa_element_sheet,Global_Search_element_sheet,Member_Search_element_sheet,User_Search_element_sheet,adhoc_adviser_charge_element_sheet,manage_investment_income_element_sheet,equity_trading_element_sheet,viewquote_element_sheet,Search_element_sheet,Quotes_applications_element_sheet_input=common_call.get_element_sheet()

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('Val_2nd_Purchase_Adviser_Residency_check')

BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)

#Lunching driver browser
driver = webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
if ((platform[:7] =='Windows') or (platform[:2] =='OS')):
    driver.set_window_size(1600,1200)
functional_common_call.maximize_driver_window(driver)

def val_error_multiple_spaces(driver):
    time.sleep(10)
    global input_file_name
    err_results = []
    input_list=[]

    input_file_name = "Val_2nd_Purchase_Adviser_Residency_check_input.csv"
    input_df= pd.read_csv(input_file+input_file_name,encoding='cp1252')

    GlobalSearch_button = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[156, 'accessibility_id'])
    common_call.highlight_element(GlobalSearch_button, 2, 5)
    err_results.append(GlobalSearch_button.text)
    print(GlobalSearch_button.text)
    GlobalSearch_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[157, 'accessibility_id'])))
    SearchClient_by = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[157, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",SearchClient_by)
    common_call.highlight_element(SearchClient_by, 2, 5)
    SearchClient_by.send_keys("20856004")
    SearchClient_by.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[163, 'accessibility_id'])))
    Selectclient = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[163, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Selectclient)
    common_call.highlight_element(Selectclient, 2, 5)
    err_results.append(Selectclient.text)
    print(Selectclient.text)
    Selectclient.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[160, 'accessibility_id'])))
    SelectcbuyProduct = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[160, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",SelectcbuyProduct)
    common_call.highlight_element(SelectcbuyProduct, 2, 5)
    err_results.append(SelectcbuyProduct.text)
    print(SelectcbuyProduct.text)
    SelectcbuyProduct.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])))
    Proposition_screen_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Proposition_screen_validation)
    common_call.highlight_element(Proposition_screen_validation, 2, 5)
    print(Proposition_screen_validation.text)
    if (device == 'Safari/15'):
        mis_text = Proposition_screen_validation.text[:5]
        cis_text = Proposition_screen_validation.text[-22:]
        err_results.append(cis_text.rstrip())
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/109') or (device == 'Edge/109'):
        mis_text = Proposition_screen_validation.text[:5]
        cis_text = Proposition_screen_validation.text[-21:]
        err_results.append(cis_text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[30, 'accessibility_id'])))
    StartButton = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[30, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",StartButton)
    common_call.highlight_element(StartButton, 2, 5)
    print(StartButton.text)
    err_results.append(StartButton.text)
    StartButton.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[165, 'accessibility_id'])))
    ValidationError = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[165, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ValidationError)
    common_call.highlight_element(ValidationError, 2, 5)
    validateerror=ValidationError.text.lstrip()
    print(validateerror.rstrip())
    err_results.append(validateerror.rstrip())

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[150, 'accessibility_id'])))
    SelectPlatformRadioButton = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[150, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",SelectPlatformRadioButton)
    common_call.highlight_element(SelectPlatformRadioButton, 2, 5)
    print(SelectPlatformRadioButton.text)
    err_results.append(SelectPlatformRadioButton.text.rstrip())
    SelectPlatformRadioButton.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[30, 'accessibility_id'])))
    StartButton = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[30, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",StartButton)
    common_call.highlight_element(StartButton, 2, 5)
    print(StartButton.text)
    err_results.append(StartButton.text)
    StartButton.click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])))
    ProductSelection_screen_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ProductSelection_screen_validation)
    common_call.highlight_element(ProductSelection_screen_validation, 2, 5)
    print(ProductSelection_screen_validation.text)
    if (device == 'Safari/15'):
        mis_text = ProductSelection_screen_validation.text[:5]
        cis_text = ProductSelection_screen_validation.text[-18:]
        err_results.append(cis_text.rstrip())
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/109') or (device == 'Edge/109'):
        mis_text = ProductSelection_screen_validation.text[:5]
        cis_text = ProductSelection_screen_validation.text[-17:]
        err_results.append(cis_text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[171, 'accessibility_id'])))
    Residentcontent = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[171, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Residentcontent)
    common_call.highlight_element(Residentcontent, 2, 5)
    Resicont=Residentcontent.text.lstrip()
    print(Resicont.rstrip())
    err_results.append(Resicont.rstrip())

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[170, 'accessibility_id'])))
    UKResidentRadiobutton_No = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[170, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",UKResidentRadiobutton_No)
    common_call.highlight_element(UKResidentRadiobutton_No, 2, 5)
    print(UKResidentRadiobutton_No.text)
    err_results.append(UKResidentRadiobutton_No.text)
    print('Advice radio button selected : ' + str(UKResidentRadiobutton_No.is_selected()))
    err_results.append(UKResidentRadiobutton_No.is_selected())
    UKResidentRadiobutton_No.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[173, 'accessibility_id'])))
    UKResidentRadiobutton_No_Validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[173, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",UKResidentRadiobutton_No_Validation)
    common_call.highlight_element(UKResidentRadiobutton_No_Validation, 2, 5)
    validateerror=UKResidentRadiobutton_No_Validation.text.lstrip()
    print(validateerror.rstrip())
    err_results.append(validateerror.rstrip())

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[169, 'accessibility_id'])))
    ResidentRadiobutton_Yes = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[169, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ResidentRadiobutton_Yes)
    common_call.highlight_element(ResidentRadiobutton_Yes, 2, 5)
    print(ResidentRadiobutton_Yes.text)
    err_results.append(ResidentRadiobutton_Yes.text)
    print('Advice radio button selected : ' + str(ResidentRadiobutton_Yes.is_selected()))
    err_results.append(ResidentRadiobutton_Yes.is_selected())
    ResidentRadiobutton_Yes.click()
    time.sleep(1)
    checked_att = ResidentRadiobutton_Yes.get_attribute("aria-checked")
    if("true" in checked_att):
        print("radio button found checked")
        err_results.append("True")



    return err_results,input_file_name

#Validation
functional_common_call.login_quick(Username,Password,driver,web_address)
time.sleep(10)
err_results_1,input_file_name = val_error_multiple_spaces(driver)
#result_list_2 = val_error_multiple_spaces(driver)
result_list = err_results_1
print(result_list)

#Accessibility Testing
# print("Accessibility Testing completed in: " + device)
# functional_common_call.accessibility_testing(device,driver)
session_id=common_call.get_session_id(driver)
print(session_id)
input_df= pd.read_csv(input_file+input_file_name,encoding='cp1252')
print(input_df)

actual_result_list =[]
actual_result_list = result_list.copy()
output_df = common_call.create_output(input_df,actual_result_list,session_id,BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,driver)
print(output_df)
output_df.to_csv(output_file+op_filename+"_output.csv",index = False)
driver.quit()
common_call.stop_local()
