import React from 'react';
import './styles.css';

const Carousel = () => {
  return (
    <div className="carousel">
      <button className="carousel-button prev">&lt;</button>
      <div className="carousel-items">
        <div className="item">
          <img src="/joystick.png" alt="Joystick" />
          <p>Joystick</p>
        </div>
        <div className="item">
          <img src="/controller.png" alt="Controller" />
          <p>Controller</p>
        </div>
        <div className="item">
          <img src="/headset.png" alt="Headset" />
          <p>Headset</p>
        </div>
        <div className="item">
          <img src="/console.png" alt="Console" />
          <p>Console</p>
        </div>
      </div>
      <button className="carousel-button next">&gt;</button>
    </div>
  );
};

export default Carousel;
