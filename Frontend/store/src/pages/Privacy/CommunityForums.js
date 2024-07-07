import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const CommunityForums = () => {
  return (
    <div className="container my-5">
      <h1 className="text-primary border-bottom pb-2 mb-4">Community Forums</h1>

      <p>Welcome to the PlayStation 5 E-commerce Community Forums! Connect with fellow gamers, share tips, and get support from the community. Our forums are a great place to discuss everything related to PlayStation 5.</p>

      <h3 className="text-info mt-5">Popular Topics</h3>
      <ul>
        <li>General Discussion</li>
        <li>Game Tips and Tricks</li>
        <li>Technical Support</li>
        <li>Off-Topic</li>
      </ul>

      <h3 className="text-info mt-5">Forum Rules</h3>
      <p>To ensure a positive experience for everyone, please adhere to the following rules:</p>
      <ul>
        <li>Be respectful to other members.</li>
        <li>No spamming or advertising.</li>
        <li>Keep discussions on-topic.</li>
        <li>Report any inappropriate content to moderators.</li>
      </ul>

      <h3 className="text-info mt-5">Join the Discussion</h3>
      <p>Sign in to participate in the forums. If you don't have an account, <a href="/signup" className="text-info">sign up here</a>.</p>

      <p>Thank you for being a part of our community. Happy gaming!</p>
    </div>
  );
};

export default CommunityForums;
