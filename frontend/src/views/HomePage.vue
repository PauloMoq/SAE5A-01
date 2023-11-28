<template>
  <div>
    <div class="background"></div>
    <div class="home">
      <div class="hero">
        <div class="hero-content">
          <h1>Bienvenue sur notre site</h1>
          <p id="description">La meilleure expérience culturelle vous attend.</p>
        </div>

        <div class="container-application">
          <h4>Téléchargez notre application!</h4>
          <p>Notre application vous permettra de récupérer vos données à partir de votre fichier json.</p>
          <a href="" download="MushRoomPy.exe" id="button_dl">
            <img src="../assets/telecharger.png" alt="logo telecharger">
            Télécharger
          </a>
        </div>
        
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
    transform: scaleX(-1); /* Inverser horizontalement */
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
  margin-top: 30px;
  font-size: 70px;
  margin-bottom: 10px;
}

#description {
  font-size: 21px;
}
.container-application {
  position: absolute;
  width: 330px;
  height: 250px;
  bottom: 50px;
  right: 50px;
  text-align: center;
  color :white;
  background: rgba(0, 66, 37, 0.8); /* Couleur de fond semi-transparente avec flou */
  border-radius: 7px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(7px); /* Effet de flou */
}

.container-application h4{
  padding: 10px;
}
.container-application p {
  text-align: left;
  margin-left: 25px;
}

.container-application img {
  width: 30px;
  height: 30px;
}

#button_dl {
  padding-top:10px ;
  display: block;
  border-radius: 7px;
  background-color: #dcb253;
  width: 160px;
  height: 50px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 25px;
  font-size: 18px;
  text-decoration: none;
  color: white;
}
</style>