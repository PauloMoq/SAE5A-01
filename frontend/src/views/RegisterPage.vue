<template>
  <div>
    <!-- Arrière-plan avec une image du Louvre -->
    <div class="background"></div>

    <!-- Conteneur principal -->
    <div class="container">
      <!-- Checkbox pour activer/désactiver le formulaire -->
      <input type="checkbox" id="check">

          <!-- Formulaire d'inscription -->
      <div class="registration form">
        <header>S'inscrire</header>
        <form>
          <!-- Champ pour le pseudo -->
          <div class="input-container">
            <img src="../assets/username.png" alt="Icône pseudo">
            <input v-model="username" type="text" placeholder="Entrez votre pseudo">
          </div>

          <!-- Champ pour le mot de passe -->
          <div class="input-container">
            <img src="../assets/icon_cadena.png" alt="Icône mdp">
            <input v-model="password" type="password" placeholder="Créez votre mot de passe">
          </div>

          <!-- Champ pour confirmer le mot de passe -->
          <div class="input-container">
            <img src="../assets/icon_cadena.png" alt="Icône mdp">
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

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    register() {
      // confirm pas définis car je le vérif ici et j'envoe pas sur postman
      if (this.password != this.confirmPassword) {
        Swal.fire("Erreur !", "Les mots de passes sont différents.", "error");
      }
      else {
        axios.post('http://localhost:3000/auth/register', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          console.log(response)
          this.$router.push('/login');
        })
        .catch(error => {
          console.log(error)
          if (error.response) {
            // Récupérer le message d'erreur de la réponse JSON
            if (error.response.data && error.response.data.error) {
              Swal.fire("Erreur !", error.response.data.error, "error");
            } else {
              Swal.fire("Erreur !", 'Une erreur inattendue s\'est produite.', "error");
            }
          } else if (error.request) {
            // La requête a été faite, mais aucune réponse n'a été reçue
            console.log(error.request);
          } else {
            // Une erreur s'est produite lors de la configuration de la requête
            console.log('Error', error.message);
          }
          console.log(error.config); // La configuration de la requête qui a déclenché l'erreur
        });
      }
    },
  },
};
</script>

<style scoped>
/* Styles CSS spécifiques à ce composant */

.background {
  /* Styles pour l'arrière-plan avec une image du Louvre */
  background-image: url('../assets/Louvre_Cour_Carree.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  position: fixed;
  top: 0;
  left: 300;
  width: 100%;
  height: 100%;
  z-index: -1;
  /* Place l'arrière-plan derrière les autres éléments */
}

/* Styles pour les conteneurs d'entrée */
.input-container {
  display: flex;
  /* Utilisez flexbox pour aligner horizontalement */
  justify-content: center;
  /* Centre les éléments horizontalement */
  background-color: #dcb253;
  height: 60px;
  margin-bottom: 20px;
  border-radius: 10px;
}

.input-container img {
  /* Styles pour les images dans les champs */
  margin-top: 15px;
  margin-right: 8px;
  margin-left: 10px;
  width: 30px;
  height: 30px;
  color: white;
}

/* Styles globaux */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  /* Styles pour le corps du document */
  min-height: 100vh;
  width: 100%;
  background: #009579;
}

.container {
  /* Styles pour le conteneur principal */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 430px;
  width: 100%;
  background: rgba(0, 66, 37, 0.8);
  /* Couleur de fond semi-transparente avec flou */
  border-radius: 7px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(7px);
  /* Effet de flou */
}

#check {
  display: none;
  /* Cache la checkbox par défaut */
}

.container .form {
  /* Styles pour le formulaire d'inscription */
  padding: 2rem;
}

.form header {
  /* Styles pour l'en-tête du formulaire */
  font-size: 2rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 1.5rem;
  color: white;
}

.form input {
  /* Styles pour les champs de saisie */
  height: 60px;
  width: 100%;
  padding: 0 15px;
  font-size: 17px;
  margin-bottom: 1.3rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  outline: none;
}

#send {
  /* Styles pour le bouton d'envoi */
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px;
}

.form input:focus {
  /* Styles pour le champ de saisie lorsqu'il est en focus */
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.2);
}

.form a {
  /* Styles pour les liens dans le formulaire */
  font-size: 16px;
  color: #009579;
  text-decoration: none;
}

.form a:hover {
  /* Styles pour les liens survolés */
  text-decoration: underline;
}

.form input.button {
  /* Styles pour le bouton du formulaire */
  color: #000000;
  background: #dcb253;
  border: none;
  font-size: 1.2rem;
  font-weight: 500;
  letter-spacing: 1px;
  margin-top: 10px;
  cursor: pointer;
  transition: 0.4s;
}

.form input.button:hover {
  /* Styles pour le bouton du formulaire au survol */
  background: #ffffff;
}

.signup {
  /* Styles pour la section "Tu as déjà un compte ?" */
  font-size: 17px;
  text-align: center;
  color: white;
}

.signup label {
  /* Styles pour le lien "Se connecter" dans la section "Tu as déjà un compte ?" */
  color: #dcb253;
  cursor: pointer;
}

.signup label:hover {
  /* Styles pour le lien "Se connecter" survolé */
  text-decoration: underline;
}</style>
