import React, { useState, useEffect } from 'react';
import { fetchGuidesData } from '../lib/mockGuidesData';
import FeaturedGuideHero from '../components/guides/FeaturedGuideHero';
import SearchFilterLayer from '../components/guides/SearchFilterLayer';
import OfficialGuidesSection from '../components/guides/OfficialGuidesSection';
import CommunityGuidesSection from '../components/guides/CommunityGuidesSection';
import TrendingGuidesRail from '../components/guides/TrendingGuidesRail';
import QuickTipsPanel from '../components/guides/QuickTipsPanel';
import GuideReader from '../components/guides/GuideReader';
import styles from './GuidesPage.module.css';

const GuidesPage = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeFilter, setActiveFilter] = useState('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedGuide, setSelectedGuide] = useState(null);
  const [bookmarkedIds, setBookmarkedIds] = useState(new Set());

  const handleBookmarkToggle = (id) => {
    setBookmarkedIds(prev => {
      const newSet = new Set(prev);
      if (newSet.has(id)) newSet.delete(id);
      else newSet.add(id);
      return newSet;
    });
  };

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const result = await fetchGuidesData();
        setData(result);
      } catch (error) {
        console.error('Error fetching guides:', error);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  if (loading) {
    return <div className={styles.loading}>Loading Knowledge Ecosystem...</div>;
  }

  if (!data) return null;

  // Filter logic
  const filterGuides = (guides) => {
    return guides.filter(guide => {
      const matchesSearch = 
        guide.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        guide.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
        guide.tags.some(t => t.toLowerCase().includes(searchQuery.toLowerCase()));
      
      const matchesFilter = activeFilter === 'All' || 
        guide.category === activeFilter ||
        guide.difficulty === activeFilter ||
        guide.tags.includes(activeFilter) ||
        (activeFilter === 'Trending' && guide.trending) ||
        (activeFilter === 'Community' && !guide.isOfficial) ||
        (activeFilter === 'Saved' && bookmarkedIds.has(guide.id));

      return matchesSearch && matchesFilter;
    });
  };

  const filteredOfficial = filterGuides(data.official);
  const filteredCommunity = filterGuides(data.community);

  const showHero = activeFilter === 'All' && searchQuery === '';

  return (
    <div className={styles.pageContainer}>
      <SearchFilterLayer 
        activeFilter={activeFilter} 
        setActiveFilter={setActiveFilter}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
      />

      {showHero && <FeaturedGuideHero guide={data.featured} onClick={setSelectedGuide} />}

      <div className={styles.layoutGrid}>
        <div className={styles.mainColumn}>
          {(filteredOfficial.length > 0 || showHero) && (
            <OfficialGuidesSection 
              guides={filteredOfficial} 
              onGuideClick={setSelectedGuide} 
              bookmarkedIds={bookmarkedIds}
              onBookmarkToggle={handleBookmarkToggle}
            />
          )}
          
          {(filteredCommunity.length > 0 || showHero) && (
            <CommunityGuidesSection 
              guides={filteredCommunity} 
              onGuideClick={setSelectedGuide} 
              bookmarkedIds={bookmarkedIds}
              onBookmarkToggle={handleBookmarkToggle}
            />
          )}

          {filteredOfficial.length === 0 && filteredCommunity.length === 0 && (
            <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: '4rem 0' }}>
              No workflows found matching your criteria.
            </div>
          )}
        </div>

        <div className={styles.sidebarColumn}>
          <TrendingGuidesRail guides={[...data.official, ...data.community]} />
          <QuickTipsPanel tips={data.tips} />
        </div>
      </div>
      
      {selectedGuide && (
        <GuideReader 
          guide={selectedGuide} 
          onClose={() => setSelectedGuide(null)} 
        />
      )}
    </div>
  );
};

export default GuidesPage;
