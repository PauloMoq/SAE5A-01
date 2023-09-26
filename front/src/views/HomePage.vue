<template>
  <div class="background"></div>
  <div class="home">
    <div class="hero">
      <div class="hero-content">
        <h1>Bienvenue sur notre site</h1>
        <p>La meilleure expérience culturelle vous attend.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
/* Styles spécifiques à la page Home */
/* Appliquez un style au conteneur du bandeau */
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
    z-index: -1; /* Place l'arrière-plan derrière les autres éléments */
}

/* Appliquez un style à l'image du bandeau */
.home {
  text-align: left;
  padding: 40px;
}

.hero-content {
  position: relative;
  max-width: 90%; /* Ajustez la largeur comme vous le souhaitez */
  margin: 0 auto;
}

h1 {
  font-size: 70px;
  margin-bottom: 10px;
}

p {
  font-size: 25px;
  color: #555;
}
</style>