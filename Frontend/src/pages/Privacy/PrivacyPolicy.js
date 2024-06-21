import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const PrivacyPolicy = () => {
  return (
    <div className="container my-5">
      <h1 className="text-primary border-bottom pb-2 mb-4">Privacy Policy</h1>

      <p>At PlayStation 5 E-commerce, we are committed to protecting your privacy. This Privacy Policy outlines the types of information we collect, how we use it, and how we protect it.</p>

      <h3 className="text-info mt-5">Information We Collect</h3>
      <ul>
        <li>Personal Information: Name, email address, phone number, etc.</li>
        <li>Payment Information: Credit/debit card details, billing address, etc.</li>
        <li>Usage Data: Pages visited, time spent on the site, etc.</li>
      </ul>

      <h3 className="text-info mt-5">How We Use Your Information</h3>
      <p>We use your information to:</p>
      <ul>
        <li>Process and fulfill your orders.</li>
        <li>Provide customer support.</li>
        <li>Improve our website and services.</li>
        <li>Send promotional emails (you can opt-out at any time).</li>
      </ul>

      <h3 className="text-info mt-5">Data Security</h3>
      <p>We implement a variety of security measures to maintain the safety of your personal information. Your data is stored in secure networks and is only accessible by a limited number of persons who have special access rights to such systems.</p>

      <h3 className="text-info mt-5">Third-Party Disclosure</h3>
      <p>We do not sell, trade, or otherwise transfer to outside parties your Personally Identifiable Information unless we provide users with advance notice. This does not include website hosting partners and other parties who assist us in operating our website, conducting our business, or serving our users, so long as those parties agree to keep this information confidential.</p>

      <h3 className="text-info mt-5">Contact Us</h3>
      <p>If you have any questions regarding this privacy policy, you may contact us using the information below:</p>
      <ul>
        <li>Email: <a href="mailto:privacy@playstation5ecommerce.com" className="text-info">privacy@playstation5ecommerce.com</a></li>
        <li>Phone: 1-800-123-4567</li>
      </ul>

      <p>Thank you for trusting PlayStation 5 E-commerce with your information. We are committed to protecting your privacy.</p>
    </div>
  );
};

export default PrivacyPolicy;
