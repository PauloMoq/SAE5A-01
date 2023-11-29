<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css"/>
    <div id="app">
      <navbar :isAuthenticated="isAuthenticated" :username="username" @logout="logout" />
      <router-view :updateAuthentication="updateAuthentication" />
    </div>
  </div>
</template>

<script>
import Navbar from './components/NavbarPage.vue'; // Assurez-vous d'importer correctement le chemin du composant navbar

export default {
  name: 'App',
  components: {
    Navbar,
  },
  data() {
    return {
      isAuthenticated: false,
      username: '',
    };
  },
  methods: {
    updateAuthentication({ isAuthenticated, username }) {
      this.isAuthenticated = isAuthenticated;
      this.username = username; // Mettez à jour l'username
    },
    logout() {
      this.isAuthenticated = false;
      this.username = '';
    },
  }
};
</script>

<style>
/* Styles globaux de l'application */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
body {
  margin: 0; /* Supprime la marge par défaut */
}

</style>
