<template>
  <div>
    <div class="background"></div>
    <div class="container">
    <input type="checkbox" id="check">
    <div class="forgot form">
      <header>Mot de passe oublié</header>
      <form action="#">
        <div class="input-container">
          <img src="../assets/icon_mail.png" alt="Icône email">
          <input type="text" placeholder="Entrez votre email">
        </div>
        <input type="button" class="button" id="send" value="Envoyez un email">
      </form>
      <div class="login">
        <span class="login">Tu souhaite te connecter ?
         <label for="check"><router-link to="/login">Se connecter</router-link></label>
        </span>
      </div>
    </div>
  </div>
  </div>
  
</template>

<script>
export default {
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
#check:checked ~ .forgot{
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
 #send {
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px;
 }
 .form input:focus{
   box-shadow: 0 1px 0 rgba(0,0,0,0.2);
 }
.form a{
  font-size: 16px;
  color: #dcb253;
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
  background: #dcb253;
  font-size: 1.2rem;
  font-weight: 500;
  letter-spacing: 1px;
  margin-top: 15px;
  cursor: pointer;
  transition: 0.4s;
}
.form input.button:hover{
  background: #ffde92;
}
.login{
  font-size: 17px;
  text-align: center;
  color : white;
}
.login label{
  color: #dcb253;
  cursor: pointer;
}
.login label:hover{
  text-decoration: underline;
}
</style>