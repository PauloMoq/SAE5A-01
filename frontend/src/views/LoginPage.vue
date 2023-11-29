<template>
  <div>
    <div class="background"></div>
    <div class="container">
      <input type="checkbox" id="check">
      <div class="login form">
        <header>Connexion</header>
          <form action="#">
            <div class="input-container">
              <img src="../assets/username.png" alt="Icône username">
              <input v-model="username" type="text" placeholder="Entrez votre pseudo">
            </div>
            <div class="input-container">
              <img src="../assets/icon_cadena.png" alt="Icône mdp">
              <input v-model="password" type="password" placeholder="Entrez votre mot de passe">
            </div>
            <router-link to="/forgotPassword"><a href="#">Mot de passe oublié?</a></router-link>
            <input type="button" class="button" id="send" value="Se connecter" @click="login">
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

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  props: ['updateAuthentication'],
  data() {
    return {
      username: '',
      password: '',
      errorMessage: null,  // Variable pour stocker le message d'erreur
    };
  },
  methods: {
    login() {
      axios.post('http://localhost:3000/auth/login', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          console.log(response)
          this.updateAuthentication({
            isAuthenticated: true,
            username: this.username,
          });          
          this.$router.push('/');
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
    },
  },
};
</script>

<style scoped>/* Style pour le titre du message */

.background {
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

.container {
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
  margin-top: 15px;
  margin-right: 8px;
  margin-left: 10px;
  width: 30px;
  height: 30px;
  color: white;
}

.container .registration {
  display: none;
}

#check:checked~.registration {
  display: block;
}

#check:checked~.login {
  display: none;
}

#check {
  display: none;
}

.container .form {
  padding: 2rem;
}

.form header {
  font-size: 2rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 1.5rem;
  color: white;
}

.form input {
  height: 60px;
  width: 90%;
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
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px;
}

.form input:focus {
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.2);
}

.form a {
  font-size: 16px;
  color: #dcb253;
  text-decoration: none;
}

.form a:hover {
  text-decoration: underline;
}

.form input.button {
  width: 100%;
  margin-left: 0px;
  color: #000000;
  border: none;
  background: #dcb253;
  font-size: 1.2rem;
  font-weight: 500;
  letter-spacing: 1px;
  margin-top: 15px;
  cursor: pointer;
  transition: 0.4s;
}

.form input.button:hover {
  background: #ffde92;
}

.signup {
  font-size: 17px;
  text-align: center;
  color: white;
}

.signup label {
  color: #dcb253;
  cursor: pointer;
}

.signup label:hover {
  text-decoration: underline;
}
</style>