from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from base64 import b64encode
import json
#  {
#     "BusinessShortCode": 174379,
#     "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIxMDI1MTQxODMx",
#     "Timestamp": "20221025141831",
#     "TransactionType": "CustomerPayBillOnline",
#     "Amount": 1,
#     "PartyA": 254708374149,
#     "PartyB": 174379,
#     "PhoneNumber": 254790908351,
#     "CallBackURL": "https://mydomain.com/path",
#     "AccountReference": "CompanyXLTD",
#     "TransactionDesc": "Payment of X" 
#   }
# Consumer Key: 0d4NxJG3vD9XhyohIjy1W1fGy1GrbFq1
# Consumer Secret: CAsSee79oznXbkyo
def authenticate():
    consumer_key="0d4NxJG3vD9XhyohIjy1W1fGy1GrbFq1"
    consumer_secret="CAsSee79oznXbkyo"
    """
    :return: MPESA_TOKEN
    """
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    print(r.text)
    return r.text


def stk_push(token, business_shortcode, lipa_na_mpesapasskey, amount, party_a, phonenumber, callbackurl):
    # sandbox_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % token}
    timestamp = datetime.now().strftime("%Y%m%d%I%M%S")
    pswd = (business_shortcode + lipa_na_mpesapasskey + timestamp).encode("utf-8")
    password = b64encode(pswd).decode()
    req = {
        "BusinessShortCode": "174379",
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": party_a,
        "PartyB": business_shortcode,
        "PhoneNumber": phonenumber,
        "CallBackURL": callbackurl,
        "AccountReference": business_shortcode,
        "TransactionDesc": "REG",
    }
    print(req)
    response = requests.post(api_url, json=req, headers=headers)

    print(response.text)
    return response

def pay(phone_number,amount):
    callback_url="https://9886-154-153-230-79.in.ngrok.io /payment/callback/"
    token_data = authenticate()
    try:
        token = json.loads(token_data)["access_token"]
    except Exception:
        token = ""
    business_shortcode = "174379"
    lipa_na_mpesapasskey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    party_b = business_shortcode
    resp=stk_push(token, business_shortcode, lipa_na_mpesapasskey, amount, party_b, phone_number, callback_url)
    return resp.text