<template>
   <div class="container">
    <input type="checkbox" id="check">
    <div class="Password_Form">
      <header>Mot de passe oublié</header>
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

</style>