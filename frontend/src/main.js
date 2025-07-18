import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Import the router
import './style.css'

createApp(App)
  .use(router) // Tell Vue to use the router
  .mount('#app') 