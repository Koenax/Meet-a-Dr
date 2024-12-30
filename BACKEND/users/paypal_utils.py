from django.db import models
from django.contrib.auth.models import User
import paypalrestsdk
from paypalrestsdk import Payment as PayPalPayment

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": "your-paypal-client-id",
    "client_secret": "your-paypal-client-secret"
})

def create_paypal_payment(amount, currency="USD"):
    """
    Creates a PayPal payment object.

    Args:
        amount (float): The payment amount.
        currency (str): The currency code (default is "USD").

    Returns:
        PayPalPayment: The PayPal payment object if created successfully.
        None: If payment creation fails.
    """
    payment = PayPalPayment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [{
            "amount": {
                "total": str(amount),
                "currency": currency
            },
            "description": "Payment for appointment"
        }],
        "redirect_urls": {
            "return_url": "https://your-domain.com/payment-success",
            "cancel_url": "https://your-domain.com/payment-cancel"
        }
    })

    if payment.create():
        return payment
    else:
        print(f"Error creating PayPal payment: {payment.error}")
        return None
