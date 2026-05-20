import React, { useState } from 'react';
import { useCommunity } from '../../context/CommunityContext';
import Modal from '../ui/Modal';
import Button from '../ui/Button';
import TagPill from './TagPill';
import styles from './CreateThreadModal.module.css';

const CreateThreadModal = ({ isOpen, onClose }) => {
  const { addThread, predefinedTags } = useCommunity();
  
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [selectedTags, setSelectedTags] = useState([]);

  const toggleTag = (tagId) => {
    setSelectedTags(prev => 
      prev.includes(tagId) 
        ? prev.filter(t => t !== tagId)
        : [...prev, tagId]
    );
  };

  const handleClose = () => {
    setTitle('');
    setContent('');
    setSelectedTags([]);
    onClose();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim() || !content.trim() || selectedTags.length === 0) return;
    
    addThread(title, content, selectedTags);
    handleClose();
  };

  const isValid = title.trim() && content.trim() && selectedTags.length > 0;

  return (
    <Modal isOpen={isOpen} onClose={handleClose} title="Start a New Discussion" size="large">
      <form onSubmit={handleSubmit} className={styles.form}>
        
        <div className={styles.formGroup}>
          <label className={styles.label}>Title</label>
          <input 
            type="text" 
            className={styles.input}
            placeholder="e.g., How do I chain schedules?"
            value={title}
            onChange={e => setTitle(e.target.value)}
            maxLength={100}
            required
          />
        </div>

        <div className={styles.formGroup}>
          <label className={styles.label}>
            Select Tags <span className={styles.required}>(required)</span>
          </label>
          <div className={styles.tagsContainer}>
            {predefinedTags.map(tag => (
              <TagPill 
                key={tag.id} 
                tag={tag}
                selectable
                selected={selectedTags.includes(tag.id)}
                onClick={() => toggleTag(tag.id)}
              />
            ))}
          </div>
          {selectedTags.length === 0 && (
            <span className={styles.errorText}>Please select at least one tag.</span>
          )}
        </div>

        <div className={styles.formGroup}>
          <label className={styles.label}>Details</label>
          <textarea 
            className={styles.textarea}
            placeholder="Provide details about your question, feedback, or idea..."
            value={content}
            onChange={e => setContent(e.target.value)}
            rows={8}
            required
          />
        </div>

        <div className={styles.actions}>
          <Button type="button" variant="secondary" onClick={handleClose}>
            Cancel
          </Button>
          <Button type="submit" variant="primary" disabled={!isValid}>
            Post Discussion
          </Button>
        </div>

      </form>
    </Modal>
  );
};

export default CreateThreadModal;
