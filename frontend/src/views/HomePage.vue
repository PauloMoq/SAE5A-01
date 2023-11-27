<template>
  <div>
    <!-- Image de fond de la page -->
    <div class="background"></div>
    <div class="home">
      <div class="hero">
        <div class="hero-content">
          <!-- Titre principal de la page d'accueil -->
          <h1>Bienvenue sur notre site</h1>
          <!-- Description de la page d'accueil -->
          <p>La meilleure expérience culturelle vous attend.</p>

          <!-- Invitation à télécharger l'application -->
          <p>Telecharger notre application afin de telecharger les données :</p>
          <button>Télécharger</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage', // Nom du composant
};
</script>

<style scoped>
/* Styles spécifiques à la page Home */
/* Style pour l'image de fond */
.background {
  background-image: url('../assets/test.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  /* Place l'arrière-plan derrière les autres éléments */
  transform: scaleX(-1);
  /* Inverser horizontalement */
}

/* Styles pour le conteneur principal */
.home {
  text-align: left;
  padding: 40px;
}

/* Styles pour le contenu principal (hero) */
.hero-content {
  position: relative;
  max-width: 90%;
  margin: 0 auto;
}

/* Style pour le titre principal */
h1 {
  margin-top: 30px;
  font-size: 70px;
  margin-bottom: 10px;
}

/* Style pour les paragraphes de description */
p {
  font-size: 25px;
  color: #555;
}
</style>
