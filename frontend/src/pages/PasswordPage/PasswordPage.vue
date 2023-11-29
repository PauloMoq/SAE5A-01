<template>
  <!-- Conteneur principal -->
  <div class="PasswordPage">
    <!-- Arrière-plan avec une image du Louvre -->
    <div class="background-password"></div>
    <div class="container">
      <!-- Formulaire de récupération de mot de passe -->
      <div class="forgot form">
        <header>Mot de passe oublié</header>
        <form action="#">
          <!-- Champ pour l'email -->
          <div class="input-container">
            <img src="../../assets/icon_mail.png" alt="Icône email">
            <input type="text" placeholder="Entrez votre email">
          </div>

          <!-- Bouton pour envoyer l'email de récupération -->
          <input type="button" class="button" id="send" value="Envoyez un email">
        </form>

        <!-- Lien pour se connecter -->
        <div class="login">
          <span class="login">Tu souhaites te connecter ?
            <label for="check"><router-link to="/login">Se connecter</router-link></label>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./PasswordPage.js"></script>
<style lang="scss" src="./PasswordPage.scss"></style>
