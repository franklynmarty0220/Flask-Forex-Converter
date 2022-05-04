from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from decimal import Decimal
from converter import Currency

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] ="BlingBling"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] =False

debug = DebugToolbarExtension(app)


@app.route('/root')
def form():
    """Renders page to contain form for the forex converter"""

    return render_template('root.html')


@app.route('/results', methods=['GET', 'POST'])
def calculate():

    init = request.form.get('init')
    final = request.form.get('final')
    amnt= request.form.get('amount')

    

    amount = Decimal(amnt)

    curr = Currency(init)

    new_curr = Currency(final)

    try:
        amount
    except:
        alert_amt = "Please enter a valid number for the amount"
        flash(alert_amt)
        return redirect('/root')

    try:
        curr
    except:
        alert_curr = "Please enter a valid currency"
        flash(alert_curr)
        return redirect('/root')

    try:
        new_curr
    except:
        alert_new = "Please resubmit"
        flash(new_curr)
        return redirect('/root')
    
    try:
        converse = curr.convert_amount(init,final,amount)
        converted_value = round(converse, 2)
        converted_sym = curr.currency_symbol(final)
    except:
        alert_converter="Error! Please check your values and try again!"
        flash(alert_converter)
        return redirect('/root')

    return render_template('results.html', conv=converted_value, sym=converted_sym)