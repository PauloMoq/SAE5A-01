<template>
  <div>
  <div class="background"></div>
  <div class="container">
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

    <select id="dropdown-list">
      <option value="">Sélectionnez une région</option>
      <option value="">lier à la BDD</option>
    </select>

    <button @click="getData" class="search-button">Rechercher</button>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newAuthor: '', // Auteur saisi
      newTitle: '', // Titre saisi
      newSupport: '',
      selectedAuthors: [], // Liste des auteurs sélectionnés
      selectedTitles: [], // Liste des titres sélectionnés
      selectedSupports: [], // Liste des titres sélectionnés
      startDate: '', // Date de début
      endDate: '' // Date de fin
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
    getData() {
      // Récupérer la liste des auteurs actuellement sélectionnés
      const authors = this.selectedAuthors;
      // const titles = this.selectedTitles;
      // const supports = this.selectedSupports;
      // const startDate = this.startDate;
      // const endDate = this.endDate;

      // Vérifier si la liste n'est pas vide
      if (authors.length > 0) {
        // Faites quelque chose avec la liste d'auteurs ici, par exemple, les afficher dans la console.
        alert("Liste des auteurs sélectionnés : " + authors);
      } else {
        // Si la liste est vide, mettez à jour le message en conséquence
        alert("Pas d'auteurs")
      }
    }
  }
};
</script>

<style scoped>
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
    z-index: -1; /* Place l'arrière-plan derrière les autres éléments */
}
.container {
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

.author-filter , .support-filter , .title-filter {
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

select {
  position: absolute;
  top:475px;
  left:70px;
  border-radius: 5px;
}
#DateDebut {
  position: absolute;
  top:475px;
  left:340px;
}
#startDate {
  position: absolute;
  top:470px;
  left:550px;
}
#endDate {
  position: absolute;
  top:470px;
  left:850px;
}
#DateFin {
  position: absolute;
  top:475px;
  left:685px;
}
#horloge1 {
  position: absolute;
  top:455px;
  left:805px
}
#horloge2 {
  position: absolute;
  top:455px;
  left:503px
}
.date-filter img{
 margin-top:15px;
 margin-right: 8px;
 margin-left:10px;
 width: 37px;
 height: 36px;
 color : white;
 background-color: #dcb253;
 border-top-left-radius: 5px;
 border-bottom-left-radius: 5px;
 padding: 4px;
}


.container h4, h1 {
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
  transition: 0.4s;
  background-color: #dcb253;
}

</style>