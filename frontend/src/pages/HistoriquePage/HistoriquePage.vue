<template>
  <!-- div background afin de mettre l'image de fond de la page -->
  <div class="HistoriquePage">
    <div id="container">
      <h1>Historique de recherche</h1>
      <div class="file-info">
        <p id="title-info">Fichier publié :</p>
        <p class="name-info" v-if="fichierAjoute">{{ nomFichier }}</p>
        <!-- Affiche le nom du fichier si un fichier est ajouté -->
        <p class="name-info" v-else>Aucun fichier</p>
      </div>
      <button id="add-file" @click="ouvrirModal">
        <img src="@/assets/add-file.png" alt="Ajouter un fichier" />
      </button>
      <!-- Bouton pour ouvrir la modal d'ajout de fichier -->
      <p id="avertissement">
        Cette fonctionnalité n'est pas encore disponible.
      </p>
    </div>

    <!-- Modal pour ajouter un fichier -->
    <div v-show="modalVisible" class="modal">
      <div class="modal-content">
        <span class="close" @click="fermerModal">&times;</span>
        <!-- Bouton pour fermer la modal -->
        <p>Glissez et déposez votre fichier JSON ici :</p>

        <!-- Zone de glisser-déposer pour ajouter un fichier -->
        <div
          class="dropArea"
          @dragenter.prevent
          @dragover.prevent
          @dragleave.prevent
          @drop.prevent="handleDrop"
          @click="ouvrirGestionnaireFichiers"
          accept=".json"
        >
          <!-- Affiche un "+" si aucun fichier n'est ajouté -->
          <template v-if="!fichierAjoute">
            <p class="plus">+</p>
          </template>
          <!-- Affiche une coche et le nom du fichier si un fichier est ajouté -->
          <template v-else>
            <p class="fichier_ajouter">✓</p>
            <p class="fichier_ajouter">{{ nomFichier }}</p>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./HistoriquePage.js"></script>
<style lang="scss" src="./HistoriquePage.scss"></style>
