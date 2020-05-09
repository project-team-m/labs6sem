from pycbrf.toolbox import ExchangeRates
from datetime import datetime, timedelta

if __name__ == "__main__":
    mass = []
    dates = []
    for i in range(90):
        #rates = ExchangeRates(str((datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d")))
        if not i % 10:
            dates.append(str((datetime.today() - timedelta(days=i)).strftime("%d-%m")))
        #mass.append(float(str(rates["EUR"].value)))
    #print(list(reversed(mass)))
    print(list(reversed(dates)))
