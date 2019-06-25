from lastwill.contracts.submodels.common import Contract
import datetime

def return_li(year,month,day):
    mainnet_list = [
        'ETHEREUM_MAINNET',
        'NEO_MAINNET',
        'EOS_MAINNET',
        'BTC_MAINNET',
        'TRON_MAINNET',
        'WAVES_MAINNET',
        'BINANCE_MAINNET'
    ]
    state_list = [
        'WAITING_ACTIVATION',
        'WAITING_FOR_DEPLOYMENT',
        'WAITING_FOR_PAYMENT',
        'CREATED',
        'POSTPONED',
    ]

    values = Contract.objects.all()
    dates = values.filter(created_date__gte=datetime.date(year,month,day))
    for mainnet in mainnet_list:
        network = for dates.filter(network.name = mainnet)
    for state in state_list:
        states = network.exclude(state=state )
    print(values = states.filter.all().group_by('contract_type'))
