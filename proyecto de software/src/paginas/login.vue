<template>
  <div class="auth-container">
    <div class="auth-box">
      <h2 class="title">Ingresa</h2>
      <form @submit.prevent="login">
        <input type="email" v-model="email" placeholder="Dirección de correo" required />
        <input type="password" v-model="password" placeholder="Contraseña" required />

        <!-- Botones de login social -->
        <button type="button" class="btn-social facebook">Sign up with Facebook</button>
        <button type="button" class="btn-social google">Sign up with Google</button>
        <button type="button" class="btn-social apple">Sign up with Apple</button>
        <router-link to="/register" class="btn-link">Registrarse</router-link>

        <button type="submit" class="btn-main">Continuar</button>
      </form>
    </div>
    <!-- logo -->
    <router-link to="/" class="logo-link">
      <h1 class="logo">iEssence</h1>
    </router-link>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const login = () => {
  console.log('Login con:', email.value, password.value)
  // Aquí conectas al backend o proveedor de auth
}
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #1c2147;
}
.auth-box {
  background: #c9cbe8;
  padding: 2rem;
  border-radius: 10px;
  width: 320px;
  text-align: center;
}
.title {
  margin-bottom: 1.5rem;
  color: #d94d6a;
}
input {
  width: 100%;
  margin: 0.5rem 0;
  padding: 0.7rem;
  border: none;
  border-radius: 5px;
}
.btn-main {
  width: 100%;
  padding: 0.7rem;
  background-color: #1c2147;
  color: white;
  border: none;
  border-radius: 5px;
  margin-top: 1rem;
  cursor: pointer;
}
.btn-social {
  width: 100%;
  padding: 0.6rem;
  margin: 0.4rem 0;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}
.facebook {
  background: #3b5998;
  color: white;
}
.google {
  background: #db4437;
  color: white;
}
.apple {
  background: #000;
  color: white;
}

.logo-link {
  position: absolute;
  top: 20px;
  left: 20px;
  color: white;
  text-decoration: none;
  font-size: 1.8rem;
  font-weight: bold;
}

.logo {
  margin: 0;
}
</style>
