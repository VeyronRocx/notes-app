import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

const api = axios.create({
  baseURL: API_URL,
});

// Add auth token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const register = (username, password) => {
  return api.post('/register', { username, password });
};

export const login = (username, password) => {
  return api.post('/login', { username, password });
};

export const getNotes = () => {
  return api.get('/notes');
};

export const getNote = (id) => {
  return api.get(`/notes/${id}`);
};

export const createNote = (note) => {
  return api.post('/notes', note);
};

export const updateNote = (id, note) => {
  return api.put(`/notes/${id}`, note);
};

export const deleteNote = (id) => {
  return api.delete(`/notes/${id}`);
};

export default api;
