import os
import json
import pandas as pd
import stripe
import uuid
from flask import Flask, jsonify, request, render_template, session
from utils import predict_approval
import datetime
import config
from flask_cors import CORS
import sys
sys.path.append('../pipelines/')
from etl.config import COURSE_NAMES
from models.config import FEATURES

#app = Flask(__name__, template_folder='template', static_folder='template/assets')
app = Flask(__name__)
# Set a secret key for the application
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
CORS(app)

USER_LINKS_FILE = "user_links.json"

# Load existing user links from the JSON file
try:
    with open(f"app/{USER_LINKS_FILE}", "r") as file:
        user_links = json.load(file)
except FileNotFoundError:
    user_links = {}

print(f"user_links: {user_links}")

stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
    "endpoint_secret": os.environ["STRIPE_ENDPOINT_SECRET"], # new
}

stripe.api_key = stripe_keys["secret_key"]

#df_scores = pd.read_parquet('../data/processed/scores_approvals_convocation_2020_2022.parquet')
#df_scores = df_scores[config.RESULTS_INFO]

# @app.route('/filter', methods=['GET']) 
# def filter_dataframe():
#     numero_inscricao = request.args.get('numero_inscricao')  # Get 'name' parameter from the request

#     if numero_inscricao:
#         filtered_df = df_scores[df_scores['numero_inscricao'] == numero_inscricao]  # Filter DataFrame based on 'name'
#         result = filtered_df.to_dict('records')
#     else:
#         result = df_scores.to_dict('records')  # Return the entire DataFrame if 'name' parameter is not provided

#     return jsonify(result)

# @app.route('/form')
# def form_page():
#     data = {
#         'features': FEATURES,
#         'course_names' : COURSE_NAMES
#     }
#     return render_template('formpage.html', data=data)


def save_user_links_to_file():
    # Save user_links to the JSON file
    with open(f"app/{USER_LINKS_FILE}", "w") as file:
        json.dump(user_links, file)


@app.route('/result')
def result():
    data = {
        'escore_bruto_p1_etapa1': float(request.args.get('escore_bruto_p1_etapa1')),
        'escore_bruto_p2_etapa1': float(request.args.get('escore_bruto_p2_etapa1')),
        'escore_bruto_p1_etapa2': float(request.args.get('escore_bruto_p1_etapa2')),
        'escore_bruto_p2_etapa2': float(request.args.get('escore_bruto_p2_etapa2')),
        'escore_bruto_p1_etapa3': float(request.args.get('escore_bruto_p1_etapa3')),
        'escore_bruto_p2_etapa3': float(request.args.get('escore_bruto_p2_etapa3')),
        'cotas_negros_flag': int(request.args.get('cotas_negros_flag')),
        'publicas1_flag': int(request.args.get('publicas1_flag')),
        'publicas2_flag': int(request.args.get('publicas2_flag')),
        'publicas3_flag': int(request.args.get('publicas3_flag')),
        'publicas4_flag': int(request.args.get('publicas4_flag')),
        'publicas5_flag': int(request.args.get('publicas5_flag')),
        'publicas6_flag': int(request.args.get('publicas6_flag')),
        'publicas7_flag': int(request.args.get('publicas7_flag')),
        'publicas8_flag': int(request.args.get('publicas8_flag')),
        'course': request.args.get('course'),
    }

    approval_prediction = predict_approval(data)

    result_data = {
        'approval_prediction': approval_prediction
    }
    
    # Access the data from the session
    received_data = session.get('data', {})

    print(f"received_data: {received_data}")
    print(f"request.args: {request.args}")

    return render_template('resultpage.html', data=result_data, received_data=received_data)

# @app.post('/predict') 
# def predict():
    
#     # this is a python dictionary 
#     data = request.json
           
#     approval_prediction = predict_approval(data)
        
#     try:
#         result = jsonify({'metadata': {"timestamp": str(datetime.datetime.now())},
#                           'prediction': {"probability": approval_prediction}})
    
#     except TypeError as e:
#         return jsonify({'error': str(e)})
        
#     return result


@app.route("/hello")
def hello_world():
    return jsonify("hello, world!")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/config")
def get_publishable_key():
    """
    Now, after the page load, a call will be made to /config, which will
    respond with the Stripe publishable key. We'll then use this key to 
    create a new instance of Stripe.js.
    """
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)


@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            #client_reference_id=current_user.id if current_user.is_authenticated else None,
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price": "price_1OTwBXD1X8yObih9MXQpufKP",
                    #"name": "T-shirt",
                    "quantity": 1,
                    #"currency": "usd",
                    #"amount": "2000",
                    
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")


@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        print(f"event:\n{event}")

        # TODO: run some custom code here
        event_id = event["id"]
        checkout_session_id = event["data"]["object"]["id"]
        email = event["data"]["object"]["customer_details"]["email"]
       
        # Store the link in the database
        user_links[email] = {
            "event_id": event_id,
            "checkout_session_id": checkout_session_id,
            "user_identifier": str(uuid.uuid4())
        }
        # Store the link in the JSON file
        save_user_links_to_file()

    return "Success", 200


#@app.route("/confirmation/<event_id>/<email>")
@app.route("/confirmation/<user_identifier>")
def confirmation_page(user_identifier):
#def confirmation_page(event_id, email):
    
    # user_identifier comes from parameter function
    print(f"user_identifier: {user_identifier}")



    print(f"user_links: {user_links}")
    
    
    # Ensure the user_id is valid (you might want to add more checks)
    user_identifiers = [user_links[key]["user_identifier"] for key in user_links]
    print(user_identifiers)
    if user_identifier not in user_identifiers:
        return "Invalid user ID or payment not registered", 404

    data = {
        'features': FEATURES,
        'course_names' : COURSE_NAMES
    }

    # Store the data in the session
    session['data'] = user_identifier
    
    # Perform any additional actions or render a confirmation page
    # In this example, we'll just render a simple template
    #return render_template("confirmation_page.html", email=email, event_id=event_id, unique_link=unique_link)
    return render_template("formpage.html", email=user_identifier, data=data)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)