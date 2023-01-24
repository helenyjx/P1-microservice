from flask import Flask
from flask import jsonify
app = Flask(__name__)

def change(amount):
    # Compute the resultant change and then store it to the result (res)
    res = []
    coins = [1,5,10,25] # It represents value of pennies, nickels, dimes, and quarters
    coin_lookup = {25: "Quarters", 10: "Dimes", 5: "Nickels", 1: "Pennies"}

    # Divide the amount (in cents) *100 by a coin value
    # Record the quantity of evenly divided coins and remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # Append the coin kinds and the total quantity of coins with no remaining value
    res.append({num:coin_lookup[coin]})

    # If there is still some remainder, keep adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res

@app.route('/')
def hello():
    print("I am an Automatic Change Machine")
    return 'Hello Automatic Change Machine! Please use it to make change at route by typing: /change/x/y (x is dollar and y is cents)'

@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)
    
@app.route('/100/change/<dollar>/<cents>')
def change100route(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    amount100 = float(amount) * 100
    print(f"This is the {amount} X 100")
    result = change(amount100)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
