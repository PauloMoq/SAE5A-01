<template>
  <nav class="navbar">
    <div class="navbar-accueil">
      <router-link class="navbar-link" to="/" :class="{ 'active-link-accueil': currentRoute === '/' }"><img src="../../assets/logo-louvres.png" alt="Logo accueil louvres" id="logo_accueil">Accueil</router-link>
    </div>
    <div class="navbar-links">
      <router-link class="navbar-link" :class="{ 'active-link-search': currentRoute === '/search' }" to="/search" id="research"><img src="./../../assets/search.png" alt=""> Rechercher</router-link>
      <router-link class="navbar-link" v-if="!isAuthenticated" :class="{ 'active-link-login': currentRoute === '/login' }" to="/login">Connexion</router-link>
      <router-link class="navbar-link" v-if="!isAuthenticated" :class="{ 'active-link-register': currentRoute === '/register' }" to="/register">Inscription</router-link>
      <router-link class="navbar-link" v-if="isAuthenticated" :class="{ 'active-link-historique': currentRoute === '/historique' }" to="/historique">Historique</router-link>
      <router-link v-if="isAuthenticated" :class="{ 'active-link-logout': currentRoute === '/login' }" @click="handleLogout" to="/login" id="logout">{{ username }}<img src="./../../assets/icon-logout.png" alt=""></router-link> 
    </div>
  </nav>
</template>
  
<script src="./NavbarPage.js"></script>
<style lang="scss" src="./NavbarPage.scss"></style>