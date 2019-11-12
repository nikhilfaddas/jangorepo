from flask import Flask,render_template,request
from onlinestore.ConsumerController import *
capp = Flask(__name__)

def dummy_cust():
    return Book(cid=0,cnm='',cag=0,csal=0.0,cadr='',cpan='',cdes='')


@capp.route("/consumer/welcome/",methods=["GET"])
def welcome_consumer():
    return render_template('customer.html',cust=dummy_cust(),customers=get_customers())

@capp.route("/consumer/save/",methods=["POST"])
def customer_save_info():
    customer =Cust(cid=request.form['id'],               # request.form---convert ui lang to python lang.
         cnm=request.form['name'],
         cag=request.form['age'],
         csal=request.form['salary'],
         cadr=request.form['address'],
         cpan=request.form['pancard'],
         cdes=request.form['position'],)

    status = add_customers(customer)
    return render_template('customer.html', cust=dummy_cust(),msg=status,customers=get_customers())


if __name__ == '__main__':
    capp.run(debug=True,port=5001)