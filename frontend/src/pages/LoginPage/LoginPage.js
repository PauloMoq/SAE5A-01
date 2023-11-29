import axios from "axios";
import Swal from "sweetalert2";
import NavbarPage from "./../../components/Navbar/NavbarPage.vue";

export default {
  components: {
    NavbarPage,
  },
  props: ["updateAuthentication"],
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      // envoi la requete de connexion au back (avec l'username et le mot de passe comme paramètre)
      axios
        .post("http://localhost:3000/auth/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          console.log(response);
          // permet d'envoyer l'info à la navbar que l'user est connecté afin d'actualiser les champs de la navbar
          this.updateAuthentication({
            isAuthenticated: true,
            username: this.username,
          });
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
          if (error.response) {
            // Récupérer le message d'erreur de la réponse JSON
            if (error.response.data && error.response.data.error) {
              // Swal permet d'afficher des messages d'erreur facilement avec un style de base
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
          console.log(error.config); // La configuration de la requête a déclenché l'erreur
        });
    },
  },
};
