<script setup>
import { store } from './store.js';
import api from './api.js';
import { useRouter } from 'vue-router';

const router = useRouter();

const handleLogout = async () => {
  try {
    await api.logout();
    store.user = null;
    router.push('/login');
  } catch (error) {
    console.error("Failed to logout", error);
    // Even if API fails, log the user out on the frontend
    store.user = null; 
  }
};
</script>

<template>
  <header>
    <nav>
      <router-link to="/">Game</router-link> |
      <router-link to="/leaderboard">Leaderboard</router-link> |
      <template v-if="store.user">
        <span>Welcome, {{ store.user.username }}</span> |
        <a href="#" @click.prevent="handleLogout">Logout</a>
      </template>
      <template v-else>
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Register</router-link>
      </template>
    </nav>
  </header>
  <main>
    <router-view></router-view>
  </main>
</template>

<style>
header {
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #ccc;
}
nav {
  display: flex;
  justify-content: center;
  gap: 15px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}
nav a.router-link-exact-active {
  color: #42b983;
}
span {
    padding: 0 10px;
}
a {
    cursor: pointer;
}
</style> 