<template>
  <nav class="navbar">
    <div class="navbar-accueil">
      <router-link class="navbar-link" to="/">Accueil</router-link>
    </div>
    <div class="navbar-links">
      <router-link class="navbar-link" v-if="!authenticated" to="/login">Connexion</router-link>
      <router-link class="navbar-link" v-if="!authenticated" to="/register">Inscription</router-link>
      <router-link class="navbar-link" v-if="authenticated" to="/dashboard">Tableau de bord</router-link>
      <button v-if="authenticated" @click="logout" class="logout-button">Déconnexion</button>
    </div>
  </nav>
</template>
  
<script>
export default {
  computed: {
    authenticated() {
      // Utilisez cette propriété calculée pour vérifier si l'utilisateur est authentifié.
      // Par exemple, en vérifiant la présence d'un jeton d'authentification ou d'autres informations d'authentification.
      // Renvoyez true si l'utilisateur est authentifié, sinon renvoyez false.
      return false; // À personnaliser en fonction de votre logique d'authentification.
    },
  },
  methods: {
    logout() {
      // Ajoutez ici la logique pour déconnecter l'utilisateur.
      // Cela peut inclure l'effacement des informations d'authentification, la redirection vers la page de connexion, etc.
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
  margin-left: 10px;
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
  transition: color 0.3s; /* Animation de transition de la couleur du texte */
}

.navbar-link:hover {
  color: #ffcd00; /* Couleur du texte des liens au survol (personnalisez-la selon vos besoins) */
}

.logout-button {
  background-color: transparent; /* Fond du bouton transparent */
  border: none; /* Pas de bordure */
  color: #fff; /* Couleur du texte du bouton */
  font-size: 1rem; /* Taille du texte du bouton */
  cursor: pointer; /* Curseur en forme de main au survol */
  transition: background-color 0.3s, color 0.3s; /* Animation de transition de la couleur du texte et du fond du bouton */
}

.logout-button:hover {
  background-color: #fff; /* Fond du bouton au survol (personnalisez-la selon vos besoins) */
  color: #004F2D; /* Couleur du texte du bouton au survol (personnalisez-la selon vos besoins) */
}
</style>