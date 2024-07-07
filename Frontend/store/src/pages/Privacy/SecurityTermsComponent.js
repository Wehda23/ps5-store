import React from 'react';
import securityTerms from './securityTerms';

const SecurityTermsComponent = () => {
  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Security Terms for PlayStation 5 E-commerce Website</h1>
      {securityTerms.map((term, index) => (
        <div className="card mb-4" key={index}>
          <div className="card-header">
            <h2 className="card-title">{term.title}</h2>
          </div>
          <div className="card-body">
            <p className="card-text">{term.description}</p>
            <ul>
              {term.details.map((detail, idx) => (
                <li key={idx}>{detail}</li>
              ))}
            </ul>
          </div>
        </div>
      ))}
    </div>
  );
};

export default SecurityTermsComponent;
