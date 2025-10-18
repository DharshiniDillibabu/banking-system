from flask import Flask, render_template, request

app = Flask(__name__)

balance = 5000
pin = "1234"

@app.route("/", methods=["GET", "POST"])
def home():
    global balance
    message = ""
    if request.method == "POST":
        user_pin = request.form.get("pin")
        action = request.form.get("action")
        amount = request.form.get("amount")

        if user_pin != pin:
            message = "❌ Incorrect PIN"
        else:
            if action == "deposit":
                try:
                    amt = float(amount)
                    if amt > 0:
                        balance += amt
                        message = f"✅ Deposited ${amt}. Current Balance: ${balance}"
                    else:
                        message = "⚠️ Enter a positive amount"
                except:
                    message = "⚠️ Invalid input"
            
            elif action == "withdraw":
                try:
                    amt = float(amount)
                    if 0 < amt <= balance:
                        balance -= amt
                        message = f"✅ Withdrawn ${amt}. Current Balance: ${balance}"
                    else:
                        message = "⚠️ Invalid amount or insufficient balance"
                except:
                    message = "⚠️ Invalid input"

            elif action == "check":
                message = f"💰 Current Balance: ${balance}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)


