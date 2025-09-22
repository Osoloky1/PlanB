<template>
  <div class="carrito-container">
    <!-- NAVBAR -->
    <header class="navbar">
      <button @click="toggleMenu" class="menu-btn">☰</button>
      <h1 class="logo">iEssence</h1>
      <div class="user-actions">
        <button class="login-btn">Login</button>
        <button class="register-btn">Registrarse</button>
        <span class="user-icon">👤</span>
      </div>
    </header>

    <!-- TÍTULO -->
    <h2 class="titulo">Resumen de Carrito 🛒</h2>

    <!-- TABLA DEL CARRITO -->
    <table class="tabla-carrito">
      <thead>
        <tr>
          <th>Imagen Miniatura</th>
          <th>Id_producto</th>
          <th>Nombre Producto</th>
          <th>Precio</th>
          <th>Cantidad</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in carrito" :key="index">
          <td><img :src="item.imagen" :alt="item.nombre" class="miniatura" /></td>
          <td>{{ item.id }}</td>
          <td>{{ item.nombre }}</td>
          <td>$ {{ item.precio }}</td>
          <td>{{ item.cantidad }}</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td colspan="4" class="total-label">Total:</td>
          <td class="total-precio">$ {{ total }}</td>
        </tr>
      </tfoot>
    </table>

    <!-- BOTÓN IR A PAGAR -->
    <div class="acciones">
      <button class="btn-pagar">Ir a pagar ➤</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const carrito = ref([
  { id: 1, nombre: 'Audífonos Pro', precio: 129990, cantidad: 1, imagen: 'audifonos1.png' },
  { id: 2, nombre: 'Cable USB-C', precio: 19990, cantidad: 2, imagen: 'cable.png' },
])

// Calcular total dinámicamente
const total = computed(() =>
  carrito.value.reduce((acc, item) => acc + item.precio * item.cantidad, 0)
)

const toggleMenu = () => {
  console.log('Sidebar aquí si la agregas')
}
</script>

<style scoped>
/* Contenedor */
.carrito-container {
  background: #e8e8ec;
  min-height: 100vh;
  padding: 2rem;
  font-family: Arial, sans-serif;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #243447;
  padding: 1rem;
  color: white;
}

.menu-btn {
  font-size: 1.5rem;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
}

.logo {
  font-size: 1.5rem;
}

.user-actions button {
  margin: 0 0.5rem;
  background: none;
  border: 1px solid white;
  color: white;
  padding: 0.3rem 0.7rem;
  cursor: pointer;
  border-radius: 5px;
}

/* Título */
.titulo {
  text-align: center;
  background: white;
  padding: 0.5rem 1rem;
  border-radius: 10px;
  margin: 1.5rem auto;
  display: inline-block;
  font-size: 1.5rem;
  font-weight: bold;
}

/* Tabla */
.tabla-carrito {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem auto;
  background: white;
  border-radius: 10px;
  overflow: hidden;
}

.tabla-carrito th,
.tabla-carrito td {
  border: 1px solid #ccc;
  padding: 0.8rem;
  text-align: center;
}

.tabla-carrito th {
  background: #f5f5f5;
  font-weight: bold;
}

.miniatura {
  width: 50px;
  height: auto;
  border-radius: 5px;
}

/* Total */
.total-label {
  text-align: right;
  font-weight: bold;
}

.total-precio {
  font-weight: bold;
}

/* Botón pagar */
.acciones {
  text-align: right;
  margin-top: 1rem;
}

.btn-pagar {
  background: #4cafef;
  border: none;
  padding: 0.8rem 1.5rem;
  color: white;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 20px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.btn-pagar:hover {
  background: #369ad6;
}
</style>
