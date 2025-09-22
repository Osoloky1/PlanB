// src/main.ts
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router' // 👉 Importa las rutas

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

const app = createApp(App)

app.use(createPinia()) // 👉 Estado global (Pinia)
app.use(router) // 👉 Habilita la navegación con vue-router

app.mount('#app') // 👉 Renderiza la app en el div con id="app"
