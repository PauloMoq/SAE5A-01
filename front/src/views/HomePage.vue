<template>
  <img id="banner-image" src="../assets/Louvre-Museum-Paris.webp" alt="">
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
#banner-image {
  width: 100%; /* La largeur de l'image occupera 100% de la largeur de son conteneur */
  height: auto; /* La hauteur s'ajustera automatiquement pour conserver les proportions d'origine de l'image */
  object-fit: cover; /* L'image sera ajustée pour couvrir complètement le conteneur */
  margin : 0;
}
.home {
  text-align: left;
  padding: 40px;
}

.hero-content {
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
