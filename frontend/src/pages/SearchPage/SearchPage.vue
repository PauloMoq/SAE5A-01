<template>
  <div class="SearchPage">
    <!-- div background afin de mettre l'image de fond de la page -->
    <div class="background-search"></div>
    <div id="container">
      <h1>Recherchez des oeuvres d'arts</h1>
      
      <!-- Champ pour ajouter un filtre auteur-->
      <div class="author-filter">
        <h4>Auteurs</h4>
        <input type="text" v-model="newAuthor" @keydown.enter="addAuthor" placeholder="Ajouter un auteur">
        <button class="add-button" @click="addAuthor">+</button>
        <div v-if="selectedAuthors.length > 0">
          <ul>
            <li v-for="author in selectedAuthors" :key="author">
              {{ author }}
              <span @click="removeAuthor(author)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Champ pour ajouter un filtre titre -->
      <div class="title-filter">
        <h4>Titres</h4>
        <input type="text" v-model="newTitle" @keydown.enter="addTitle" placeholder="Ajouter un titre">
        <button class="add-button" @click="addTitle">+</button>
        <div v-if="selectedTitles.length > 0">
          <ul>
            <li v-for="title in selectedTitles" :key="title">
              {{ title }}
              <span @click="removeTitle(title)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Champ pour ajouter un filtre support -->
      <div class="support-filter">
        <h4>Supports</h4>
        <input type="text" v-model="newSupport" @keydown.enter="addSupport" placeholder="Ajouter un support">
        <button class="add-button" @click="addSupport">+</button>
        <div v-if="selectedSupports.length > 0">
          <ul>
            <li v-for="support in selectedSupports" :key="support">
              {{ support }}
              <span @click="removeSupport(support)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Champ pour ajouter un filtre région -->
      <div class="region-filter">
        <h4>Region</h4>
        <input type="text" v-model="newRegion" @keydown.enter="addRegion" placeholder="Ajouter une région">
        <button class="add-button" @click="addRegion">+</button>
        <div v-if="selectedRegions.length > 0">
          <ul>
            <li v-for="region in selectedRegions" :key="region">
              {{ region }}
              <span @click="removeRegion(region)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Champ pour ajouter un filtre année de début et fin-->
      <div class="date-filter">
        <div class="date-inputs">
          <h4 id="DateDebut" for="startDate">Année de début</h4>
          <img src="../../assets/horloge.png" id="horloge1" alt="Icône horloge">
          <input id="startDate" type="text" placeholder="1200" @input="updateStartDate" maxlength="4" oninput="this.value=this.value.replace(/[^0-9]/g,'')" pattern="[0-9]*"> 
          <h4 id="DateFin" for="endDate">Année de fin</h4>
          <img src="../../assets/horloge.png" id="horloge2" alt="Icône horloge">
          <input id="endDate" type="text" placeholder="2023" @input="updateEndDate" maxlength="4" oninput="this.value=this.value.replace(/[^0-9]/g,'')" pattern="[0-9]*">
        </div>
      </div>

      <!-- Pop up qui annonce qu'un téléchargement est en cours -->
      <div v-if="downloading" class="loading-overlay">
        <div class="loading-popup">
          <div class="loading-message">Téléchargement en cours...</div>
        </div>
      </div>

      <button @click="search" class="search-button">Rechercher</button>

    <!-- Modal qui s'affiche pour télécharger le JSON -->
    </div>
      <div id="myModal" class="modal">
          <p>Voici votre JSON : </p>
          <img src="../../assets/logo_json.png" alt="Aperçu du fichier JSON">
          <button @click="downloadJSON">Télécharger</button>
      </div>
  </div>
</template>

<script src="./SearchPage.js"></script>
<style lang="scss" src="./SearchPage.scss"></style>