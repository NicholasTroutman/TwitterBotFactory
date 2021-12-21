from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup as bs
from lxml import etree, html
import sys, os
from io import StringIO
from xml.dom.minidom import parse, parseString 
import pandas as pd

#NOTES
#table[5] from the search page

# Fill in your details here to be posted to the login form.

data = {
  'UserName': 'DBergin',
  'Password': 'IrishND10!',
  'ValidateUser': '1',
  'dbKeyAuth': 'JusticeAuth',
  'SignOn': 'Sign On'
}

cookies = {
    'ASP.NET_SessionId': 'b3kgqx55xdpizu55xcembe45',
    'https://securecourtcaseaccess.nmcourts.gov/CaseDetail.aspx?CaseID=8284003': '82FC236DB280128EACAF56DACC52EF0FF0E6E7603C844E2A7931D7E458713A51C053C712E2A21724299137F7583AC8B8637E96E1C4FC43A041AB5E4102CFC5BCC61F061791E3042DE637FB3DAEB49C5CC8B0CE804BC16F7E5F6980044049DA6E89A4EA1BCBED4545BFE3F1A8AE32136133AC4D817676D1736526D02B780E4CA472D240768324B570AFAB93CA2B1BBFD9949981BC',
    'JSESSIONID': '80E3EBC99C7DF079728E94DFAC2667A5'
}



headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://securecourtcaseaccess.nmcourts.gov',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/Search.aspx?ID=100', #CHANGED
    'Accept-Language': 'en-US,en;q=0.9',
}


LOGIN_URL= "https://securecourtcaseaccess.nmcourts.gov/login.aspx"




#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~
#Bernalillo results



headersArea = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://securecourtcaseaccess.nmcourts.gov',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/default.aspx',
    'Accept-Language': 'en-US,en;q=0.9',
}

paramsArea = (
    ('ID', '100'),
)

dataArea = {
  'NodeID': '29111',
  'NodeDesc': 'Bernalillo Metropolitan'
}


DataAreaAll =  {
  'NodeID': '210,220,2210,2220,99,900,1000,1101,1055,1040,1070,1150,1175,1250,1275,1340,1355,1370,2020,3070,3101,3125,3150,4120,4240,4340,5030,5060,6080,6190,6230,7210,7229,7250,7280,8090,8180,8200,9050,9110,25601,150,500,610,700,900,100,1101,1201,1301,1400,1470,1480,1500,1600,1700,1800,1900,1910,1920,2000,2101,2201,2301,2400,2500,2600,2700,2800,2900,3000,3200,3300,3400,3500,3600,3700,3800,4000,4100,4300,4400,4500,4600,4700,4800,4900,5100,5200,5300,5400,5600,5800,5900,6001,29111',
  'NodeDesc': 'All Courts'
}




#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~
#query results from "T-4-CV-2020*"


headersSearch = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://securecourtcaseaccess.nmcourts.gov',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/default.aspx',
    'Accept-Language': 'en-US,en;q=0.9',
}

paramsSearch = (
    ('ID', '100'),
)

dataSearch = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwULLTEwOTk1NTcyNzAPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWgWAgIDDw9kFgIeB29ua2V5dXAFJnRoaXMudmFsdWUgPSB0aGlzLnZhbHVlLnRvTG93ZXJDYXNlKCk7ZGR8gO5bSe+IJNYv7tDJa3aakOK3VQ==',
  '__VIEWSTATEGENERATOR': 'BBBC20B8',
  '__EVENTVALIDATION': '/wEWAgKcp5bHDwKYxoa5COCqIZ6YKaR767+VZ1TuhCYYLd5W',
  'NodeID': '210,220,2210,2220,99,900,1000,1101,1055,1040,1070,1150,1175,1250,1275,1340,1355,1370,2020,3070,3101,3125,3150,4120,4240,4340,5030,5060,6080,6190,6230,7210,7229,7250,7280,8090,8180,8200,9050,9110,25601,150,500,610,700,900,100,1101,1201,1301,1400,1470,1480,1500,1600,1700,1800,1900,1910,1920,2000,2101,2201,2301,2400,2500,2600,2700,2800,2900,3000,3200,3300,3400,3500,3600,3700,3800,4000,4100,4300,4400,4500,4600,4700,4800,4900,5100,5200,5300,5400,5600,5800,5900,6001,29111',
  'NodeDesc': 'All Courts',
  'SearchBy': '0',
  'CaseSearchMode': 'CaseNumber',
  'CaseSearchValue': 'T-4-CV-20200051*',
  'CitationSearchValue': '',
  'CourtCaseSearchValue': '',
  'PartySearchMode': 'Name',
  'AttorneySearchMode': 'Name',
  'LastName': '',
  'FirstName': '',
  'cboState': 'AA',
  'MiddleName': '',
  'DateOfBirth': '',
  'DriverLicNum': '',
  'CaseStatusType': '0',
  'DateFiledOnAfter': '03/15/2020',
 # 'DateFiledOnBefore': '03/20/2020',
  'chkCriminal': 'on',
  'chkFamily': 'on',
  'chkCivil': 'on',
  'chkProbate': 'on',
  'chkDtRangeCriminal': 'on',
  'chkDtRangeFamily': 'on',
  'chkDtRangeCivil': 'on',
  'chkDtRangeProbate': 'on',
  'chkCriminalMagist': 'on',
  'chkFamilyMagist': 'on',
  'chkCivilMagist': 'on',
  'chkProbateMagist': 'on',
  'DateSettingOnAfter': '',
  'DateSettingOnBefore': '',
  'SortBy': 'fileddate',
  'SearchSubmit': 'Search',
  'SearchType': 'CASE',
  'SearchMode': 'CASENUMBER',
  'NameTypeKy': '',
  'BaseConnKy': '',
  'StatusType': 'true',
  'ShowInactive': '',
  'AllStatusTypes': 'true',
  'CaseCategories': '',
  'RequireFirstName': '',
  'CaseTypeIDs': '',
  'HearingTypeIDs': '',
  'SearchParams': 'SearchBy~~Search By:~~Case~~Case||CaseNumberOption~~Case Search Mode:~~CaseNumber~~Number||CaseSearchValue~~Case Number:~~T-4-CV-20200*~~T-4-CV-20200*||AllOption~~All~~0~~All||DateFiledOnAfter~~Date Filed On or After:~~03/19/2020~~03/19/2020||DateFiledOnBefore~~Date Filed On or Before:~~03/20/2020~~03/20/2020||selectSortBy~~Sort By:~~Filed Date~~Filed Date'
}




#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~
#Individual URL results







headers4 = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/Search.aspx?ID=100',
    'Accept-Language': 'en-US,en;q=0.9',
}



# Use 'with' to ensure the session context is closed after use.

with  HTMLSession() as s:
    #1. Login
    #postResult = s.post(LOGIN_URL, data=data, cookies=cookies)
    postResult = s.post(LOGIN_URL, data=data)
     
    #1.5 Select county (Bernalillo)
    AreaPostResult = s.post('https://securecourtcaseaccess.nmcourts.gov/Search.aspx', headers=headersArea, params=paramsArea,  data=DataAreaAll)
   
    #2. Search Site based on #
    #MAX T-4-CV-2020-011194
    #for i in range(45,120): #values may change later 50-97 all the data we want
    
    baseSearch="T-4-CV-2020-"
    for i in range(0,350): #values may change later 50-97 all the data we want
        
        print("Selection range: "+str(i))
        
        if (len(str(i)) ==1): 
            searchTerm = baseSearch + '000' + str(i) + '*'
        elif (len(str(i)) == 2):
            searchTerm = baseSearch + '00' + str(i) + '*'
        elif (len(str(i)) == 3):
            searchTerm = baseSearch + '0' + str(i) + '*'
    
        print(searchTerm)
        
        data['CaseSearchValue'] = searchTerm
        CGRSearch= s.post('https://securecourtcaseaccess.nmcourts.gov/Search.aspx', headers=headersSearch, params=paramsSearch,  data=data)
        
        if ('Login' in CGRSearch.url):
            print("Error in "+str(CGRSearch.url))
            sys.exit()
        
        #3. Parse Site for CaseID's and Tenants
        caseIDs=[]
        p = bs(CGRSearch.text, 'lxml')
        table = p.find_all('table')
        courtData=table[5].find_all('tr')
        for i in range(3,len(courtData)):
            if 'Landlord' in str(courtData[i]):
                tempString=bs(str(courtData[i]), 'lxml')
                caseIDs.append(str(tempString.find_all('a')[0])[32:39])
            elif 'Forcible' in str(courtData[i]):
                 tempString=bs(str(courtData[i]), 'lxml')
                 caseIDs.append(str(tempString.find_all('a')[0])[32:39])
            elif 'Mobile Home' in str(courtData[i]):
                 tempString=bs(str(courtData[i]), 'lxml')
                 caseIDs.append(str(tempString.find_all('a')[0])[32:39])
            elif 'Interpleader' in str(courtData[i]):
                 tempString=bs(str(courtData[i]), 'lxml')
                 caseIDs.append(str(tempString.find_all('a')[0])[32:39])
            
    

        print(caseIDs)
        #4. get CaseResult
        for i in caseIDs:
             paramsCase = (('CaseID', str(i)),)
             caseGetResults = s.get('https://securecourtcaseaccess.nmcourts.gov/CaseDetail.aspx', headers=headers4, params=paramsCase)
            
             if ('error' in caseGetResults.url):
                 print(str(i) + ": "+str(caseGetResults.url))
                 sys.exit()
                 
                #5. Save
             #print(caseGetResults.url)
             f = open(str(i), 'wb')
             f.write(caseGetResults.content)
             f.close()
             
          
 
  
   
