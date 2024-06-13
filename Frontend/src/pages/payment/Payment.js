import React from "react";
import { Link } from "react-router-dom";
import Breadcrumbs from "../../components/pageProps/Breadcrumbs";

const Payment = () => {
  return (
    <div className="max-w-container mx-auto px-4 py-10">
      <Breadcrumbs title="Payment Gateway" />
      <div className="pb-10">
        <h1 className="text-3xl font-bold mb-6">Payment Gateway for PlayStation 5 E-commerce</h1>
        <p className="text-lg mb-4">
          Our payment gateway is designed to provide a seamless and secure payment experience for purchasing PlayStation 5 and accessories. Below you will find detailed information about the features and benefits of using our payment gateway.
        </p>
        
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-3">Overview</h2>
          <p className="text-lg">
            The payment gateway integrates with multiple payment processors to offer flexibility and security. It supports various payment methods including credit/debit cards, PayPal, and more.
          </p>
        </section>

        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-3">Supported Payment Methods</h2>
          <ul className="list-disc list-inside text-lg">
            <li>Visa, MasterCard, American Express</li>
            <li>PayPal</li>
            <li>Apple Pay</li>
            <li>Google Pay</li>
            <li>Bank Transfers</li>
          </ul>
        </section>

        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-3">Security Features</h2>
          <p className="text-lg">
            Our payment gateway is PCI-DSS compliant and employs advanced security measures such as encryption and tokenization to protect sensitive information. Additionally, it includes fraud detection and prevention mechanisms.
          </p>
        </section>

        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-3">Steps for Processing a Payment</h2>
          <ol className="list-decimal list-inside text-lg">
            <li>Select your products and add them to your cart.</li>
            <li>Proceed to checkout and enter your shipping information.</li>
            <li>Choose your preferred payment method.</li>
            <li>Enter your payment details securely.</li>
            <li>Review your order and confirm the payment.</li>
            <li>Receive a confirmation email with your order details.</li>
          </ol>
        </section>

        <Link to="/">
          <button className="w-52 h-10 bg-primeColor text-white text-lg mt-4 hover:bg-black duration-300">
            Explore More
          </button>
        </Link>
      </div>
    </div>
  );
};

export default Payment;
