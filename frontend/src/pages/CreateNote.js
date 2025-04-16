import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { createNote } from '../services/api';
import { AuthContext } from '../context/AuthContext';
import NoteForm from '../components/NoteForm';

const CreateNote = () => {
  const { token } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleSubmit = async (note) => {
    try {
      await createNote(note);
      navigate('/');
    } catch (err) {
      console.error('Failed to create note:', err);
    }
  };

  if (!token) {
    navigate('/login');
    return null;
  }

  return (
      <div className="create-note-container">
        <h2>Create New Note</h2>
        <NoteForm onSubmit={handleSubmit} isEditing={false} />
      </div>
  );
};

export default CreateNote;
