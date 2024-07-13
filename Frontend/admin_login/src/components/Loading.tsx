import React from 'react';

const Loading: React.FC = () => {
  return (
    <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-300 bg-opacity-50 z-50">
      <div className="spinner"></div>
    </div>
  );
};

export default Loading;
