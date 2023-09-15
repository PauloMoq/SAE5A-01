<template>
  <div class="container">
    <input type="checkbox" id="check">
    <div class="login form">
      <header>Connexion</header>
      <form action="#">
        <div class="input-container">
          <img src="../assets/icon_mail.png" alt="Icône email">
          <input type="text" placeholder="Entrez votre email">
        </div>
        <div class="input-container">
          <img src="../assets/icon_cadena.png" alt="Icône mdp">
          <input type="password" placeholder="Entrez votre mot de passe">
        </div>
        <a href="#">Mot de passe oublié?</a>
        <input type="button" class="button" value="Se connecter">
      </form>
      <div class="signup">
        <span class="signup">Tu n'as pas de compte?
         <label for="check"><router-link to="/register">S'inscrire</router-link></label>
        </span>
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
     password: '',
     confirmPassword: '', // Champ pour la confirmation du mot de passe
   };
 },
 methods: {
   register() {
     // Ajoutez ici la logique d'inscription, y compris la validation du mot de passe et de la confirmation.
     if (this.password !== this.confirmPassword) {
       alert("Le mot de passe et la confirmation du mot de passe ne correspondent pas.");
       return;
     }
     // Le reste de la logique d'inscription...
   },
 },
};
</script>

<style scoped>
.input-container {
  display: flex; /* Utilisez flexbox pour aligner horizontalement */
  justify-content: center; /* Centre les éléments horizontalement */
  background-color: #ffcd00;
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
.container{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  max-width: 430px;
  width: 100%;
  background: #004225;
  border-radius: 7px;
  box-shadow: 0 5px 10px rgba(0,0,0,0.3);
}
.container .registration{
  display: none;
}
#check:checked ~ .registration{
  display: block;
}
#check:checked ~ .login{
  display: none;
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
  color: white;
}
 .form input{
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
 .form input:focus{
   box-shadow: 0 1px 0 rgba(0,0,0,0.2);
 }
.form a{
  font-size: 16px;
  color: #ffcd00;
  text-decoration: none;
}
.form a:hover{
  text-decoration: underline;
}
.form input.button{
  width: 100%;
  margin-left:0px;
  color: #000000;
  border: none;
  background: #ffcd00;
  font-size: 1.2rem;
  font-weight: 500;
  letter-spacing: 1px;
  margin-top: 15px;
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
  color: #ffcd00;
  cursor: pointer;
}
.signup label:hover{
  text-decoration: underline;
}
</style>