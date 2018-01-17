#!/usr/bin/python
# -*- coding: utf-8 -*-

from string import Template
import os
import random
import re


def zfill_number(number, width=8):
    """"把数字转换成固定长度. 比如18，转换成8位的：00000018"""
    num_str = str(number)
    return num_str.zfill(width) 


the_date = "20180108"
deal_item_lines = ["201801030000000000237922201801041560000000000000000000000000000000002153202018010314344003160106A00000108 379 00000000000000000000000001300000122 3790000000893 110000 20180104000000000000000000000000000379 0000000000 0000000000000000000000000000000000000000000 20180103 00000000000000000000000000000000000000000000000000000000000000000 000000000000000000000000000000000000000000000000000000000000000000000000 0000000000000 0000000000 0106 00 00000 0000000000000000 00000 00000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000 3790000000893 00000000000000000000000000000000000000000000000000000000000000000 00000000000000000000000000000000基金账号不存在 0000000000000000 20180104",
                   "201801030000000000237922201801041560000000000000000000000000000000002153202018010314344003160106A00000108 379 00000000000000000000000001300000122 3790000000893 110000 20180104000000000000000000000000000379 0000000000 0000000000000000000000000000000000000000000 20180103 00000000000000000000000000000000000000000000000000000000000000000 000000000000000000000000000000000000000000000000000000000000000000000000 0000000000000 0000000000 0106 00 00000 0000000000000000 00000 00000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000 3790000000893 00000000000000000000000000000000000000000000000000000000000000000 00000000000000000000000000000000基金账号不存在 0000000000000000 20180104"]
deal_counts_8_bits = zfill_number(len(deal_item_lines))


# template_file = open("template2.txt")
# template_file_content = template_file.read()
# template = Template(template_file_content)

# #直接把template写在本文件里也行，就是会很长 
template = Template("""
OFDCFDAT
20
02
379
${date}
999
04
02
379
116
APPSHEETSERIALNO
TRANSACTIONCFMDATE
CURRENCYTYPE
CONFIRMEDVOL
CONFIRMEDAMOUNT
FUNDCODE
LARGEREDEMPTIONFLAG
TRANSACTIONDATE
TRANSACTIONTIME
RETURNCODE
TRANSACTIONACCOUNTID
DISTRIBUTORCODE
APPLICATIONVOL
APPLICATIONAMOUNT
BUSINESSCODE
TAACCOUNTID
TASERIALNO
BUSINESSFINISHFLAG
DISCOUNTRATEOFCOMMISSION
DEPOSITACCT
REGIONCODE
DOWNLOADDATE
CHARGE
AGENCYFEE
NAV
BRANCHCODE
ORIGINALAPPSHEETNO
ORIGINALSUBSDATE
OTHERFEE1
INDIVIDUALORINSTITUTION
REDEMPTIONDATEINADVANCE
STAMPDUTY
VALIDPERIOD
RATEFEE
TOTALBACKENDLOAD
ORIGINALSERIALNO
SPECIFICATION
DATEOFPERIODICSUBS
TARGETDISTRIBUTORCODE
TARGETBRANCHCODE
TARGETTRANSACTIONACCOUNTID
TARGETREGIONCODE
TRANSFERDIRECTION
DEFDIVIDENDMETHOD
DIVIDENDRATIO
INTEREST
VOLUMEBYINTEREST
INTERESTTAX
TRADINGPRICE
FREEZINGDEADLINE
FROZENCAUSE
TAX
TARGETNAV
TARGETFUNDPRICE
CFMVOLOFTARGETFUND
MINFEE
OTHERFEE2
ORIGINALAPPDATE
TRANSFERFEE
FROMTAFLAG
SHARECLASS
DETAILFLAG
REDEMPTIONINADVANCEFLAG
FROZENMETHOD
ORIGINALCFMDATE
REDEMPTIONREASON
CODEOFTARGETFUND
TOTALTRANSFEE
VARIETYCODEOFPERIODICSUBS
SERIALNOOFPERIODICSUBS
RATIONTYPE
TARGETTAACCOUNTID
TARGETREGISTRARCODE
NETNO
CUSTOMERNO
TARGETSHARETYPE
RATIONPROTOCOLNO
BEGINDATEOFPERIODICSUBS
ENDDATEOFPERIODICSUBS
SENDDAYOFPERIODICSUBS
BROKER
SALESPROMOTION
ACCEPTMETHOD
FORCEREDEMPTIONTYPE
ALTERNATIONDATE
TAKEINCOMEFLAG
PURPOSEOFPESUBS
FREQUENCYOFPESUBS
PERIODSUBTIMEUNIT
BATCHNUMOFPESUBS
CAPITALMODE
DETAILCAPTICALMODE
BACKENLOADDISCOUNT
COMBINENUM
REFUNDAMOUNT
SALEPERCENT
MANAGERREALRATIO
CHANGEFEE
RECUPERATEFEE
ACHIEVEMENTPAY
ACHIEVEMENTCOMPEN
SHARESADJUSTMENTFLAG
GENERALTASERIALNO
UNDISTRIBUTEMONETARYINCOME
UNDISTRIBUTEMONETARYINCOMEFLAG
BREACHFEE
BREACHFEEBACKTOFUND
PUNISHFEE
TRADINGMETHOD
CHANGEAGENCYFEE
RECUPERATEAGENCYFEE
ERRORDETAIL
LARGEBUYFLAG
RAISEINTEREST
FEECALCULATOR
SHAREREGISTERDATE
${deal_counts_8_bits}
${deal_item_lines}
OFDCFEND
""")

trans_template = template.substitute(date=the_date,
                                     deal_counts_8_bits=deal_counts_8_bits,
                                     deal_item_lines='\n'.join(deal_item_lines))
print trans_template
filled_variables = {}

f = open(the_date + "0002.txt", 'w')
f.write(trans_template)
f.close()
