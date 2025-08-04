
# CURRENCY CONVERTER PROJECT 5





import requests

class currency():
    def info(self):
        optionS={"USD","INR","EUR","GBP","JPY","CAD","AUD"}  
        print(optionS)
        initial_cur=input("enter the initial currency from above:").upper()
        if initial_cur not in optionS or len(initial_cur)!=3 :  
            print("invalid curreny")
        else:
            print("input saved")
        final_cur=input("enter final currency:").upper()
        if final_cur not in optionS or len(final_cur)!=3 : 
            print("invalid curreny")
        else:
            print("input saved")
        amount=(input("enter the amount you want to convert:"))
        if amount.isdigit() and int(amount)>0:  
            amount=int(amount)
            print("input saved")
        else:
            print("enter valid number")
 
  
        url = "https://api.exchangerate-api.com/v4/latest/" + initial_cur


        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'rates' in data and final_cur in data['rates']:
                rate = data['rates'][final_cur]
                result = amount * rate
                print(f"{amount} {initial_cur} is equal to {result} {final_cur}")
            else:
                print("Error in conversion: Currency not found")
        else:
            print("Failed to retrieve data:", response.status_code)
    def run(self):
        print("CURRENCY CONVERTER")
        self.info()


i = currency()
i.run()