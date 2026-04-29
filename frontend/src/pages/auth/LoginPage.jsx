import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import AuthCard from '../../components/auth/AuthCard';
import InputField from '../../components/auth/InputField';
import GradientButton from '../../components/auth/GradientButton';
import bgImage from '../../assets/auth-bg.png';
import '../../components/auth/Auth.css';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login attempt:', { email, password });
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
          <h1 className="auth-title">Welcome Back</h1>
          <p className="auth-subtitle">Sign in to your Vectra dashboard</p>
        </div>

        <form className="auth-form" onSubmit={handleSubmit}>
          <InputField
            id="email"
            label="Email Address"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <InputField
            id="password"
            label="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <div className="auth-extras">
            <label className="checkbox-wrapper">
              <input type="checkbox" />
              <span>Remember me</span>
            </label>
            <Link to="#" className="forgot-link">Forgot Password?</Link>
          </div>

          <GradientButton>Sign In</GradientButton>
        </form>

        <div className="auth-footer">
          <p>
            Don't have an account? 
            <Link to="/signup" className="footer-link">Sign Up</Link>
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

export default LoginPage;
