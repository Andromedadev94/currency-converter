import requests
try:
    response = requests.get("https://api.frankfurter.app/latest?from=USD", timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException:
    print("Network error")
data= response.json()
data['base'] = 1.0
data['rates']['USD']=1
data['rates']['IRR']=155000
data['rates']['GOLD']=32258
rates=data["rates"]
data_list=list(rates.keys())
print("Currency Converter (type 'exit' anytime to quit), \nAvailable currencies:")
max_per_line=10
for jump in range(0,len(data_list),10):
    x=data_list[jump:jump+max_per_line]
    print(" ".join(x))
while True:
    while True:
        amount=input("How much money?: ")
        if amount.lower()=="exit":
            print("Program exited.")
            exit()
        try:
            amount=float(amount)
            if amount<=0:
                print("Amount must be greater than 0!\n")
                continue
            break
        except ValueError:
            print("Must enter in numbers!\n")
    while True:
        currency=input("what currency?(usd, try, irr, etc): ")
        if currency.lower()=="exit":
            print("Program exited.")
            exit()
        currency=currency.upper()
        if currency not in data['rates']:
            print("Currency does not exist! ")
            continue
        break
    while True:
        target_currency=input("convert to?(usd, try, irr, etc): ")
        if target_currency=="exit":
            print("Program exited.")
            exit()
        target_currency=target_currency.upper()
        if target_currency not in data['rates']:
            print("Currency does not exist! ")
            continue
        break
    try:
        result=amount/rates[currency]*rates[target_currency]
        print(f"{amount} {currency} = {round(result, 4)} {target_currency}\n")
    except Exception:
        print("unexpected error!")


