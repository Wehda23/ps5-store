// Footer.js

import React from 'react';
import './styles.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="social-icons">
        <a href="#"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/facebook.svg" alt="Facebook" style={{ filter: 'invert(1)' }} /></a>
        <a href="#"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/youtube.svg" alt="YouTube" style={{ filter: 'invert(1)' }} /></a>
        <a href="#"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/discord.svg" alt="Twitch" style={{ filter: 'invert(1)' }} /></a>
        <a href="#"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/twitter.svg" alt="Twitter" style={{ filter: 'invert(1)' }} /></a>
      </div>
      <p>ALX_SE Team</p>
    </footer>
  );
};

export default Footer;
