<template>
  <div>
    <div class="background"></div>
    <div class="container">
      <input type="checkbox" id="check">
      <div class="registration form">
        <header>S'inscrire</header>
        <form action="#">
          <div class="input-container">
            <img src="../assets/icon_mail.png" alt="Icône email">
            <input type="text" placeholder="Entrez votre email">
          </div>
          <div class="input-container">
            <img src="../assets/icon_cadena.png" alt="Icône mdp">
            <input type="password" placeholder="Créez votre mot de passe">
          </div>
          <div class="input-container">
            <img src="../assets/icon_cadena.png" alt="Icône mdp">
            <input type="password" placeholder="Confirmez votre mot de passe">
          </div>
          <input type="button" class="button" id="send" value="S'inscrire" @click="register()">
        </form>
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
export default {
  data() {
    return {
      firstname: '',
      lastname: '',
      email: '',
    };
  },
  methods: {
    register() {
      // Ajoutez ici la logique d'inscription, y compris la validation du mot de passe et de la confirmation.
      /* if (this.password !== this.confirmPassword) {
        alert("Le mot de passe et la confirmation du mot de passe ne correspondent pas.");
        return;
      } */
      this.$swal({
        text:"Le mot de passe n'est pas le même que dans le champ de confirmation.",
        icon:'error'
      })
      // Le reste de la logique d'inscription...
    },
  },
};
</script>


<style scoped>
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
    z-index: -1; /* Place l'arrière-plan derrière les autres éléments */
}

.input-container {
 display: flex; /* Utilisez flexbox pour aligner horizontalement */
 justify-content: center; /* Centre les éléments horizontalement */
 background-color: #dcb253;
 height: 60px;
 margin-bottom: 20px;
 border-radius:10px;
}
.input-container img{
 margin-top:15px;
 margin-right: 8px;
 margin-left:10px;
 width: 30px;
 height: 30px;
 color : white;
}
*{
 margin: 0;
 padding: 0;
 box-sizing: border-box;
 font-family: 'Poppins', sans-serif;
}
body{
 min-height: 100vh;
 width: 100%;
 background: #009579;
}
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 430px;
    width: 100%;
    background: rgba(0, 66, 37, 0.8); /* Couleur de fond semi-transparente avec flou */
    border-radius: 7px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(7px); /* Effet de flou */
}
#check{
 display: none;
}
.container .form{
 padding: 2rem;
}
.form header{
 font-size: 2rem;
 font-weight: 500;
 text-align: center;
 margin-bottom: 1.5rem;
 color : white;
}
.form input{
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
 border-top-left-radius: 6px;
 border-bottom-left-radius: 6px;
}
.form input:focus{
  box-shadow: 0 1px 0 rgba(0,0,0,0.2);
}
.form a{
 font-size: 16px;
 color: #009579;
 text-decoration: none;
}
.form a:hover{
 text-decoration: underline;
}
.form input.button{
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
.form input.button:hover{
 background: #ffffff;
}
.signup{
 font-size: 17px;
 text-align: center;
 color : white;
}
.signup label{
 color: #dcb253;
 cursor: pointer;
}
.signup label:hover{
 text-decoration: underline;
}
</style>