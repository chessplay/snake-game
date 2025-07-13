import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // Address of our Flask backend
  withCredentials: true, // This is important for sessions to work
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  register(credentials) {
    return apiClient.post('/register', credentials);
  },
  login(credentials) {
    return apiClient.post('/login', credentials);
  },
  logout() {
    return apiClient.post('/logout');
  },
  getLeaderboard() {
    return apiClient.get('/leaderboard');
  },
  submitScore(score) {
    return apiClient.post('/scores', { score });
  }
}; 