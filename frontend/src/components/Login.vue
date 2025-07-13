<template>
  <div class="auth-form">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
      <p v-if="message" class="message">{{ message }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api';
import { store } from '../store';

const router = useRouter();
const username = ref('');
const password = ref('');
const message = ref('');

const handleLogin = async () => {
  try {
    const response = await api.login({ username: username.value, password: password.value });
    store.user = response.data.user; // Update the global store with user info
    router.push('/'); // Redirect to the game page after successful login
  } catch (error) {
    message.value = error.response?.data?.message || 'Login failed.';
  }
};
</script>

<style scoped>
.auth-form {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.message {
  color: red;
  margin-top: 10px;
}
input {
  display: block;
  width: 90%;
  margin-bottom: 10px;
  padding: 8px;
}
</style> 