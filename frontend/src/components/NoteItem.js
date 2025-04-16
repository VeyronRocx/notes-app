import React from 'react';
import { Link } from 'react-router-dom';

const NoteItem = ({ note, onDelete }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  return (
      <div className="note-item">
        <h3>{note.title}</h3>
        <p className="note-date">Last updated: {formatDate(note.updated_at)}</p>
        <div className="note-preview">
          {note.content.length > 100
              ? `${note.content.substring(0, 100)}...`
              : note.content}
        </div>
        <div className="note-actions">
          <Link to={`/edit/${note.id}`} className="edit-btn">Edit</Link>
          <button onClick={() => onDelete(note.id)} className="delete-btn">Delete</button>
        </div>
      </div>
  );
};

export default NoteItem;