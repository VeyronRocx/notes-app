import React, { useEffect, useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getNotes, deleteNote } from '../services/api';
import { AuthContext } from '../context/AuthContext';
import NoteItem from '../components/NoteItem';

const Home = () => {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { currentUser, token } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate('/login');
      return;
    }

    const fetchNotes = async () => {
      try {
        const response = await getNotes();
        setNotes(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load notes');
        setLoading(false);
      }
    };

    fetchNotes();
  }, [token, navigate]);

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this note?')) {
      try {
        await deleteNote(id);
        setNotes(notes.filter(note => note.id !== id));
      } catch (err) {
        setError('Failed to delete note');
      }
    }
  };

  if (!currentUser) {
    return <div>Please log in to view your notes.</div>;
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
      <div className="home-container">
        <div className="home-header">
          <h2>My Notes</h2>
          <Link to="/create" className="create-btn">Create New Note</Link>
        </div>

        {error && <div className="error-message">{error}</div>}

        <div className="notes-list">
          {notes.length === 0 ? (
              <p>You don't have any notes yet. Create one!</p>
          ) : (
              notes.map(note => (
                  <NoteItem
                      key={note.id}
                      note={note}
                      onDelete={handleDelete}
                  />
              ))
          )}
        </div>
      </div>
  );
};

export default Home;