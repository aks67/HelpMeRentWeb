import React, {useState, useEffect} from "react";
import './Title.css';

const Title = ({ text }) => {
    const [isAnimated, setIsAnimated] = useState(false);
  
    useEffect(() => {
      setTimeout(() => {
        setIsAnimated(true);
      }, 100);
    }, []);
  
    return (
      <h1 className={`animated-title ${isAnimated ? 'animate' : ''}`}>
        {text}
      </h1>
    );
  };
  
  export default Title;