import React from 'react';
import './styles.css';

const Header = () => {
  return (
    <header>
      <div className="logo">
        <img src="/logo.png" alt="PS5 Logo" />
        <span>PlayStation</span>
      </div>
      <nav>
        <ul>
          <li><a href="#">Games</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="#">Shop</a></li>
          <li><a href="#">Help</a></li>
          <li><a href="#">Sign In</a></li>
        </ul>
      </nav>
      <div className="search-signin">
        <a href="#" className="search">Search</a>
        <a href="#" className="signin">Sign In</a>
      </div>
    </header>
  );
};

export default Header;
