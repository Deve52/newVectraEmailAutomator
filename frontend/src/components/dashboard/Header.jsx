import React from 'react';
import { motion } from 'framer-motion';
import Badge from '../ui/Badge';
import styles from './Header.module.css';

const Header = ({ title = 'Dashboard' }) => {
  return (
    <header className={styles.header}>
      <div className={styles.left}>
        <h1 className={styles.title}>{title}</h1>
      </div>

      <div className={styles.right}>
        <div className={styles.actionGroup}>
          <motion.button 
            className={styles.iconButton}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <MessageIcon />
          </motion.button>

          <motion.button 
            className={styles.iconButton}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <NotificationIcon />
            <Badge variant="neon" className={styles.badge}>3</Badge>
          </motion.button>
        </div>

        <div className={styles.divider} />

        <motion.button 
          className={styles.profileDropdown}
          whileHover={{ backgroundColor: 'rgba(0,0,0,0.03)' }}
        >
          <div className={styles.avatarMini}>JD</div>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="m6 9 6 6 6-6"/>
          </svg>
        </motion.button>
      </div>
    </header>
  );
};

const MessageIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
  </svg>
);

const NotificationIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>
  </svg>
);

export default Header;
