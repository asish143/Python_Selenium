import os, sys, json

env=os.environ

if('JENKINS_URL' in os.environ):
    JB=os.environ['JOB_NAME']
    print("JB:\n",JB)



#JBN=os.environ['JOB_BASE_NAME']
#print("JBN:\n",JBN)




parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
print("Current Directory MASTER PY: ",parentddir)

pov_automation= os.path.dirname(parentddir)
print("PoV Automation MASTER PY: ",pov_automation)


functional_direc_path = os.path.join(pov_automation, 'pyscripts/functional')
print("Pyscript funtional MASTER PY",functional_direc_path)

#Navigate to Strings directory
common_direc_path = os.path.join(pov_automation, 'common')
print("Common MASTER PY: ",common_direc_path)

config_direc_path=os.path.join(pov_automation, 'config/')
print("Config with backword slash MASTER PY : ",config_direc_path)

config_direc_path=(str(config_direc_path)).replace(r'//', '\\')
#config_direc_path=config_direc_path.replace('\\', '/')
print("Config with forward slash MASTER PY : ",config_direc_path)



import json
import sys
import subprocess
sys.path.insert(0, functional_direc_path)
sys.path.insert(0, common_direc_path)
import common_call
import pandas as pd
import numpy as np
import requests

#funtional_py_script_path='C:/Users/vranjan/Desktop/CWR_PoV/automation_Web/browserstack/pov_automation/pyscripts/functional/'
funtional_py_script_path=functional_direc_path.replace('\\', '/')


coversheet_path=common_call.get_coversheet_path() #reading_cover_sheet
coversheet_df=pd.read_csv(coversheet_path)
coversheet_df = coversheet_df.replace(np.nan, '', regex=True)

#coversheet_df=coversheet_df.loc[(coversheet_df['Execution'] == 'yes') & (coversheet_df['Test Defination'] != '')]
#coversheet_df=coversheet_df.drop_duplicates(subset ="Test Defination",keep='first')

'''if('JENKINS_URL' in os.environ):
    JB=os.environ['JOB_NAME']
    print("JB:\n",JB)
    if(JB=='ADX_Web_Regression_Pipeline'):
        coversheet_df = coversheet_df.assign(Execution='yes')
        print(coversheet_df)
    else:
        pass'''



coversheet_df=coversheet_df.loc[(coversheet_df['Execution'] == 'yes')]
print("Count of Test Cases: ",coversheet_df.shape[0])
coversheet_df=coversheet_df.drop_duplicates(subset ="Test Scripts",keep='last')
print(coversheet_df)
print("Count of Test Cases after duplicates removal: ",coversheet_df.shape[0])

#coversheet_df=(coversheet_df.loc[(coversheet_df['Execution']=='yes') or (coversheet_df['Test Defination'] !='')]).any()

#coversheet_df=coversheet_df.loc[coversheet_df['Execution'] =='yes']
#coversheet_df=coversheet_df.loc[coversheet_df['Test Defination'] !='']
if coversheet_df.empty:
    sys.exit('Execution column is marked as no or blank, mark it as yes to run the script')
else:
    print(coversheet_df)


#path ="C:/Users/vranjan/Desktop/CWR_PoV/automation_Web/browserstack/pov_automation/features/"
path=os.path.join(pov_automation, 'features/')
path=path.replace('\\', '/')

for index, column in coversheet_df.iterrows():
    platfrm=column['Device']
    #test_defination=column['Test Defination']
    file_name=column['Test Scripts']
    file_name=file_name+'.py'
    print(platfrm)
    print(file_name)
    #print(test_defination)

    file_name=funtional_py_script_path+'/'+file_name

    if(platfrm=='single'):
        CONFIG = config_direc_path+'single.json'
    elif(platfrm=='parallel1'):
        CONFIG = config_direc_path+'parallel1.json'
    elif(platfrm=='parallel2'):
        CONFIG = config_direc_path+'parallel2.json'
    elif(platfrm!=''):
        CONFIG = config_direc_path+'single.json'
    else:
        sys.exit("JSON issue")
    with open(CONFIG, "r") as f:
        obj = json.loads(f.read())
        num_of_tests = len(obj)
        process = []
    for counter in range(num_of_tests):
        cmd = "python %s %s %s " % (file_name, CONFIG, counter)
        print(cmd)
        process.append(subprocess.Popen(cmd, shell=True))
    for counter in range(num_of_tests):
        process[counter].wait()

