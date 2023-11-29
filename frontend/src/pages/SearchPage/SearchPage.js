import NavbarPage from './../../components/Navbar/NavbarPage.vue';
import axios from 'axios';

export default {
    components: {
        NavbarPage
    },
  data() {
    return {
      newAuthor: '', 
      newTitle: '', 
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
    // Cette version n'accepte qu'un seul filtre max par catégorie, si vous voulez en mettre plus, 
    // enleve le deuxieme if des méthodes add et ajustez le reste du code. 
    addAuthor() {
      if (this.newAuthor.trim() !== '') {
        if (this.selectedAuthors.length < 1) { 
          this.selectedAuthors.push(this.newAuthor);
          this.newAuthor = ''; // Réinitialise la zone de texte
        } else {
          alert('Vous ne pouvez ajouter qu\'un auteur.');
        }
      }
    },
    // méthode pour ajouter un titre
    addTitle() {
      if (this.newTitle.trim() !== '') {
        if (this.selectedTitles.length < 1) {
          this.selectedTitles.push(this.newTitle);
          this.newTitle = ''; // Réinitialise la zone de texte
        } else {
          alert('Vous ne pouvez ajouter qu\'un titre.');
        }
      }
    },
    // méthode pour ajouter un support
    addSupport() {
      if (this.newSupport.trim() !== '') {
        if (this.selectedSupports.length < 1) {
          this.selectedSupports.push(this.newSupport);
          this.newSupport = ''; // Réinitialise la zone de texte
        } else {
          alert('Vous ne pouvez ajouter qu\'un support.');
        }
      }
    },
    // méthode pour ajouter une région
    addRegion() {
      if (this.newRegion.trim() !== '') {
        if (this.selectedRegions.length < 1) {
          this.selectedRegions.push(this.newRegion);
          this.newRegion = ''; // Réinitialise la zone de texte
        } else {
          alert('Vous ne pouvez ajouter qu\'une région.');
        }
      }
    },
    // méthode pour supprimer un auteur
    removeAuthor(author) {
      const index = this.selectedAuthors.indexOf(author);
      if (index !== -1) {
        this.selectedAuthors.splice(index, 1);
      }
    },
    // méthode pour supprimer un titre
    removeTitle(title) {
      const index = this.selectedTitles.indexOf(title);
      if (index !== -1) {
        this.selectedTitles.splice(index, 1);
      }
    },
    // méthode pour supprimer un support
    removeSupport(support) {
      const index = this.selectedSupports.indexOf(support);
      if (index !== -1) {
        this.selectedSupports.splice(index, 1);
      }
    },
    // méthode pour supprimer une région
    removeRegion(region) {
      const index = this.selectedRegions.indexOf(region);
      if (index !== -1) {
        this.selectedRegions.splice(index, 1);
      }
    },
    // méthode pour mettre à jour le champ date début
    updateStartDate(event) {
      this.startDate = [event.target.value];
    },
    // méthode pour mettre à jour le champ date fin
    updateEndDate(event) {
      this.endDate = [event.target.value];
    },
    // méthode pour lancer la recherche
    search() {
      // Vérifie que les champs obligatoires sont renseignés
      if (this.selectedAuthors.length === 0 && this.selectedTitles.length === 0 && this.selectedSupports.length === 0 && this.selectedRegions.length === 0) {
        alert('Veuillez sélectionner au moins un auteur, un titre ou un support.');
        return;
      }
      
      // construction de la requête avec les filtres
      // uniquement avec le 1er champ des filtres
      const query ={
        "date_debut": this.startDate[0]==undefined ? '' : this.startDate[0],
        "date_fin": this.endDate[0]==undefined ? '' : this.endDate[0],
        "artiste": this.selectedAuthors[0]==undefined ? '' : this.selectedAuthors[0],
        "zone_geo": this.selectedRegions[0]==undefined ? '' : this.selectedRegions[0],
        "support": this.selectedSupports[0]==undefined ? '' : this.selectedSupports[0],
        "titre": this.selectedTitles[0]==undefined ? '' : this.selectedTitles[0],
      }

      // Affiche le message "Téléchargement en cours"
      this.downloading = true;

      // Envoi la requête à l'API 
      axios.get('http://localhost:3000/getObjects', { params: query })
        .then(response => {
          this.jsonResponse = response.data;
        })
        .catch(error => {
          this.jsonResponse = error.data;
          alert('Une erreur s\'est produite lors de la recherche. Veuillez réessayer plus tard.');
        })
        .finally(() => {
          this.downloading = false;
          this.afficherModal()
        });
    },

    afficherModal() {
      var modal = document.getElementById('myModal');
      modal.style.display = 'block';
      modal.style.opacity = "100%";

      // Ajoute la classe au corps pour appliquer le style de fond gris
      var div = document.getElementById('container');
      div.classList.add('modal-open');
    },

    // méthode pour fermer le modal dès qu'on clique en dehors du modal
    fermerModalSiClicExterieur(event) {
      var modal = document.getElementById('myModal');
      var div = document.getElementById('container');
      if (modal && event.target !== modal && !modal.contains(event.target)) {
        modal.style.display = 'none';
        div.classList.remove('modal-open');
      }
    },
  
    downloadJSON() {
      // utilisation de Blob pour créer un fichier JSON et créer un lien de téléchargement
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
    // Attache l'événement de fermeture de la modal à la fenêtre lorsque le composant est monté
    window.onclick = this.fermerModalSiClicExterieur;
  }
};