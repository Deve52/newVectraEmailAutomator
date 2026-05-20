import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './layouts/Navbar';
import Footer from './layouts/Footer';
import Hero from './sections/Hero';
import Features from './sections/Features';
import CTA from './sections/CTA';
import LoginPage from './pages/auth/LoginPage';
import SignupPage from './pages/auth/SignupPage';
import Dashboard from './pages/Dashboard';
import { OrganisationProvider } from './context/OrganisationContext';
import { SchedulerProvider } from './context/SchedulerContext';
import { CommunityProvider } from './context/CommunityContext';

const LandingPage = () => (
  <>
    <Hero />
    <Features />
    <CTA />
  </>
);

function App() {
  return (
    <OrganisationProvider>
      <SchedulerProvider>
        <CommunityProvider>
          <Router>
            <Routes>
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="*" element={
                <div className="app-wrapper">
                  <Navbar />
                  <main>
                    <Routes>
                      <Route path="/" element={<LandingPage />} />
                      <Route path="/login" element={<LoginPage />} />
                      <Route path="/signup" element={<SignupPage />} />
                    </Routes>
                  </main>
                  <Footer />
                </div>
              } />
            </Routes>
          </Router>
        </CommunityProvider>
      </SchedulerProvider>
    </OrganisationProvider>
  );
}

export default App;
