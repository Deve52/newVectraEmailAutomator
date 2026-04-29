import React from 'react';
import './Auth.css';

const InputField = ({ label, type = "text", value, onChange, placeholder = " ", required = true, id }) => {
  return (
    <div className="input-group">
      <input
        id={id}
        type={type}
        className="input-field"
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        required={required}
      />
      <label htmlFor={id} className="floating-label">
        {label}
      </label>
    </div>
  );
};

export default InputField;
