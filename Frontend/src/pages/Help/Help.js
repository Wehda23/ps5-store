import React from 'react';

const Help = () => {
  return (
    <div style={{ fontFamily: 'Arial, sans-serif', lineHeight: '1.6', color: '#333', padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h1 style={{ color: '#0056b3', borderBottom: '2px solid #0056b3', paddingBottom: '10px' }}>Help & Support</h1>

      <h2 style={{ color: '#007bff', marginTop: '30px' }}>Welcome to the PlayStation 5 E-commerce Help Section</h2>
      <p>We're here to assist you with any questions or issues you may have. Below, you will find answers to common questions and ways to contact our support team.</p>

      <h3 style={{ color: '#007bff', marginTop: '30px' }}>Frequently Asked Questions (FAQs)</h3>

      <h4 style={{ color: '#0056b3' }}>1. How do I create an account?</h4>
      <p>To create an account, click on the 'Sign Up' button at the top right corner of the page and fill in the required information. You will receive a confirmation email to activate your account.</p>

      <h4 style={{ color: '#0056b3' }}>2. How can I reset my password?</h4>
      <p>If you've forgotten your password, click on the 'Forgot Password' link on the login page. Enter your email address, and we'll send you instructions to reset your password.</p>

      <h4 style={{ color: '#0056b3' }}>3. What payment methods are accepted?</h4>
      <p>We accept various payment methods including credit/debit cards, PayPal, and other online payment gateways. You can select your preferred payment method at checkout.</p>

      <h4 style={{ color: '#0056b3' }}>4. How do I track my order?</h4>
      <p>Once your order is shipped, you will receive a tracking number via email. You can use this number to track your order on our website or the courier's website.</p>

      <h4 style={{ color: '#0056b3' }}>5. What is the return policy?</h4>
      <p>If you are not satisfied with your purchase, you can return the product within 30 days of delivery for a full refund. The product must be in its original condition and packaging. Please visit our <a href="/return-policy" style={{ color: '#007bff' }}>Return Policy</a> page for more details.</p>

      <h4 style={{ color: '#0056b3' }}>6. How can I contact customer support?</h4>
      <p>If you need further assistance, you can contact our customer support team through the following methods:</p>
      <ul>
        <li>Email: <a href="mailto:support@playstation5ecommerce.com" style={{ color: '#007bff' }}>support@playstation5ecommerce.com</a></li>
        <li>Phone: 1-800-123-4567</li>
        <li>Live Chat: Available on our website from 9 AM to 6 PM EST</li>
      </ul>

      <h3 style={{ color: '#007bff', marginTop: '30px' }}>Shipping Information</h3>
      <p>We offer various shipping options to meet your needs. Standard shipping typically takes 5-7 business days, while express shipping options are also available at an additional cost. For more details, please visit our <a href="/shipping-info" style={{ color: '#007bff' }}>Shipping Information</a> page.</p>

      <h3 style={{ color: '#007bff', marginTop: '30px' }}>Warranty and Repairs</h3>
      <p>All PlayStation 5 consoles come with a one-year warranty. If you encounter any issues with your console, please contact our support team for troubleshooting and repair options. For more details, visit our <a href="/warranty-info" style={{ color: '#007bff' }}>Warranty Information</a> page.</p>

      <h3 style={{ color: '#007bff', marginTop: '30px' }}>Community and Support Forums</h3>
      <p>Join our community to connect with other PlayStation 5 users, share tips, and get support from fellow gamers. Visit our <a href="/community-forums" style={{ color: '#007bff' }}>Community Forums</a> to get started.</p>

      <p>Thank you for choosing PlayStation 5 E-commerce. We are committed to providing you with the best possible service and support.</p>
    </div>
  );
};

export default Help;
