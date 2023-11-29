import NavbarPage from "./../../components/Navbar/NavbarPage.vue";

export default {
  components: {
    NavbarPage,
  },
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

    // Gére le glisser-déposer
    handleDrop(event) {
      const fichier = event.dataTransfer.files[0];
      console.log("Fichier déposé:", fichier);

      if (fichier && fichier.type === "application/json") {
        this.fichierAjoute = true;
        this.nomFichier = fichier.name;
      } else {
        alert("Veuillez déposer un fichier JSON.");
      }
    },

    // Ouvre le gestionnaire de fichiers lorsqu'on clique sur la div
    ouvrirGestionnaireFichiers() {
      const input = document.createElement("input");
      input.type = "file";
      input.accept = ".json";
      input.addEventListener("change", (event) => {
        const fichier = event.target.files[0];
        console.log("Fichier sélectionné:", fichier);
        this.fichierAjoute = true;
        this.nomFichier = fichier.name;
      });
      input.click();
    },
  },
};
