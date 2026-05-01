import React, { useState } from 'react';
import Sidebar from '../components/dashboard/Sidebar';
import Header from '../components/dashboard/Header';
import PremiumBanner from '../components/dashboard/PremiumBanner';
import StatsRow from '../components/dashboard/StatsRow';
import ScheduleCard from '../components/dashboard/ScheduleCard';
import OrganisationCard from '../components/dashboard/OrganisationCard';
import styles from './Dashboard.module.css';

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('home');

  return (
    <div className={styles.dashboardContainer}>
      <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />
      
      <main className={styles.mainContent}>
        <Header title={activeTab.charAt(0).toUpperCase() + activeTab.slice(1)} />
        
        <div className={styles.scrollArea}>
          <div className={styles.contentWrapper}>
            <PremiumBanner />
            <StatsRow />
            
            <div className={styles.grid}>
              <div className={styles.gridLeft}>
                <ScheduleCard />
              </div>
              <div className={styles.gridRight}>
                <OrganisationCard organisations={[]} />
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
