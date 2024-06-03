import React from 'react';
import Header from './components/Header';
import Carousel from './components/Carousel';
import Footer from './components/Footer';
import './components/styles.css';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <h1>Ps5 E-commerce</h1>
        <h2>Your Gateway to PS5 Adventure</h2>
        <Carousel />
      </main>
      <Footer />
    </div>
  );
}

export default App;
