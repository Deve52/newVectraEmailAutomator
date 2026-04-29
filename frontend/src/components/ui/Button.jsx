import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { buttonHover } from '../../lib/motion';
import './Button.css';

const Button = ({ children, variant = 'primary', onClick, className = '', href, to, ...props }) => {
  if (to) {
    const MotionLink = motion.create(Link);
    return (
      <MotionLink
        to={to}
        className={`btn btn-${variant} ${className}`}
        onClick={onClick}
        variants={buttonHover}
        whileHover="hover"
        whileTap="tap"
        {...props}
      >
        {children}
      </MotionLink>
    );
  }

  const Component = href ? motion.a : motion.button;
  
  return (
    <Component 
      className={`btn btn-${variant} ${className}`} 
      onClick={onClick}
      variants={buttonHover}
      whileHover="hover"
      whileTap="tap"
      href={href}
      {...props}
    >
      {children}
    </Component>
  );
};

export default Button;

