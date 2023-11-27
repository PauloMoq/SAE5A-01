<template>
    <div class="background">
        <div id="container">
            <h1>Historique de recherche</h1>
            <div class="file-info">
                <p id="title-info">Fichier publié :</p>
                <p class ="name-info" v-if="fichierAjoute">{{ nomFichier }}</p>
                <p class ="name-info" v-else>Aucun fichier</p>
            </div>
            <button id="add-file" @click="ouvrirModal"><img src="@/assets/add-file.png" alt="Ajouter un fichier"/></button>            
            <button class="search-button">Rechercher</button>
        </div>
        <div v-show="modalVisible" class="modal">
            <div class="modal-content">
                <span class="close" @click="fermerModal">&times;</span>
                <p>Glissez et déposez votre fichier JSON ici :</p>
                <div class="dropArea" @dragenter.prevent @dragover.prevent @dragleave.prevent @drop.prevent="handleDrop" @click="ouvrirGestionnaireFichiers" accept=".json">
                    <template v-if="!fichierAjoute">
                        <p class="plus">+</p>
                    </template>
                    <template v-else>
                        <p class="fichier_ajouter">✓</p>
                        <p class="fichier_ajouter">{{ nomFichier }}</p>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
  data() {
    return {
      modalVisible: false,
      fichierAjoute: false,
      nomFichier: null,
    };
  },
  methods: {
    ouvrirModal() {
      this.modalVisible = true;
    },
    fermerModal() {
      this.modalVisible = false;
    },
    handleDrop(event) {
      // Gérer le glisser-déposer ici
      const fichier = event.dataTransfer.files[0];
      console.log('Fichier déposé:', fichier);

      if (fichier && fichier.type === 'application/json') {
        // Vérifier le type de fichier pour s'assurer qu'il s'agit d'un fichier JSON
        this.fichierAjoute = true;
        this.nomFichier = fichier.name;
        // Vous pouvez ajouter le code pour traiter le fichier ici
      } else {
        alert('Veuillez déposer un fichier JSON.');
      }
    },
    ouvrirGestionnaireFichiers() {
      // Ouvrir le gestionnaire de fichiers lorsqu'on clique sur la div
      const input = document.createElement('input');
      //const button = document.getElementById('button-publier');
      input.type = 'file';
      input.accept = '.json'; // Spécifiez les types de fichiers autorisés si nécessaire
      input.addEventListener('change', (event) => {
        const fichier = event.target.files[0];
        console.log('Fichier sélectionné:', fichier);
        this.fichierAjoute = true;
        this.nomFichier = fichier.name;

        //if (button && button.dataset.publierPresse == 'true') {
        //}
      });
      input.click();
    },
  },
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
}
  
  #container {
    display: block;
    transition:0.5s;
    position: absolute;
    top: 53%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 1350px;
    height: 80%;
    width: 100%;
    background: rgba(0, 66, 37, 0.8); /* Couleur de fond semi-transparente avec flou */
    border-radius: 7px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(7px); /* Effet de flou */
  }

  h1 {
    margin-top : 30px;
    font-size: 40px;
    text-align: left;
    margin-left: 20px; 
  }

  #container h4, h1 {
    color: #f5f5f5;
  }

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
    bottom:30px;
    right: 30px;
  }
  .search-button:hover {
    transition: 0.5s;
    background-color: #ffd575;
    color : black
  }

  .modal {
  display: block;
  position: fixed;
  top: 50%; /* Centrer verticalement */
  left: 50%; /* Centrer horizontalement */
  width: 40%; /* 40% de la largeur de la page */
  height: 40%; /* 40% de la hauteur de la page */
  transform: translate(-50%, -50%); /* Ajuster le centrage après le dimensionnement */
}

.modal-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  cursor: pointer;
}

.dropArea {
  padding: 20px;
  text-align: center;
  cursor: pointer;
  margin-top: 20px;
  border-radius: 5px;
  border: 2px dashed #b4b4b4;
}

.plus {
  font-size: 50px;
  margin: 0;
}
.fichier_ajouter {
    font-size: 22px;
}

.file-info {
    position: absolute;
    align-items: center;
    top: 33px;
    right: 130px;
}

.file-info p {
  margin: 0;
  color: #ffffff; /* Couleur du texte */
  font-size: 18px;
}
#title-info {
    font-weight: bold;
}
#add-file {
    position: absolute;
    top: 20px; /* Ajuster la marge par rapport au haut du conteneur */
    right: 20px; 
    background-color: #dcb253; /* Couleur grise pour le fond */
    border: none;
    cursor: pointer;
    border-radius: 50%; /* Rend le bouton rond */
    padding: 15px; /* Ajuste la taille du bouton en fonction de vos préférences */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.8); /* Ajout de l'ombre */
    transition : 0.4s;
}

#add-file img {
  width: 50px; /* Ajuster la taille de l'image en fonction de vos préférences */
}

#add-file:hover {
  background-color: #ffdf96; /* Effet d'ombre au survol */
}
#button-publier {
    margin-top : 20px
}
</style>
