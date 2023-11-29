<template>
  <div class="RegisterPage">
    <!-- Arrière-plan avec une image du Louvre -->
    <div class="background-register"></div>

    <!-- Conteneur principal -->
    <div class="container">
          <!-- Formulaire d'inscription -->
      <div class="registration form">
        <header>S'inscrire</header>
        <form>
          <!-- Champ pour le pseudo -->
          <div class="input-container">
            <img src="../../assets/username.png" alt="Icône pseudo">
            <input v-model="username" type="text" placeholder="Entrez votre pseudo">
          </div>

          <!-- Champ pour le mot de passe -->
          <div class="input-container">
            <img src="../../assets/icon_cadena.png" alt="Icône mdp">
            <input v-model="password" type="password" placeholder="Créez votre mot de passe">
          </div>

          <!-- Champ pour confirmer le mot de passe -->
          <div class="input-container">
            <img src="../../assets/icon_cadena.png" alt="Icône mdp">
            <input v-model="confirmPassword" type="password" placeholder="Confirmez votre mot de passe">
          </div>

          <!-- Bouton pour soumettre le formulaire -->
          <input type="button" class="button" id="send" value="S'inscrire" @click="register">
        </form>

        <!-- Lien vers la page de connexion -->
        <div class="signup">
          <span class="signup">Tu as déjà un compte ?
            <router-link to="/login"><label for="check">Se connecter</label></router-link>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./RegisterPage.js"></script>
<style lang="scss" src="./RegisterPage.scss"></style>