import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Help = () => {
  return (
    <div className="container my-5">
      <h1 className="text-primary border-bottom pb-2 mb-4">Help & Support</h1>

      <h2 className="text-info mt-5">Welcome to the PlayStation 5 E-commerce Help Section</h2>
      <p>We're here to assist you with any questions or issues you may have. Below, you will find answers to common questions and ways to contact our support team.</p>

      <h3 className="text-info mt-5">Frequently Asked Questions (FAQs)</h3>

      <h4 className="text-primary mt-4">1. How do I create an account?</h4>
      <p>To create an account, click on the 'Sign Up' button at the top right corner of the page and fill in the required information. You will receive a confirmation email to activate your account.</p>

      <h4 className="text-primary mt-4">2. How can I reset my password?</h4>
      <p>If you've forgotten your password, click on the 'Forgot Password' link on the login page. Enter your email address, and we'll send you instructions to reset your password.</p>

      <h4 className="text-primary mt-4">3. What payment methods are accepted?</h4>
      <p>We accept various payment methods including credit/debit cards, PayPal, and other online payment gateways. You can select your preferred payment method at checkout.</p>

      <h4 className="text-primary mt-4">4. How do I track my order?</h4>
      <p>Once your order is shipped, you will receive a tracking number via email. You can use this number to track your order on our website or the courier's website.</p>

      <h4 className="text-primary mt-4">5. What is the return policy?</h4>
      <p>If you are not satisfied with your purchase, you can return the product within 30 days of delivery for a full refund. The product must be in its original condition and packaging. Please visit our <a href="/community-forums" className="text-info">Return Policy</a> page for more details.</p>

      <h4 className="text-primary mt-4">6. How can I contact customer support?</h4>
      <p>If you need further assistance, you can contact our customer support team through the following methods:</p>
      <ul>
        <li>Email: <a href="mailto:support@playstation5ecommerce.com" className="text-info">support@playstation5ecommerce.com</a></li>
        <li>Phone: 1-800-123-4567</li>
        <li>Live Chat: Available on our website from 9 AM to 6 PM EST</li>
      </ul>

      <h3 className="text-info mt-5">Shipping Information</h3>
      <p>We offer various shipping options to meet your needs. Standard shipping typically takes 5-7 business days, while express shipping options are also available at an additional cost. For more details, please visit our <a href="/shipping-info" className="text-info">Shipping Information</a> page.</p>

      <h3 className="text-info mt-5">Warranty and Repairs</h3>
      <p>All PlayStation 5 consoles come with a one-year warranty. If you encounter any issues with your console, please contact our support team for troubleshooting and repair options. For more details, visit our <a href="/warranty-info" className="text-info">Warranty Information</a> page.</p>

      <h3 className="text-info mt-5">Community and Support Forums</h3>
      <p>Join our community to connect with other PlayStation 5 users, share tips, and get support from fellow gamers. Visit our <a href="/community-forums" className="text-info">Community Forums</a> to get started.</p>

      <p>Thank you for choosing PlayStation 5 E-commerce. We are committed to providing you with the best possible service and support.</p>
    </div>
  );
};

export default Help;
