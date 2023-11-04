import React, { useState, useEffect } from 'react';
import './DescriptionBox.css';

const DescriptionBox = ({ title, description, code }) => {
  const [isAnimated, setIsAnimated] = useState(false);

  useEffect(() => {
    // Add a slight delay to trigger the animation after the component mounts
    setTimeout(() => {
      setIsAnimated(true);
    }, 100);
  }, []);

  return (
    <div className={`description-box ${isAnimated ? 'animate' : ''}`}>
      <h2>{title}</h2>
      <p className="description-text">{description}</p>
      <pre>
        <code>{code}</code>
      </pre>
    </div>
  );
};

export default DescriptionBox;
