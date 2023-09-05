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

jira_id,Username,Password,name,env,device,platform,user_type=common_call.auto_fun('Val_2nd_Purchase_Adviser_Money_In_and_Money_Out_GIA')

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

    input_file_name = "Val_2nd_Purchase_Adviser_Money_In_and_Money_Out_GIA_input.csv"
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
    SearchClient_by.send_keys("21044351")
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

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[226, 'accessibility_id'])))
    ProductSelect_GIA = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[226, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ProductSelect_GIA)
    common_call.highlight_element(ProductSelect_GIA, 2, 5)
    print(ProductSelect_GIA.text)
    err_results.append(ProductSelect_GIA.text)
    ProductSelect_GIA.click()

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

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])))
    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Next)
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    Next.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[190, 'accessibility_id'])))
    WithoutSelectContValidation = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[190, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",WithoutSelectContValidation)
    common_call.highlight_element(WithoutSelectContValidation, 2, 5)
    validateerror=WithoutSelectContValidation.text.lstrip()
    print(validateerror.rstrip())
    err_results.append(validateerror.rstrip())
    time.sleep(2)

    ContributionList = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[194, 'accessibility_id'])
    for contribution in ContributionList:
        driver.execute_script("arguments[0].scrollIntoView()",contribution)
        common_call.highlight_element(contribution, 2, 5)
        print(contribution.text)
        err_results.append(contribution.text)
        contribution.click()
        time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])))
    Next = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[41, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Next)
    common_call.highlight_element(Next, 2, 5)
    print(Next.text)
    Next.click()
    time.sleep(2)

    EachContValidation_single = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[191, 'accessibility_id'])
    EachContValidation_indexation = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[192, 'accessibility_id'])
    EachContValidationSel = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[193, 'accessibility_id'])
    for eachvalidation in EachContValidation_single:
        driver.execute_script("arguments[0].scrollIntoView()",eachvalidation)
        common_call.highlight_element(eachvalidation, 2, 5)
        validateerror=eachvalidation.text.lstrip()
        print(validateerror.rstrip())
        err_results.append(validateerror.rstrip())
        time.sleep(1)
    time.sleep(1)
    for eachvalidationin in EachContValidation_indexation:
        driver.execute_script("arguments[0].scrollIntoView()",eachvalidationin)
        common_call.highlight_element(eachvalidationin, 2, 5)
        validateerror=eachvalidationin.text.lstrip()
        print(validateerror.rstrip())
        err_results.append(validateerror.rstrip())
        time.sleep(1)
    time.sleep(1)
    for eachvalidationSe in EachContValidationSel:
        driver.execute_script("arguments[0].scrollIntoView()",eachvalidationSe)
        common_call.highlight_element(eachvalidationSe, 2, 5)
        validateerror=eachvalidationSe.text.lstrip()
        print(validateerror.rstrip())
        err_results.append(validateerror.rstrip())
        time.sleep(1)

    ContributionList = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[194, 'accessibility_id'])
    ChangeSelection = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[252, 'accessibility_id'])
    for contribution in ContributionList:
        driver.execute_script("arguments[0].scrollIntoView()",contribution)
        common_call.highlight_element(contribution, 2, 5)
        print(contribution.text)
        #err_results.append(contribution.text)
        if contribution.text != 'Transfer in':
            contribution.click()
        if contribution.text == 'Transfer in':
            contribution.click()
            time.sleep(1)
            common_call.highlight_element(ChangeSelection, 2, 5)
            ChangeSelection.click()
            break
        time.sleep(1)
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[197, 'accessibility_id'])))
    Contribution1 = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[197, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Contribution1)
    common_call.highlight_element(Contribution1, 2, 5)
    print(Contribution1.text)
    #err_results.append(Contribution1.text)
    Contribution1.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[228, 'accessibility_id'])))
    NetAmount = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[228, 'accessibility_id'])
    NetAmount.send_keys("1400")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[198, 'accessibility_id'])))
    Contribution2 = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[198, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Contribution2)
    common_call.highlight_element(Contribution2, 2, 5)
    print(Contribution2.text)
    #err_results.append(Contribution1.text)
    Contribution2.click()
    time.sleep(2)
    Reg_widrl_Payment = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[233, 'accessibility_id'])
    for regWith in Reg_widrl_Payment:
        if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest') or (device == 'Chrome/110') or (device == 'Edge/109'):
            if regWith.text == 'Regular payments':
                driver.execute_script("arguments[0].scrollIntoView()",regWith)
                common_call.highlight_element(regWith, 2, 5)
                RP = regWith.text.lstrip()
                print(RP.rstrip())
                err_results.append(RP.rstrip())
                regWith.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[229, 'accessibility_id'])))
                RegPayment = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[229, 'accessibility_id'])
                RegPayment.send_keys("200")
                Content_RPW_GIA = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[230, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",Content_RPW_GIA)
                common_call.highlight_element(Content_RPW_GIA, 2, 5)
                print(Content_RPW_GIA.text)
                #err_results.append(Content_RPW_GIA.text)
                Indexation = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[243, 'accessibility_id'])
                for eachindex in Indexation:
                    if eachindex.text == 'None':
                        eachindex.click()
                        print(eachindex.text)
                        err_results.append(eachindex.text)
                    if eachindex.text == 'Retail Price Index':
                        eachindex.click()
                        print(eachindex.text)
                        err_results.append(eachindex.text)
                time.sleep(1)
                IndexationLink = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[208, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",IndexationLink)
                common_call.highlight_element(IndexationLink, 2, 5)
                print(IndexationLink.text)
                err_results.append(IndexationLink.text)
                IndexationLink.click()

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])))
                IndexationDoc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",IndexationDoc)
                common_call.highlight_element(IndexationDoc, 2, 5)
                print(IndexationDoc.text)
                #err_results.append(IndexationDoc.text)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])))
                Indexation_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",Indexation_Doc_Close)
                common_call.highlight_element(Indexation_Doc_Close, 2, 5)
                print(Indexation_Doc_Close.text)
                err_results.append(Indexation_Doc_Close.text)
                Indexation_Doc_Close.click()
            time.sleep(2)

            if regWith.text == 'Regular withdrawals':
                driver.execute_script("arguments[0].scrollIntoView()",regWith)
                common_call.highlight_element(regWith, 2, 5)
                RW=regWith.text.lstrip()
                print(RW.rstrip())
                err_results.append(RW.rstrip())
                regWith.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[196, 'accessibility_id'])))
                ChangeSelection = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[196, 'accessibility_id'])
                common_call.highlight_element(ChangeSelection, 2, 5)
                ChangeSelection.click()
                time.sleep(2)

                WithdrawlType = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[232, 'accessibility_id'])
                for type in WithdrawlType:
                    if type.text == 'Percentage of product value':
                        print(type.text)
                        err_results.append(type.text)
                        type.click()
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[234, 'accessibility_id'])))
                        ProductValuepercentage = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[234, 'accessibility_id'])
                        ProductValuepercentage.send_keys('10')

                        Cal_PVP_Link = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[235, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Cal_PVP_Link)
                        common_call.highlight_element(Cal_PVP_Link, 2, 5)
                        print(Cal_PVP_Link.text)
                        err_results.append(Cal_PVP_Link.text)
                        Cal_PVP_Link.click()

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[236, 'accessibility_id'])))
                        Cal_PVP_Doc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[236, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Cal_PVP_Doc)
                        common_call.highlight_element(Cal_PVP_Doc, 2, 5)
                        print(Cal_PVP_Doc.text)
                        #err_results.append(IndexationDoc.text)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[253, 'accessibility_id'])))
                        Indexation_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[253, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Indexation_Doc_Close)
                        common_call.highlight_element(Indexation_Doc_Close, 2, 5)
                        print(Indexation_Doc_Close.text)
                        err_results.append(Indexation_Doc_Close.text)
                        Indexation_Doc_Close.click()
                    time.sleep(2)

                    if type.text == 'Fixed amount':
                        driver.execute_script("arguments[0].scrollIntoView()",type)
                        common_call.highlight_element(type, 2, 5)
                        print(type.text)
                        err_results.append(type.text)
                        type.click()
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[237, 'accessibility_id'])))
                        regularwithdrawl = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[237, 'accessibility_id'])
                        regularwithdrawl.send_keys('10')
                        time.sleep(1)

                        fre_reg_date = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[238, 'accessibility_id'])
                        for frequency in fre_reg_date:
                            if frequency.text == 'Yearly':
                                driver.execute_script("arguments[0].scrollIntoView()",frequency)
                                common_call.highlight_element(frequency, 2, 5)
                                print(frequency.text)
                                err_results.append(frequency.text)
                                frequency.click()

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[239, 'accessibility_id'])))
                        StartMonth = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[239, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",StartMonth)
                        common_call.highlight_element(StartMonth, 2, 5)
                        #print(StartMonth.text)
                        #err_results.append(StartMonth.text)
                        StartMonth.click()
                        time.sleep(1)

                        SelectMonth = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[240, 'accessibility_id'])
                        for selmonth in SelectMonth:
                            driver.execute_script("arguments[0].scrollIntoView()",selmonth)
                            common_call.highlight_element(selmonth, 2, 5)
                            print(selmonth.text)
                            err_results.append(selmonth.text)
                            selmonth.click()
                            break

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[239, 'accessibility_id'])))
                        StartDate = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[241, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",StartDate)
                        common_call.highlight_element(StartDate, 2, 5)
                        #print(StartDate.text)
                        #err_results.append(StartDate.text)
                        StartDate.click()
                        time.sleep(1)

                        SelectDate = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[242, 'accessibility_id'])
                        for seldate in SelectDate:
                            driver.execute_script("arguments[0].scrollIntoView()",seldate)
                            common_call.highlight_element(seldate, 2, 5)
                            print(seldate.text)
                            err_results.append(seldate.text)
                            seldate.click()
                            break
                        time.sleep(1)

                        Indexation = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[243, 'accessibility_id'])
                        for eachindex in Indexation:
                            if eachindex.text == 'None':
                                eachindex.click()
                                print(eachindex.text)
                                err_results.append(eachindex.text)
                            if eachindex.text == 'Retail Price Index':
                                eachindex.click()
                                print(eachindex.text)
                                err_results.append(eachindex.text)
                            if eachindex.text == 'Percentage':
                                eachindex.click()
                                print(eachindex.text)
                                err_results.append(eachindex.text)
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[244, 'accessibility_id'])))
                                Percentage = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[244, 'accessibility_id'])
                                Percentage.send_keys('4')

                        time.sleep(1)
                        IndexationLink = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[208, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",IndexationLink)
                        common_call.highlight_element(IndexationLink, 2, 5)
                        print(IndexationLink.text)
                        err_results.append(IndexationLink.text)
                        IndexationLink.click()

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])))
                        IndexationDoc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",IndexationDoc)
                        common_call.highlight_element(IndexationDoc, 2, 5)
                        print(IndexationDoc.text)
                        #err_results.append(IndexationDoc.text)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])))
                        Indexation_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Indexation_Doc_Close)
                        common_call.highlight_element(Indexation_Doc_Close, 2, 5)
                        print(Indexation_Doc_Close.text)
                        err_results.append(Indexation_Doc_Close.text)
                        Indexation_Doc_Close.click()

        if (device == 'Safari/15'):
            if regWith.text == 'Regular payments ':
                driver.execute_script("arguments[0].scrollIntoView()",regWith)
                common_call.highlight_element(regWith, 2, 5)
                RP = regWith.text.lstrip()
                print(RP.rstrip())
                err_results.append(RP.rstrip())
                regWith.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[229, 'accessibility_id'])))
                RegPayment = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[229, 'accessibility_id'])
                RegPayment.send_keys("200")
                Content_RPW_GIA = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[230, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",Content_RPW_GIA)
                common_call.highlight_element(Content_RPW_GIA, 2, 5)
                print(Content_RPW_GIA.text)
                #err_results.append(Content_RPW_GIA.text)
                Indexation = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[243, 'accessibility_id'])
                for eachindex in Indexation:
                    if eachindex.text == 'None':
                        eachindex.click()
                        print(eachindex.text)
                        err_results.append(eachindex.text)
                    if eachindex.text == 'Retail Price Index':
                        eachindex.click()
                        print(eachindex.text)
                        err_results.append(eachindex.text)
                time.sleep(1)
                IndexationLink = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[208, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",IndexationLink)
                common_call.highlight_element(IndexationLink, 2, 5)
                print(IndexationLink.text)
                err_results.append(IndexationLink.text)
                IndexationLink.click()

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])))
                IndexationDoc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",IndexationDoc)
                common_call.highlight_element(IndexationDoc, 2, 5)
                print(IndexationDoc.text)
                #err_results.append(IndexationDoc.text)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])))
                Indexation_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])
                driver.execute_script("arguments[0].scrollIntoView()",Indexation_Doc_Close)
                common_call.highlight_element(Indexation_Doc_Close, 2, 5)
                print(Indexation_Doc_Close.text)
                err_results.append(Indexation_Doc_Close.text)
                Indexation_Doc_Close.click()
            time.sleep(2)

            if regWith.text == 'Regular withdrawals ':
                driver.execute_script("arguments[0].scrollIntoView()",regWith)
                common_call.highlight_element(regWith, 2, 5)
                RW=regWith.text.lstrip()
                print(RW.rstrip())
                err_results.append(RW.rstrip())
                regWith.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[196, 'accessibility_id'])))
                ChangeSelection = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[196, 'accessibility_id'])
                common_call.highlight_element(ChangeSelection, 2, 5)
                ChangeSelection.click()
                time.sleep(2)

                WithdrawlType = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[232, 'accessibility_id'])
                for type in WithdrawlType:
                    if type.text == 'Percentage of product value':
                        print(type.text)
                        err_results.append(type.text)
                        type.click()
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[234, 'accessibility_id'])))
                        ProductValuepercentage = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[234, 'accessibility_id'])
                        ProductValuepercentage.send_keys('10')

                        Cal_PVP_Link = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[235, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Cal_PVP_Link)
                        common_call.highlight_element(Cal_PVP_Link, 2, 5)
                        print(Cal_PVP_Link.text)
                        err_results.append(Cal_PVP_Link.text)
                        Cal_PVP_Link.click()

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[236, 'accessibility_id'])))
                        Cal_PVP_Doc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[236, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Cal_PVP_Doc)
                        common_call.highlight_element(Cal_PVP_Doc, 2, 5)
                        print(Cal_PVP_Doc.text)
                        #err_results.append(IndexationDoc.text)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[253, 'accessibility_id'])))
                        Indexation_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[253, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Indexation_Doc_Close)
                        common_call.highlight_element(Indexation_Doc_Close, 2, 5)
                        print(Indexation_Doc_Close.text)
                        err_results.append(Indexation_Doc_Close.text)
                        Indexation_Doc_Close.click()
                    time.sleep(2)

                    if type.text == 'Fixed amount':
                        driver.execute_script("arguments[0].scrollIntoView()",type)
                        common_call.highlight_element(type, 2, 5)
                        print(type.text)
                        err_results.append(type.text)
                        type.click()
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[237, 'accessibility_id'])))
                        regularwithdrawl = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[237, 'accessibility_id'])
                        regularwithdrawl.send_keys('10')
                        time.sleep(1)

                        fre_reg_date = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[238, 'accessibility_id'])
                        for frequency in fre_reg_date:
                            if frequency.text == 'Yearly':
                                driver.execute_script("arguments[0].scrollIntoView()",frequency)
                                common_call.highlight_element(frequency, 2, 5)
                                print(frequency.text)
                                err_results.append(frequency.text)
                                frequency.click()

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[239, 'accessibility_id'])))
                        StartMonth = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[239, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",StartMonth)
                        common_call.highlight_element(StartMonth, 2, 5)
                        #print(StartMonth.text)
                        #err_results.append(StartMonth.text)
                        StartMonth.click()
                        time.sleep(1)

                        SelectMonth = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[240, 'accessibility_id'])
                        for selmonth in SelectMonth:
                            driver.execute_script("arguments[0].scrollIntoView()",selmonth)
                            common_call.highlight_element(selmonth, 2, 5)
                            print(selmonth.text)
                            err_results.append(selmonth.text)
                            selmonth.click()
                            break

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[239, 'accessibility_id'])))
                        StartDate = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[241, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",StartDate)
                        common_call.highlight_element(StartDate, 2, 5)
                        #print(StartDate.text)
                        #err_results.append(StartDate.text)
                        StartDate.click()
                        time.sleep(1)

                        SelectDate = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[242, 'accessibility_id'])
                        for seldate in SelectDate:
                            driver.execute_script("arguments[0].scrollIntoView()",seldate)
                            common_call.highlight_element(seldate, 2, 5)
                            print(seldate.text)
                            err_results.append(seldate.text)
                            seldate.click()
                            break
                        time.sleep(1)

                        Indexation = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[243, 'accessibility_id'])
                        for eachindex in Indexation:
                            if eachindex.text == 'None':
                                eachindex.click()
                                print(eachindex.text)
                                err_results.append(eachindex.text)
                            if eachindex.text == 'Retail Price Index':
                                eachindex.click()
                                print(eachindex.text)
                                err_results.append(eachindex.text)
                            if eachindex.text == 'Percentage':
                                eachindex.click()
                                print(eachindex.text)
                                err_results.append(eachindex.text)
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[244, 'accessibility_id'])))
                                Percentage = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[244, 'accessibility_id'])
                                Percentage.send_keys('4')

                        time.sleep(1)
                        IndexationLink = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[208, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",IndexationLink)
                        common_call.highlight_element(IndexationLink, 2, 5)
                        print(IndexationLink.text)
                        err_results.append(IndexationLink.text)
                        IndexationLink.click()

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])))
                        IndexationDoc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[210, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",IndexationDoc)
                        common_call.highlight_element(IndexationDoc, 2, 5)
                        print(IndexationDoc.text)
                        #err_results.append(IndexationDoc.text)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])))
                        Indexation_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[211, 'accessibility_id'])
                        driver.execute_script("arguments[0].scrollIntoView()",Indexation_Doc_Close)
                        common_call.highlight_element(Indexation_Doc_Close, 2, 5)
                        print(Indexation_Doc_Close.text)
                        err_results.append(Indexation_Doc_Close.text)
                        Indexation_Doc_Close.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[199, 'accessibility_id'])))
    Contribution3 = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[199, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Contribution3)
    common_call.highlight_element(Contribution3, 2, 5)
    print(Contribution3.text)
    #err_results.append(Contribution1.text)
    Contribution3.click()

    Fulltransfer = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[217, 'accessibility_id'])
    for Full in Fulltransfer:
        driver.execute_script("arguments[0].scrollIntoView()",Full)
        common_call.highlight_element(Full, 2, 5)
        print(Full.text)
        err_results.append(Full.text)
        if Full.text == "Yes":
            Full.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[220, 'accessibility_id'])))
    transferAmt = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[220, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",transferAmt)
    common_call.highlight_element(transferAmt, 2, 5)
    IsPresenttransAmt=str(transferAmt.is_displayed())
    print(IsPresenttransAmt)
    err_results.append(IsPresenttransAmt)
    transferAmt.send_keys('1200')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[219, 'accessibility_id'])))
    Prodref = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[219, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Prodref)
    common_call.highlight_element(Prodref, 2, 5)
    IsPresentProdref=str(Prodref.is_displayed())
    print(IsPresentProdref)
    err_results.append(IsPresentProdref)
    Prodref.send_keys('QA')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[73, 'accessibility_id'])))
    Transprov = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[73, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Transprov)
    common_call.highlight_element(Transprov, 2, 5)
    IsPresenttransprov=str(Transprov.is_displayed())
    print(IsPresenttransprov)
    err_results.append(IsPresenttransprov)
    Transprov.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[74, 'accessibility_id'])))
    ValidateTransferprovider = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[74, 'accessibility_id'])
    if (device == 'Chrome/latest') or (device == 'Edge/latest') or (device == 'Firefox/latest'):
        common_call.highlight_element(ValidateTransferprovider, 2, 5)
    print(ValidateTransferprovider.text)
    err_results.append(ValidateTransferprovider.text)
    time.sleep(3)

    SaveCancel = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[78, 'accessibility_id'])
    for save in SaveCancel:
        if save.text == 'Save':
            driver.execute_script("arguments[0].scrollIntoView()",save)
            common_call.highlight_element(save, 2, 5)
            print(save.text)
            err_results.append(save.text)
            save.click()
    time.sleep(3)

    TP_error_withoutselectTP = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[79, 'accessibility_id'])
    common_call.highlight_element(TP_error_withoutselectTP, 2, 5)
    Err=TP_error_withoutselectTP.text.lstrip()
    print(Err.rstrip())
    err_results.append(Err.rstrip())
    time.sleep(5)

    driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[225, 'accessibility_id']).send_keys('pra')
    time.sleep(2)

    Transferprovider_dropdown = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[76,'accessibility_id'])
    for TP in Transferprovider_dropdown:
        common_call.highlight_element(TP, 2, 5)
        print(TP.text)
        TP.click()
        break
    time.sleep(5)

    driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[225, 'accessibility_id']).click()
    time.sleep(2)

    Transferprovider_dropdown = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[76,'accessibility_id'])
    for TP in Transferprovider_dropdown:
        if TP.text == 'Praemium Retirement Account':
            common_call.highlight_element(TP, 2, 5)
            print(TP.text)
            TP.click()
            break
    time.sleep(5)

    SaveCancel = driver.find_elements(By.XPATH,Quotes_applications_element_sheet_input.loc[78, 'accessibility_id'])
    for save in SaveCancel:
        if save.text == 'Save':
            driver.execute_script("arguments[0].scrollIntoView()",save)
            common_call.highlight_element(save, 2, 5)
            print(save.text)
            err_results.append(save.text)
            save.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[250, 'accessibility_id'])))
    ReRegLink = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[250, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ReRegLink)
    common_call.highlight_element(ReRegLink, 2, 5)
    ReRegLK = ReRegLink.text.lstrip()
    print(ReRegLK.rstrip())
    err_results.append(ReRegLK.rstrip())
    ReRegLink.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[249, 'accessibility_id'])))
    ReRegDoc = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[249, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ReRegDoc)
    common_call.highlight_element(ReRegDoc, 2, 5)
    print(ReRegDoc.text)
    #err_results.append(ReRegDoc.text)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[254, 'accessibility_id'])))
    ReReg_Doc_Close = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[254, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",ReReg_Doc_Close)
    common_call.highlight_element(ReReg_Doc_Close, 2, 5)
    print(ReReg_Doc_Close.text)
    err_results.append(ReReg_Doc_Close.text)
    ReReg_Doc_Close.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[255, 'accessibility_id'])))
    Add_Invst_ReReg = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[255, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Add_Invst_ReReg)
    common_call.highlight_element(Add_Invst_ReReg, 2, 5)
    print(Add_Invst_ReReg.text)
    err_results.append(Add_Invst_ReReg.text)
    Add_Invst_ReReg.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[256, 'accessibility_id'])))
    ReReg_Assetsearch = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[256, 'accessibility_id'])
    ReReg_Assetsearch.send_keys('Black')

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[257, 'accessibility_id'])))
    Add_reInvest = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[257, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Add_reInvest)
    common_call.highlight_element(Add_reInvest, 2, 5)
    print(Add_reInvest.text)
    Add_reInvest.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[258, 'accessibility_id'])))
    Close_reInvest_Searchbar = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[258, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Close_reInvest_Searchbar)
    common_call.highlight_element(Close_reInvest_Searchbar, 2, 5)
    print(Close_reInvest_Searchbar.text)
    #err_results.append(Close_reInvest_Searchbar.text)
    Close_reInvest_Searchbar.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[259, 'accessibility_id'])))
    ReReg_AllocationPer = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[259, 'accessibility_id'])
    ReReg_AllocationPer.send_keys('100')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,Quotes_applications_element_sheet_input.loc[224, 'accessibility_id'])))
    Save = driver.find_element(By.XPATH,Quotes_applications_element_sheet_input.loc[224, 'accessibility_id'])
    driver.execute_script("arguments[0].scrollIntoView()",Save)
    common_call.highlight_element(Save, 2, 5)
    print(Save.text)
    err_results.append(Save.text)
    Save.click()
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
