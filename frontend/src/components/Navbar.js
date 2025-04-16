import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Navbar = () => {
  const { currentUser, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
      <nav className="navbar">
        <div className="navbar-brand">
          <Link to="/">Notes App</Link>
        </div>
        <div className="navbar-menu">
          {currentUser ? (
              <>
                <span className="navbar-item">Welcome, {currentUser.username}</span>
                <button className="logout-btn" onClick={handleLogout}>Logout</button>
              </>
          ) : (
              <>
                <Link to="/login" className="navbar-item">Login</Link>
                <Link to="/register" className="navbar-item">Register</Link>
              </>
          )}
        </div>
      </nav>
  );
};

export default Navbar;
