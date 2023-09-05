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

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('Val_2nd_Purchase_Adviser_Investment_Allocation_page')

BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY,caps,web_address,op_filename,input_file,output_file=common_call.fun(platform,device,env,name,jira_id,user_type)

#Lunching driver browser
driver = webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
if ((platform[:7] =='Windows') or (platform[:2] =='OS')):
    driver.set_window_size(1600,1200)
functional_common_call.maximize_driver_window(driver)


def val_error_multiple_spaces(driver):
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[0, 'accessibility_id'])))
    driver.implicitly_wait(10)
    global input_file_name
    err_results = []
    input_list=[]

    input_file_name = "Val_2nd_Purchase_Adviser_Investment_Allocation_page_input.csv"
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
    SearchClient_by.send_keys("20821500")
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
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/110') or (device == 'Edge/109'):
        mis_text = Proposition_screen_validation.text[:5]
        cis_text = Proposition_screen_validation.text[-21:]
        err_results.append(cis_text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[149, 'accessibility_id'])))
    SelectPlatformRadioButton = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[149, 'accessibility_id'])
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
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/110') or (device == 'Edge/109'):
        mis_text = ProductSelection_screen_validation.text[:5]
        cis_text = ProductSelection_screen_validation.text[-17:]
        err_results.append(cis_text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[153, 'accessibility_id'])))
    AdvicecRadiobutton_Yes = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[153, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",AdvicecRadiobutton_Yes)
    common_call.highlight_element(AdvicecRadiobutton_Yes, 2, 5)
    print(AdvicecRadiobutton_Yes.text)
    err_results.append(AdvicecRadiobutton_Yes.text)
    print('Advice radio button selected : ' + str(AdvicecRadiobutton_Yes.is_selected()))
    err_results.append(AdvicecRadiobutton_Yes.is_selected())
    AdvicecRadiobutton_Yes.click()
    time.sleep(1)
    checked_att = AdvicecRadiobutton_Yes.get_attribute("aria-checked")
    if("true" in checked_att):
        print("radio button found checked")
        err_results.append("True")

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

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[260, 'accessibility_id'])))
    ProductSelect_ISA = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[260, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ProductSelect_ISA)
    common_call.highlight_element(ProductSelect_ISA, 2, 5)
    print(ProductSelect_ISA.text)
    err_results.append(ProductSelect_ISA.text)
    ProductSelect_ISA.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])))
    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Next)
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    err_results.append(Next.text)
    Next.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])))
    MoneyInOutSIPP_screen_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",MoneyInOutSIPP_screen_validation)
    common_call.highlight_element(MoneyInOutSIPP_screen_validation, 2, 5)
    print(MoneyInOutSIPP_screen_validation.text)
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[197, 'accessibility_id'])))
    Contribution1 = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[197, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Contribution1)
    common_call.highlight_element(Contribution1, 2, 5)
    print(Contribution1.text)
    err_results.append(Contribution1.text)
    Contribution1.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[228, 'accessibility_id'])))
    NetAmount = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[228, 'accessibility_id'])
    NetAmount.send_keys("1400")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])))
    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Next)
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    err_results.append(Next.text)
    Next.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])))
    Investmentoption_screen_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Investmentoption_screen_validation)
    common_call.highlight_element(Investmentoption_screen_validation, 2, 5)
    mis_text = Investmentoption_screen_validation.text[:5]
    cis_text = Investmentoption_screen_validation.text[-18:]
    print(cis_text)
    err_results.append(cis_text)
    time.sleep(5)

    Investmentoptions_select = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[107, 'accessibility_id'])
    for selectinvestments in Investmentoptions_select:
        if (device == 'Safari/15'):
            if selectinvestments.text == 'Select investments ':
                common_call.highlight_element(selectinvestments, 2, 5)
                SelInvest= selectinvestments.text.lstrip()
                print(SelInvest.rstrip())
                err_results.append(SelInvest.rstrip())
                selectinvestments.click()

        if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/110') or (device == 'Edge/109'):
            if selectinvestments.text == 'Select investments':
                common_call.highlight_element(selectinvestments, 2, 5)
                SelInvest= selectinvestments.text.lstrip()
                print(SelInvest.rstrip())
                err_results.append(SelInvest.rstrip())
                selectinvestments.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])))
    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    err_results.append(Next.text)
    Next.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])))
    InvestmentSearch_screen_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",InvestmentSearch_screen_validation)
    common_call.highlight_element(InvestmentSearch_screen_validation, 2, 5)
    print(InvestmentSearch_screen_validation.text)
    if (device == 'Safari/15'):
        mis_text = InvestmentSearch_screen_validation.text[:5].lstrip()
        cis_text = InvestmentSearch_screen_validation.text[-18:].lstrip()
        err_results.append(cis_text.rstrip())
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/110') or (device == 'Edge/109'):
        mis_text = InvestmentSearch_screen_validation.text[:5].lstrip()
        cis_text = InvestmentSearch_screen_validation.text[-17:].lstrip()
        err_results.append(cis_text.rstrip())

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[112, 'accessibility_id'])))
    AssetSearch = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[112, 'accessibility_id'])
    AssetSearch.send_keys('7IM AAP Income C Inc')
    time.sleep(15)

    Asset_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[113, 'accessibility_id'])
    common_call.highlight_element(Asset_validation, 2, 5)
    print(Asset_validation.text)
    err_results.append(Asset_validation.text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[115, 'accessibility_id'])))
    AddButton = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[115, 'accessibility_id'])
    common_call.highlight_element(AddButton, 2, 5)
    print(AddButton.text)
    AddButton.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])))
    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Next)
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    err_results.append(Next.text)
    Next.click()
    time.sleep(2)

    InvestmentAllocation_screen_validation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[28, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",InvestmentAllocation_screen_validation)
    common_call.highlight_element(InvestmentAllocation_screen_validation, 2, 5)
    if (device == 'Safari/15'):
        mis_text = InvestmentAllocation_screen_validation.text[:5].lstrip()
        cis_text = InvestmentAllocation_screen_validation.text[-21:].lstrip()
        print(cis_text.rstrip())
        err_results.append(cis_text.rstrip())
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/110') or (device == 'Edge/109'):
        mis_text = InvestmentAllocation_screen_validation.text[:5].lstrip()
        cis_text = InvestmentAllocation_screen_validation.text[-21:].lstrip()
        print(cis_text.rstrip())
        err_results.append(cis_text.rstrip())

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[272, 'accessibility_id'])))
    ValidateAsset = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[272, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ValidateAsset)
    common_call.highlight_element(ValidateAsset, 2, 5)
    print(ValidateAsset.text)
    err_results.append(ValidateAsset.text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[116, 'accessibility_id'])))
    ValidateAssetpercentage = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[116, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ValidateAssetpercentage)
    common_call.highlight_element(ValidateAssetpercentage, 2, 5)
    print(ValidateAssetpercentage.text)
    ValidateAssetpercentage.send_keys('99.75')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[119, 'accessibility_id'])))
    ValidateEditInvestment = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[119, 'accessibility_id'])
    common_call.highlight_element(ValidateEditInvestment, 2, 5)
    EditInvest= ValidateEditInvestment.text.lstrip()
    print(EditInvest.rstrip())
    err_results.append(EditInvest.rstrip())
    time.sleep(1)

    RebalancingOption = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[107, 'accessibility_id'])
    for rebalancing in RebalancingOption:
        if rebalancing.text == 'None':
            driver.execute_script("arguments[0].scrollIntoView()",rebalancing)
            common_call.highlight_element(rebalancing, 2, 5)
            print(rebalancing.text)
            err_results.append(rebalancing.text)
            rebalancing.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[120, 'accessibility_id'])))
    CreateBreakdown = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[120, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",CreateBreakdown)
    common_call.highlight_element(CreateBreakdown, 2, 5)
    print(CreateBreakdown.text)
    err_results.append(CreateBreakdown.text)
    CreateBreakdown.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[121, 'accessibility_id'])))
    DownloadBreakdown = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[121, 'accessibility_id'])
    common_call.highlight_element(DownloadBreakdown, 2, 5)
    print(DownloadBreakdown.text)
    err_results.append(DownloadBreakdown.text)
    DownloadBreakdown.click()
    time.sleep(5)

    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    err_results.append(Next.text)
    Next.click()


    time.sleep(2)
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
