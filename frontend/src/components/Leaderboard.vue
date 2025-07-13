<template>
  <div class="leaderboard">
    <h2>Top 10 Players</h2>
    <div v-if="loading">Loading...</div>
    <div v-if="error" class="error">{{ error }}</div>
    <ol v-if="scores.length">
      <li v-for="(score, index) in scores" :key="index">
        <span class="username">{{ score.username }}</span> - <span class="score">{{ score.score }}</span>
      </li>
    </ol>
    <p v-else>No scores yet. Be the first!</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../api';

const scores = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await api.getLeaderboard();
    scores.value = response.data;
  } catch (err) {
    error.value = 'Failed to load leaderboard.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.leaderboard {
  max-width: 400px;
  margin: auto;
}
ol {
  list-style-type: decimal;
  padding-left: 30px;
}
li {
  font-size: 1.2em;
  margin-bottom: 5px;
}
.username {
  font-weight: bold;
}
.score {
  color: #3eaf7c;
}
.error {
    color: red;
}
</style> 