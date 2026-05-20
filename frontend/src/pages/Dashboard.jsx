import React, { useState } from 'react';
import Sidebar from '../components/dashboard/Sidebar';
import Header from '../components/dashboard/Header';
import PremiumBanner from '../components/dashboard/PremiumBanner';
import StatsRow from '../components/dashboard/StatsRow';
import ScheduleCard from '../components/dashboard/ScheduleCard';
import OrganisationCard from '../components/dashboard/OrganisationCard';
import OrganisationsPage from './Organisations';
import SchedulerPage from './SchedulerPage';
import CommunityPage from './CommunityPage';
import { useOrganisations } from '../context/OrganisationContext';
import styles from './Dashboard.module.css';

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('home');
  const { organisations } = useOrganisations();

  return (
    <div className={styles.dashboardContainer}>
      <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />
      
      <main className={styles.mainContent}>
        <Header title={activeTab.charAt(0).toUpperCase() + activeTab.slice(1)} />
        
        <div className={styles.scrollArea}>
          <div className={styles.contentWrapper}>
            {activeTab === 'home' && (
              <>
                <PremiumBanner />
                <StatsRow />
              </>
            )}
            
            <div className={styles.grid}>
              {activeTab === 'home' ? (
                <>
                  <div className={styles.gridLeft}>
                    <ScheduleCard />
                  </div>
                  <div className={styles.gridRight}>
                    <OrganisationCard organisations={organisations} />
                  </div>
                </>
              ) : activeTab === 'organisation' ? (
                <div className={styles.fullWidth}>
                  <OrganisationsPage />
                </div>
              ) : activeTab === 'scheduled' ? (
                <div className={styles.fullWidth}>
                  <SchedulerPage />
                </div>
              ) : activeTab === 'community' ? (
                <div className={styles.fullWidth}>
                  <CommunityPage />
                </div>
              ) : (
                <div className={styles.placeholder}>
                  <h3>{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)} coming soon...</h3>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
