<template>
  <div class="home">
    <!-- NAVBAR -->
    <header class="navbar">
      <button @click="toggleMenu" class="menu-btn">☰</button>

      <!-- logo -->
      <router-link to="/" class="logo-link">
        <h1 class="logo">iEssence</h1>
      </router-link>

      <div class="user-actions">
        <!-- Cambié los botones por router-link -->
        <router-link to="/login" class="btn-link">Login</router-link>
        <router-link to="/register" class="btn-link">Registrarse</router-link>
        <span class="user-icon">👤</span>
      </div>
    </header>

    <!-- SIDEBAR -->
    <aside v-if="menuOpen" class="sidebar">
      <div class="sidebar-header">
        <button @click="toggleMenu" class="close-btn">✖</button>
      </div>
      <ul>
        <li><router-link to="/">Catálogo</router-link></li>
        <li><router-link to="/carrito">Carro 🛒</router-link></li>
        <li><router-link to="/acerca">Acerca de nosotros</router-link></li>
      </ul>
    </aside>

    <!-- CATÁLOGO DE PRODUCTOS -->
    <main class="catalogo">
      <div v-for="(producto, index) in productos" :key="index" class="producto-card">
        <img :src="`/src/assets/${producto.imagen}`" :alt="producto.nombre" />
        <h3>{{ producto.nombre }}</h3>
        <p>{{ producto.marca }}</p>
        <p class="precio">$ {{ producto.precio }}</p>
        <button class="btn-agregar">Agregar al carrito</button>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const menuOpen = ref(false)
const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const productos = ref([
  { nombre: 'Audífonos Pro', marca: 'Marca X', precio: 129990, imagen: 'audifonos1.png' },
  { nombre: 'Audífonos Air', marca: 'Marca Y', precio: 159990, imagen: 'audifonos2.png' },
  { nombre: 'Headset Gamer', marca: 'Marca Z', precio: 99990, imagen: 'headset.png' },
  { nombre: 'Cargador Rápido', marca: 'Marca A', precio: 29990, imagen: 'cargador.png' },
  { nombre: 'Cable USB-C', marca: 'Marca B', precio: 19990, imagen: 'cable.png' },
  { nombre: 'PowerBank', marca: 'Marca C', precio: 49990, imagen: 'powerbank.png' },
])
</script>

<style scoped>
/* Estilos generales */
.home {
  font-family: Arial, sans-serif;
  color: #fff;
  background-color: #1f1f2e;
  min-height: 100vh;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #243447;
  padding: 1rem;
}

.menu-btn {
  font-size: 1.5rem;
  background: none;
  color: white;
  border: none;
  cursor: pointer;
}

.logo {
  font-size: 1.5rem;
}

.user-actions {
  display: flex;
  align-items: center;
}

.btn-link {
  margin: 0 0.5rem;
  text-decoration: none;
  border: 1px solid white;
  color: white;
  padding: 0.3rem 0.7rem;
  border-radius: 5px;
  transition: background 0.2s;
}

.btn-link:hover {
  background: white;
  color: #243447;
}

.user-icon {
  margin-left: 10px;
}

/* Sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 200px;
  height: 100%;
  background-color: #2e3a4f;
  padding: 1rem;
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar li {
  margin: 1rem 0;
}

.sidebar a {
  color: white;
  text-decoration: none;
}

.sidebar a:hover {
  text-decoration: underline;
}

/* click boton */
.logo-link {
  text-decoration: none;
  color: inherit;
}

/* Catálogo */
.catalogo {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
  padding: 2rem;
}

.producto-card {
  background: #2c2c3e;
  border-radius: 10px;
  padding: 1rem;
  text-align: center;
}

.producto-card img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}

.precio {
  font-weight: bold;
  margin: 0.5rem 0;
}

.btn-agregar {
  background-color: #4cafef;
  border: none;
  padding: 0.5rem 1rem;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}
</style>
