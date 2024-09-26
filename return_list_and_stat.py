from lastwill.contracts.submodels.common import Contract
import datetime

def return_li(year,month,day):
    mainnet_list = [
        'ETHEREUM_MAINNET',
        'NEO_MAINNET', 'EOS_MAINNET','BTC_MAINNET',
        'TRON_MAINNET','WAVES_MAINNET','BINANCE_MAINNET'
    ]
    state_list = ['WAITING_ACTIVATION','WAITING_FOR_DEPLOYMENT',
        'WAITING_FOR_PAYMENT','CREATED','POSTPONED', ]
    values = Contract.objects.all()
    dates = values.filter(created_date__gte=datetime.date(year,month,day)).filter(network__name__in = mainnet_list)
    var = dates.exclude(state__in = state_list)
    print(var.values_list().order_by("contract_type")
          
          
          
          
from lastwill.contracts.models import Contracts
import datetime

mainnet_list = [
        'ETHEREUM_MAINNET',
        'NEO_MAINNET', 'EOS_MAINNET','BTC_MAINNET',
        'TRON_MAINNET','WAVES_MAINNET','BINANCE_MAINNET'
    ]
state_list = ['WAITING_ACTIVATION','WAITING_FOR_DEPLOYMENT',
        'WAITING_FOR_PAYMENT','CREATED','POSTPONED', ]

def find_contracts(day,mon,year):
    for i in mainnet_list:
        m = values.filter(created_date__gte=datetime.date(2019,7,4)).filter(network__name__in = mainnet_list).filter(network__name__in= [i])
        print(str(i)+' '+str(len(m)))




if __main__ == "__name__":
    day = input('day')
    mon = input('mon')
    year = input('year')
    find_contracts(day,mon,year)


