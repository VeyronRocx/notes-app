import React, { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getNote, updateNote } from '../services/api';
import { AuthContext } from '../context/AuthContext';
import NoteForm from '../components/NoteForm';

const EditNote = () => {
  const { id } = useParams();
  const [note, setNote] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { token } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate('/login');
      return;
    }

    const fetchNote = async () => {
      try {
        const response = await getNote(id);
        setNote(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load note');
        setLoading(false);
      }
    };

    fetchNote();
  }, [id, token, navigate]);

  const handleSubmit = async (updatedNote) => {
    try {
      await updateNote(id, updatedNote);
      navigate('/');
    } catch (err) {
      setError('Failed to update note');
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
      <div className="edit-note-container">
        <h2>Edit Note</h2>
        <NoteForm note={note} onSubmit={handleSubmit} isEditing={true} />
      </div>
  );
};

export default EditNote;