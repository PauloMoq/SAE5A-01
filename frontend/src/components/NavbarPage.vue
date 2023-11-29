<template>
  <nav class="navbar">
    <div class="navbar-accueil">
      <router-link class="navbar-link" to="/" :class="{ 'active-link-accueil': currentRoute === '/' }"><img src="../assets/logo-louvres.png" alt="Logo accueil louvres" id="logo_accueil">Accueil</router-link>
    </div>
    <div class="navbar-links">
      <router-link class="navbar-link" :class="{ 'active-link-search': currentRoute === '/search' }" to="/search"><img src="./../assets/search.png" alt=""> Rechercher</router-link>
      <router-link class="navbar-link" v-if="!isAuthenticated" :class="{ 'active-link-login': currentRoute === '/login' }" to="/login">Connexion</router-link>
      <router-link class="navbar-link" v-if="!isAuthenticated" :class="{ 'active-link-register': currentRoute === '/register' }" to="/register">Inscription</router-link>
      <router-link class="navbar-link" v-if="isAuthenticated" :class="{ 'active-link-historique': currentRoute === '/historique' }" to="/historique">Historique</router-link>
      <router-link v-if="isAuthenticated" :class="{ 'active-link-logout': currentRoute === '/login' }" @click="handleLogout" to="/login" id="logout">{{ username }} <img src="./../assets/icon-logout.png" alt=""></router-link> 
    </div>
  </nav>
</template>
  
<script>
export default {
  props: ['isAuthenticated', 'username'],
  data() {
    return {
      currentRoute: '',
    };
  },
  watch: {
    '$route'(to) {
      this.currentRoute = to.path;
    },
  },
  methods: {
    handleLogout() {
      this.$emit('logout');
    },
  },
};
</script>
<style scoped>
/* Styles spécifiques à la navbar */
.navbar-accueil{
  display: flex;
  flex: 1;
  justify-content: flex-start;
  margin-left: 20px;
}
#logo_accueil {
  width: 25px;
  height: 25px;
  filter: invert(100%); /* Inverser les couleurs de l'image (de noir à blanc) */
  margin-top: -5px;
  margin-right: 5px;
}
#navbar-accueil:hover {
  filter: invert(50%); /* Inverser les couleurs de l'image (de noir à blanc) */
}

.navbar {
  background-color: #004225; /* Couleur d'arrière-plan de la barre de navigation (personnalisez-la selon vos besoins) */
  color: #fff; /* Couleur du texte */
  padding: 15px 0; /* Espacement intérieur de la barre de navigation */
  display: flex;
  justify-content: flex-end;
  align-items: center;
  width: 100vw; /* Utilisation de la largeur de la fenêtre pour supprimer les marges */
  margin: 0; /* Supprimer les marges par défaut */
  position: fixed; /* Fixer la barre de navigation en haut de la page */
  top: 0; /* Position en haut de la page */
  left: 0; /* Position à gauche de la page */
  right: 0; /* Position à droite de la page */
  z-index: 1000; /* Assurer que la barre de navigation est au-dessus de tout autre contenu */
  background: rgba(0, 66, 37, 0.9); /* Couleur de fond semi-transparente avec flou */
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(7px); /* Effet de flou */
  max-height: 60px;
}

.navbar-links {
  display: flex;
  gap: 20px; /* Espacement entre les liens et le bouton */
  margin-right: 10px;
}

.navbar-link {
  text-decoration: none;
  color: #fff; /* Couleur du texte des liens */
  font-size: 20px; /* Taille du texte des liens */
  transition: 0.3s; /* Ajout de la transition pour la couleur et la taille du texte */
}
.navbar-link:hover {
  color: #dcb253; /* Couleur du texte des liens au survol (personnalisez-la selon vos besoins) */
  font-size: 22px;
}

/* Permet de garder le style du hover sur le nom de la page dans la navbar, lorsqu'on est sur la page active  */
/* le a. permet de donner la priorité à ce CSS */
a.active-link-login, a.active-link-register, a.active-link-historique, a.active-link-logout, a.active-link-accueil, a.active-link-search {
  color: #dcb253; /* Couleur du texte des liens au survol (personnalisez-la selon vos besoins) */
  font-size: 22px;
  transition: 0.3s; /* Ajout de la transition pour la couleur et la taille du texte */
}

#logout img {
  width: 25px;
  height: 25px;
  filter: invert(100%); /* Inverser les couleurs de l'image (de noir à blanc) */
  margin-top: -3px;
}
#logout {
  text-decoration: none;
  color: #fff; /* Couleur du texte des liens */
  font-size: 20px; /* Taille du texte des liens */
  transition: 0.3s; 
}
#logout:hover {
  color: #dcb253; /* Couleur du texte des liens au survol (personnalisez-la selon vos besoins) */
}

.navbar-link img {
  color:#dcb253;
  width: 25px;
  height: 25px;
  filter: invert(100%); /* Inverser les couleurs de l'image (de noir à blanc) */
  margin-top: -3px;
}
</style>