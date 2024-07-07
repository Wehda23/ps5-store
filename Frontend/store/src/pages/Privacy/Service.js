import React from 'react';
import { Link, } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './Service.css';

const Service = () => {
  return (
    <div className="container my-5">
      <h1 className="text-primary mb-4">PS5-Ecommerce: Dive Deeper into the Details</h1>

      <div className="row">
        {/* Massive Selection of PlayStation Games */}
        <div className="col-md-12 mb-4">
          <h2 className="text-info">Massive Selection of PlayStation Games:</h2>
          <div className="card rounded-rectangle">
            <div className="card-body bg-white">
              <h5 className="card-title">New Releases</h5>
              <p className="card-text">Be the first to snag the hottest titles the day they launch. Pre-order upcoming games to secure your copy and avoid disappointment.</p>

              <h5 className="card-title">Pre-Owned Paradise</h5>
              <p className="card-text">Find fantastic deals on previously loved games, allowing you to expand your library without breaking the bank.</p>

              <h5 className="card-title">Classic Corner</h5>
              <p className="card-text">Relive your gaming memories or discover timeless titles with our curated selection of PlayStation classics.</p>

              <h5 className="card-title">Genre Galore</h5>
              <p className="card-text">Filter and browse through a vast library categorized by genre (action, adventure, RPG, etc.) to find your perfect match.</p>
            </div>
          </div>
        </div>

        {/* PlayStation Hardware and Accessories */}
        <div className="col-md-12 mb-4">
          <h2 className="text-info">PlayStation Hardware and Accessories:</h2>
          <div className="card rounded-rectangle">
            <div className="card-body bg-white">
              <h5 className="card-title">Consoles</h5>
              <p className="card-text">Get your hands on the latest PlayStation consoles, including bundles with popular games and controllers.</p>

              <h5 className="card-title">Controllers</h5>
              <p className="card-text">Upgrade your gameplay with a variety of DualShock® controllers, including special edition designs.</p>

              <h5 className="card-title">VR Power</h5>
              <p className="card-text">Immerse yourself in virtual worlds with PlayStation VR headsets and compatible games.</p>

              <h5 className="card-title">Essential Extras</h5>
              <p className="card-text">Find all the accessories you need to enhance your experience, from charging stations to headsets.</p>
            </div>
          </div>
        </div>

        {/* Digital Downloads for Instant Gratification */}
        <div className="col-md-12 mb-4">
          <h2 className="text-info">Digital Downloads for Instant Gratification:</h2>
          <div className="card rounded-rectangle">
            <div className="card-body bg-white">
              <h5 className="card-title">Skip the Wait</h5>
              <p className="card-text">Purchase and download games directly to your PlayStation console, eliminating the need for physical discs.</p>

              <h5 className="card-title">Exclusive Deals</h5>
              <p className="card-text">Look out for special offers and discounts available only on digital downloads.</p>

              <h5 className="card-title">Pre-Load Power</h5>
              <p className="card-text">Pre-load upcoming games and be ready to play the moment they unlock, no waiting required.</p>
            </div>
          </div>
        </div>

        {/* Subscriptions to Unwind and Explore */}
        <div className="col-md-12 mb-4">
          <h2 className="text-info">Subscriptions to Unwind and Explore:</h2>
          <div className="card rounded-rectangle">
            <div className="card-body bg-white">
              <h5 className="card-title">PlayStation Plus</h5>
              <p className="card-text">Access online multiplayer gaming, free monthly games, exclusive discounts, and cloud storage for your game saves.</p>

              <h5 className="card-title">PlayStation Now</h5>
              <p className="card-text">Stream a vast library of PlayStation games directly to your console, perfect for trying new titles or revisiting classics.</p>
            </div>
          </div>
        </div>

        {/* More Than Just Products */}
        <div className="col-md-12 mb-4">
          <h2 className="text-info">More Than Just Products:</h2>
          <div className="card rounded-rectangle">
            <div className="card-body bg-white">
              <h5 className="card-title">Pre-Order and Wishlist</h5>
              <p className="card-text">Pre-order upcoming games to guarantee your copy and add desired titles to your wishlist for easy future reference.</p>

              <h5 className="card-title">Price Comparisons</h5>
              <p className="card-text">We do the legwork for you by comparing prices with other retailers. Find the best deals and save money on your PlayStation purchases.</p>

              <h5 className="card-title">User Reviews and Recommendations</h5>
              <p className="card-text">Read honest reviews from fellow gamers and get valuable insights before you buy. Share your own experiences to help others make informed choices.</p>

              <h5 className="card-title">Fast and Secure Checkout</h5>
              <p className="card-text">Enjoy a smooth and secure checkout process with a variety of payment options to suit your needs.</p>

              <h5 className="card-title">Reliable Shipping</h5>
              <p className="card-text">Get your games and gear delivered quickly and safely with our trusted shipping partners. Track your order every step of the way.</p>

              <h5 className="card-title">Top-Notch Customer Support</h5>
              <p className="card-text">Our friendly and knowledgeable customer support team is here to answer your questions and assist with any issues you may encounter.</p>
            </div>
          </div>
        </div>

        {/* Become a Part of the PS5-Ecommerce Family */}
        <div className="col-md-12 mb-4">
          <h2 className="text-info">Become a Part of the PS5-Ecommerce Family:</h2>
          <div className="card rounded-rectangle">
            <div className="card-body bg-white">
              <h5 className="card-title">Engaging Blog and Social Media Channels</h5>
              <p className="card-text">Stay up-to-date on the latest PlayStation news, game reviews, upcoming releases, and insightful articles.</p>

              <h5 className="card-title">Active Community Forum (or Social Media Group)</h5>
              <p className="card-text">Connect with other PlayStation enthusiasts, share your gaming experiences, discuss strategies, and discover hidden gems.</p>

              <h5 className="card-title">Loyalty Program</h5>
              <p className="card-text">Earn points for every purchase, redeem them for exclusive discounts, early access to pre-orders, and other exciting rewards.</p>
            </div>
          </div>
        </div>
      </div>

      <h2 className="text-primary mt-5">Shop with Confidence at PS5-Ecommerce!</h2>
      <p>We offer a comprehensive PlayStation experience with a wide variety of games, hardware, services, and a thriving community. Explore our website, discover your next gaming adventure, and level up your PlayStation experience with PS5-Ecommerce!</p>
      <div className="flex justify-center">
      <Link to="/shop">
      <button className="w-52 h-10 bg-primeColor text-white hover:bg-black duration-300 rounded-full">
      Continue Shopping
     </button>
    </Link>
    </div>
    </div>
  );
};

export default Service;
