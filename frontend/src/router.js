import { createRouter, createWebHistory } from 'vue-router';
import Game from './components/Game.vue';
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import Leaderboard from './components/Leaderboard.vue';

const routes = [
  { path: '/', name: 'Game', component: Game },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/leaderboard', name: 'Leaderboard', component: Leaderboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 