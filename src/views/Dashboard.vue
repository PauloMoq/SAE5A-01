<template>
    <div>
      <h2>Tableau de bord</h2>
      <p>Bienvenue dans votre tableau de bord.</p>
      <!-- Contenu du tableau de bord -->
      <button @click="logout">Déconnexion</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        // Ajoutez ici la logique pour déconnecter l'utilisateur.
        // Cela peut inclure l'effacement des informations d'authentification, la redirection vers la page de connexion, etc.
      },
    },
  };
  </script>
  