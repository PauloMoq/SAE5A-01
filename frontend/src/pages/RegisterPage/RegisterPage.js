import NavbarPage from "./../../components/Navbar/NavbarPage.vue";
import axios from "axios";
import Swal from "sweetalert2";

export default {
  components: {
    NavbarPage,
  },
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    register() {
      if (this.password != this.confirmPassword) {
        Swal.fire("Erreur !", "Les mots de passes sont différents.", "error");
      } else {
        // envoi la requete register au back
        axios
          .post("http://localhost:3000/auth/register", {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            console.log(response);
            this.$router.push("/login");
          })
          .catch((error) => {
            console.log(error);
            if (error.response) {
              // Récupérer le message d'erreur de la réponse JSON
              if (error.response.data && error.response.data.error) {
                Swal.fire("Erreur !", error.response.data.error, "error");
              } else {
                Swal.fire(
                  "Erreur !",
                  "Une erreur inattendue s'est produite.",
                  "error"
                );
              }
            } else if (error.request) {
              // La requête a été faite, mais aucune réponse n'a été reçue
              console.log(error.request);
            } else {
              // Une erreur s'est produite lors de la configuration de la requête
              console.log("Error", error.message);
            }
            console.log(error.config); // La configuration de la requête qui a déclenché l'erreur
          });
      }
    },
  },
};
