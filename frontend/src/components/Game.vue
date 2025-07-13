<template>
  <div class="game-container">
    <h1>Vue Snake Game</h1>
    <canvas ref="gameCanvas" :width="canvasSize" :height="canvasSize"></canvas>
    <div class="game-info">
      <p>Score: {{ score }}</p>
      <p v-if="isGameOver">Game Over! Press 'R' to restart.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { store } from '../store';
import api from '../api';

const gameCanvas = ref(null);
const canvasSize = 400;
const gridSize = 20;
const score = ref(0);
const isGameOver = ref(false);

let snake = [{ x: 10, y: 10 }];
let food = {};
let direction = 'right';
let lastRenderTime = 0;
const snakeSpeed = 5; // blocks per second
let gameLoopRequest;

function main(currentTime) {
  if (isGameOver.value) return;

  gameLoopRequest = window.requestAnimationFrame(main);

  const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000;
  if (secondsSinceLastRender < 1 / snakeSpeed) return;

  lastRenderTime = currentTime;

  update();
  draw();
}

function update() {
  // Move snake
  const head = { x: snake[0].x, y: snake[0].y };
  if (direction === 'up') head.y--;
  if (direction === 'down') head.y++;
  if (direction === 'left') head.x--;
  if (direction === 'right') head.x++;

  snake.unshift(head);

  // Check for collision with food
  if (head.x === food.x && head.y === food.y) {
    score.value++;
    placeFood();
  } else {
    snake.pop();
  }

  // Check for collision with wall or self
  if (
    head.x < 0 || head.x >= gridSize ||
    head.y < 0 || head.y >= gridSize ||
    checkSelfCollision()
  ) {
    gameOver();
  }
}

function draw() {
  const ctx = gameCanvas.value.getContext('2d');

  // Clear canvas
  ctx.fillStyle = '#f0f0f0';
  ctx.fillRect(0, 0, canvasSize, canvasSize);

  // Draw snake
  ctx.fillStyle = 'green';
  snake.forEach(segment => {
    ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize, gridSize);
  });

  // Draw food
  ctx.fillStyle = 'red';
  ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize, gridSize);
}

function placeFood() {
  food = {
    x: Math.floor(Math.random() * gridSize),
    y: Math.floor(Math.random() * gridSize)
  };
  // Ensure food is not placed on the snake
  if (snake.some(segment => segment.x === food.x && segment.y === food.y)) {
    placeFood();
  }
}

function checkSelfCollision() {
  const [head, ...body] = snake;
  return body.some(segment => segment.x === head.x && segment.y === head.y);
}

async function gameOver() {
  isGameOver.value = true;
  window.cancelAnimationFrame(gameLoopRequest);

  // If user is logged in, submit the score
  if (store.user && score.value > 0) {
    try {
      await api.submitScore(score.value);
    } catch (error) {
      console.error("Failed to submit score:", error);
      // Optional: show a message to the user that score submission failed
    }
  }
}

function handleKeydown(e) {
  const key = e.key.toLowerCase();
  if (isGameOver.value && key === 'r') {
    resetGame();
    return;
  }

  if (key === 'w' && direction !== 'down') direction = 'up';
  else if (key === 's' && direction !== 'up') direction = 'down';
  else if (key === 'a' && direction !== 'right') direction = 'left';
  else if (key === 'd' && direction !== 'left') direction = 'right';
}

function resetGame() {
    snake = [{ x: 10, y: 10 }];
    placeFood();
    direction = 'right';
    score.value = 0;
    isGameOver.value = false;
    window.requestAnimationFrame(main);
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
  placeFood();
  window.requestAnimationFrame(main);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown);
  window.cancelAnimationFrame(gameLoopRequest);
});
</script>

<style scoped>
.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
canvas {
  border: 1px solid #ccc;
  background-color: #f0f0f0;
}
.game-info {
    margin-top: 20px;
    font-size: 1.2em;
}
</style> 