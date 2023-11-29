<template>
  <div class="HomePage">
    <!-- div background afin de mettre l'image de fond de la page -->
    <div class="background-home"></div>
    <div class="home">
      <div class="hero">
        <div class="hero-content">
          <h1>Bienvenue sur notre site</h1>
          <p id="description">
            La meilleure expérience culturelle vous attend.
          </p>
        </div>

        <!-- Container ou l'on peut télécharger l'application -->
        <div class="container-application">
          <h4><b>Téléchargez notre application</b></h4>
          <p>
            Notre application vous permettra de récupérer vos données à partir
            de votre fichier JSON.
          </p>
          <!-- lien vers l'appli sur le github -->
          <a
            href="https://github.com/Moquequette/SAE5A-01/raw/main/Appli_Python/MushRoomPy/MushRoomPy.exe"
            download="MushRoomPy.exe"
            id="button_dl"
          >
            <img src="../../assets/telecharger.png" alt="logo telecharger" />
            Télécharger
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./HomePage.js"></script>
<style lang="scss" src="./HomePage.scss"></style>
