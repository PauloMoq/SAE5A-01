<template >
  <div class="LoginPage">
    <!-- div background afin de mettre l'image de fond de la page -->
    <div class="background-login"></div>
    <div class="container">
      <div class="login form">
        <header>Connexion</header>
          <form action="#">
            <div class="input-container">
              <img src="../../assets/username.png" alt="Icône username">
              <input v-model="username" type="text" placeholder="Entrez votre pseudo">
            </div>
            <div class="input-container">
              <img src="../../assets/icon_cadena.png" alt="Icône mdp">
              <input v-model="password" type="password" placeholder="Entrez votre mot de passe">
            </div>
            <router-link to="/forgotPassword"><a href="#">Mot de passe oublié?</a></router-link>
            <input type="button" class="button" id="send" value="Se connecter" @click="login"> <!-- Appel la méthode login -->
          </form>
          <div class="signup">
            <span class="signup">Tu n'as pas de compte?
              <label for="check"><router-link to="/register">S'inscrire</router-link></label>
            </span>
          </div>
        </div>
    </div>
  </div>
</template>

<script src="./LoginPage.js"></script>
<style lang="scss" src="./LoginPage.scss"></style>