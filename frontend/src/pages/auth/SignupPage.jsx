import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import AuthCard from '../../components/auth/AuthCard';
import InputField from '../../components/auth/InputField';
import GradientButton from '../../components/auth/GradientButton';
import bgImage from '../../assets/auth-bg.png';
import '../../components/auth/Auth.css';

const SignupPage = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.id]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Signup attempt:', formData);
  };

  return (
    <div className="auth-page">
      {/* Background Elements */}
      <div className="auth-background">
        <img src={bgImage} alt="Background" className="bg-image" />
        <div className="bg-gradient-overlay" />
        <div className="animated-gradient" />
      </div>

      {/* System Status */}
      <div className="system-status">
        <div className="status-dot" />
        <span>Vectra System Active</span>
      </div>

      <AuthCard>
        <div className="auth-header">
          <h1 className="auth-title">Create Your Account</h1>
          <p className="auth-subtitle">Start automating smarter today</p>
        </div>

        <form className="auth-form" onSubmit={handleSubmit}>
          <div className="input-group-row">
            <InputField
              id="firstName"
              label="First Name"
              value={formData.firstName}
              onChange={handleChange}
            />
            <InputField
              id="lastName"
              label="Last Name"
              value={formData.lastName}
              onChange={handleChange}
            />
          </div>
          
          <InputField
            id="email"
            label="Email Address"
            type="email"
            value={formData.email}
            onChange={handleChange}
          />
          <InputField
            id="password"
            label="Password"
            type="password"
            value={formData.password}
            onChange={handleChange}
          />
          <InputField
            id="confirmPassword"
            label="Confirm Password"
            type="password"
            value={formData.confirmPassword}
            onChange={handleChange}
          />

          <div className="auth-extras">
            <label className="checkbox-wrapper">
              <input type="checkbox" required />
              <span>I agree to the Terms & Conditions</span>
            </label>
          </div>

          <GradientButton>Create Account</GradientButton>
        </form>

        <div className="auth-footer">
          <p>
            Already have an account? 
            <Link to="/login" className="footer-link">Sign In</Link>
          </p>
        </div>

        <div className="micro-text">
          <span>Secure</span>
          <span>•</span>
          <span>Encrypted</span>
          <span>•</span>
          <span>Reliable</span>
        </div>
      </AuthCard>
    </div>
  );
};

export default SignupPage;
