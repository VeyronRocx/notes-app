import React, { useState, useEffect } from 'react';

const NoteForm = ({ note, onSubmit, isEditing }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  useEffect(() => {
    if (note) {
      setTitle(note.title);
      setContent(note.content);
    }
  }, [note]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ title, content });
  };

  return (
      <form className="note-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Title</label>
          <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
          />
        </div>
        <div className="form-group">
          <label htmlFor="content">Content</label>
          <textarea
              id="content"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              rows="10"
              required
          />
        </div>
        <button type="submit" className="submit-btn">
          {isEditing ? 'Update Note' : 'Create Note'}
        </button>
      </form>
  );
};

export default NoteForm;