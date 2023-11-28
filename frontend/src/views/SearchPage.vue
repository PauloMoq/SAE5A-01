<template>
  <div id="bg">
    <div class="background"></div>
    <div id="container">
      <h1>Recherchez des oeuvres d'arts</h1>
      
      <div class="author-filter">
        <h4>Auteurs</h4>
        <input type="text" v-model="newAuthor" @keydown.enter="addAuthor" placeholder="Ajouter un auteur">
        <button @click="addAuthor">+</button>
        <div v-if="selectedAuthors.length > 0">
          <ul>
            <li v-for="author in selectedAuthors" :key="author">
              {{ author }}
              <span @click="removeAuthor(author)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="title-filter">
        <h4>Titres</h4>
        <input type="text" v-model="newTitle" @keydown.enter="addTitle" placeholder="Ajouter un titre">
        <button @click="addTitle">+</button>
        <div v-if="selectedTitles.length > 0">
          <ul>
            <li v-for="title in selectedTitles" :key="title">
              {{ title }}
              <span @click="removeTitle(title)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="support-filter">
        <h4>Supports</h4>
        <input type="text" v-model="newSupport" @keydown.enter="addSupport" placeholder="Ajouter un support">
        <button @click="addSupport">+</button>
        <div v-if="selectedSupports.length > 0">
          <ul>
            <li v-for="support in selectedSupports" :key="support">
              {{ support }}
              <span @click="removeSupport(support)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="region-filter">
        <h4>Region</h4>
        <input type="text" v-model="newRegion" @keydown.enter="addRegion" placeholder="Ajouter une région">
        <button @click="addRegion">+</button>
        <div v-if="selectedRegions.length > 0">
          <ul>
            <li v-for="region in selectedRegions" :key="region">
              {{ region }}
              <span @click="removeRegion(region)" class="remove-button">x</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="date-filter">
        <div class="date-inputs">
          <h4 id="DateDebut" for="startDate">Date de début</h4>
          <img src="../assets/horloge.png" id="horloge1" alt="Icône horloge">
          <input  type="date" id="startDate" v-model="startDate">
          <h4 id="DateFin" for="endDate">Date de fin</h4>
          <img src="../assets/horloge.png" id="horloge2" alt="Icône horloge">
          <input  type="date" id="endDate" v-model="endDate">
        </div>
      </div>

      <div v-if="downloading" class="loading-overlay">
        <div class="loading-popup">
          <div class="loading-message">Téléchargement en cours...</div>
        </div>
      </div>

      <button @click="search" class="search-button">Rechercher</button>

    </div>
      <div id="myModal" class="modal">
          <p>Voici votre JSON : </p>
          <img src="../assets/logo_json.png" alt="Aperçu du fichier JSON">
          <button @click="downloadJSON">Télécharger</button>
      </div>
  </div>
  
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newAuthor: '', // Auteur saisi
      newTitle: '', // Titre saisi
      newSupport: '',
      newRegion: '',
      selectedAuthors: [], // Liste des auteurs sélectionnés
      selectedTitles: [], // Liste des titres sélectionnés
      selectedSupports: [], // Liste des titres sélectionnés
      selectedRegions: [], // Liste des titres sélectionnés
      startDate: '', // Date de début
      endDate: '', // Date de fin
      downloading: false,
      jsonResponse: null,
    };
  },
  methods: {
    addAuthor() {
      if (this.newAuthor.trim() !== '') {
        this.selectedAuthors.push(this.newAuthor);
        this.newAuthor = ''; // Réinitialisez la zone de texte
      }
    },
    addTitle() {
      if (this.newTitle.trim() !== '') {
        this.selectedTitles.push(this.newTitle);
        this.newTitle = ''; // Réinitialisez la zone de texte
      }
    },
    addSupport() {
      if (this.newSupport.trim() !== '') {
        this.selectedSupports.push(this.newSupport);
        this.newSupport = ''; // Réinitialisez la zone de texte
      }
    },
    addRegion() {
      if (this.newRegion.trim() !== '') {
        this.selectedRegions.push(this.newRegion);
        this.newRegion = ''; // Réinitialisez la zone de texte
      }
    },
    removeAuthor(author) {
      const index = this.selectedAuthors.indexOf(author);
      if (index !== -1) {
        this.selectedAuthors.splice(index, 1);
      }
    },
    removeTitle(title) {
      const index = this.selectedTitles.indexOf(title);
      if (index !== -1) {
        this.selectedTitles.splice(index, 1);
      }
    },
    removeSupport(support) {
      const index = this.selectedSupports.indexOf(support);
      if (index !== -1) {
        this.selectedSupports.splice(index, 1);
      }
    },
    removeRegion(region) {
      const index = this.selectedRegions.indexOf(region);
      if (index !== -1) {
        this.selectedRegions.splice(index, 1);
      }
    },
    search() {
      // Vérifiez que les champs obligatoires sont renseignés
      if (this.selectedAuthors.length === 0 && this.selectedTitles.length === 0 && this.selectedSupports.length === 0 && this.selectedRegions.length === 0) {
        alert('Veuillez sélectionner au moins un auteur, un titre ou un support.');
        return;
      }

      // construction de la requête avec les filtres
      // vérifier que startDate et endDate fonctionne 
      const query ={
        "date_debut": this.startDate[0],
        "date_fin": this.endDate[0],
        "artiste": this.selectedAuthors[0],
        "zone_geo": this.selectedRegions[0],
        "support": this.selectedSupports[0],
        "titre": this.selectedTitles[0]
      }

      // Affichez le message "Téléchargement en cours"
      this.downloading = true;

      // Envoyez la requête à l'API 
      axios.get('http://localhost:3000/getObjects', query)
        .then(response => {
          this.jsonResponse = response.data;
          console.log("ok")
        })
        .catch(error => {
          console.log(query)
          console.error('Erreur de recherche', error);
          alert('Une erreur s\'est produite lors de la recherche. Veuillez réessayer plus tard.');
        })
        .finally(() => {
          this.downloading = false;
          this.afficherModal()
          console.log("done")
        });
    },

    afficherModal() {
      // affichez le modal
      var modal = document.getElementById('myModal');
      modal.style.display = 'block';
      modal.style.opacity = "100%";

      // Ajoutez la classe au corps pour appliquer le style de fond gris
      var div = document.getElementById('container');
      div.classList.add('modal-open');
    },

    fermerModalSiClicExterieur(event) {
      var modal = document.getElementById('myModal');
      var div = document.getElementById('container');
      if (modal && event.target !== modal && !modal.contains(event.target)) {
        modal.style.display = 'none';
        div.classList.remove('modal-open');
      }
    },
  
    downloadJSON() {
      // utilisation de Blob pour créer un fichier JSON et créez un lien de téléchargement
      if (this.jsonResponse) {
        const blob = new Blob([JSON.stringify(this.jsonResponse)], { type: 'application/json' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'resultats_recherche.json';
        link.click();
      } else {
        alert('Aucune donnée à télécharger.');
      }
    },
  },
  mounted() {
    // Attachez l'événement de fermeture de la modal à la fenêtre lorsque le composant est monté
    window.onclick = this.fermerModalSiClicExterieur;
  }
};


</script>

<style scoped>
#myModal {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 400px;
    background: rgba(0, 66, 37, 1); /* Couleur de fond semi-transparente avec flou */
    height: 200px;
    border-radius: 20px;
    color: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Ajout de l'ombre */
}

#myModal img {
  filter: invert(100%); /* Inverser les couleurs de l'image (de noir à blanc) */
  width: 80px;
  height: 80px;
}
#myModal button {
  display: block;
  margin: auto;
  margin-top:10px;
}
#myModal p {
  margin-top:10px;
}
.background {
    background-image: url('../assets/searchpage.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    position: fixed;
    top: 0;
    left: 300;
    width: 100%;
    height: 100%;
}

.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Couleur de fond semi-transparente */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    border-radius: 7px;
  }

  .loading-popup {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }

  .loading-message {
    text-align: center;
  }

#container {
  transition:0.5s;
  position: absolute;
  top: 53%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 1300px;
  height: 70%;
  width: 100%;
  background: rgba(0, 66, 37, 0.8); /* Couleur de fond semi-transparente avec flou */
  border-radius: 7px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(7px); /* Effet de flou */
}
h1 {
  margin-top: 80px;
  font-size: 30px;
  text-align: left;
  margin-left: 20px; 
}
/* Style de la croix de suppression */
.remove-button {
  margin-left: 5px;
  cursor: pointer;
  color: rgb(0, 0, 0);
  font-weight: bold;
}

.author-filter , .support-filter , .title-filter, .region-filter{
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  width:400px;
  border-radius: 5px;
  text-align: left;
  margin-left: 10px;
}
.author-filter {
  position: absolute;
  top: 90px;
}
.title-filter {
  position: absolute;
  top: 90px;
  left: 450px;
}
.support-filter {
  position: absolute;
  top: 90px;
  left: 900px;
}

.region-filter {
  position: absolute;
  top: 300px;
  left: 0px;
}

#DateDebut {
  position: absolute;
  top:360px;
  left:480px;
}
#startDate {
  position: absolute;
  top:352px;
  left:700px;
  font-size: 19px;
}
#horloge1 {
  position: absolute;
  top:337px;
  left:65 0px
}

#DateFin {
  position: absolute;
  top:360px;
  left:950px;
}
#endDate {
  position: absolute;
  top:352px;
  left:1140px;
  font-size: 19px;
}
#horloge2 {
  position: absolute;
  top:337px;
  left:1090px
}

.date-filter img{
 margin-top:15px;
 margin-right: 8px;
 margin-left:10px;
 width: 42px;
 height: 42px;
 color : white;
 background-color: #dcb253;
 border-top-left-radius: 5px;
 border-bottom-left-radius: 5px;
 padding: 4px;
}


#container h4, h1 {
  color: #f5f5f5;
}
h1 {
  margin-top : 30px;
  font-size: 40px;
}

.date-inputs input {
  width: 115px;
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;

}
.date-inputs label {
  color:#f5f5f5;
}
/* champ input pour auteur */
input {
  width: 81%;
  padding: 5px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

/* button ajouter auteur */
button {
  padding: 5px 10px;
  border: 1px solid #727272;
  border-radius: 5px;
  background-color: #dcb253;
  color: #fff;
  cursor: pointer;
}

/* enleve mes bullets points */
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

/* css des auteurs dans la liste */
li {
  margin-top: 10px;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px;
  display: inline-block;
  margin-right: 10px;
}

/* Style du bouton de recherche */
.search-button {
  position: absolute;
  background-color: #dcb253;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 20px;
  cursor: pointer;
  margin-top: 20px;
  top:445px;
  left: 1100px;
}

.search-button:hover {
  transition: 0.5s;
  background-color: #ffd575;
  color : black
}
.modal-open {
  width: 100%;
  height: 100%;
  overflow: hidden;    
  opacity: 0.8; /* Ajoutez l'opacité que vous souhaitez */
  transition : 0.5s;
}
</style>