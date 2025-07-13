<template>
  <div class="auth-form">
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Register</button>
      <p v-if="message" class="message">{{ message }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api';

const router = useRouter();
const username = ref('');
const password = ref('');
const message = ref('');

const handleRegister = async () => {
  try {
    await api.register({ username: username.value, password: password.value });
    router.push('/login'); // Redirect to login page after successful registration
  } catch (error) {
    message.value = error.response?.data?.message || 'Registration failed.';
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