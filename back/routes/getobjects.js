var express = require('express');
const axios = require('axios');
var router = express.Router();

/* Un moyen de récupérer les oeuvres recherchés */
router.get('/', async function (req, res, next) {
  // On récupère les paramètres de la recherche.
  const filtreRecherche = {
    "date_debut": "",
    "date_fin": "",
    "artiste": "Claude Monet",
    "zone_geo": "",
    "support": "",
    "titre": ""
  };

  // Ici, on créé "baseUrl", qui est la base de l'url de recherche.
  const baseUrl = "https://collectionapi.metmuseum.org/public/collection/v1/search";

  // Créer une liste des paramètres de la recherche à partir des valeurs remplies.
  const queryParams = Object.entries(filtreRecherche)
    .filter(([key, value]) => value !== "")
    .map(([key, value]) => `${key}=${encodeURIComponent(value)}`);

  // Construire l'URL complète avec les paramètres?
  const queryString = queryParams.length > 0 ? `?${queryParams.join('&')}` : '';
  var fullUrl = `${baseUrl}${queryString}`;
  // On fait ici le remplacement des chaînes de caractères pour que cela fasse la requête que l'on souhaite à l'API.
  fullUrl = fullUrl.replace("zone_geo", "geoLocation").replace("support", "medium").replace("artiste", "q").replace("date_fin", "dateEnd").replace("date_debut", "dateBegin").replace("titre", "title") + "&hasImages=true";

  try {

    // On fait la requête à l'API.
    const responseSearch = await axios.get(fullUrl);

    // On récupère la liste des objectIDs.
    const listObjectIDs = responseSearch.data.objectIDs;

    const objects = [];

    // On récupère les informations de chaque oeuvre.
    for (let index = 0; index < listObjectIDs.length; index++) {
      try {
        // On récupère l'oeuvre.
        const object = await axios.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + listObjectIDs[index]);
        if (object.data.primaryImage === ""){
          // Si l'oeuvre n'a pas d'image, on ne l'ajoute pas au json.
          console.error("L'objet " + listObjectIDs[index] + " n'a pas d'image, il ne sera pas ajouté au json.");
          continue;
        }

        const objectData = 
        { // On récupère les informations de l'oeuvre.
          "date_oeuvre": object.data.objectDate,
          "auteur_oeuvre": object.data.artistDisplayName,
          "support_oeuvre": object.data.medium,
          "zonegeo_oeuvre": object.data.country,
          "lien_oeuvre": object.data.primaryImage
        };
        // On ajoute l'oeuvre à la liste des oeuvres.
        objects.push(objectData);

      } catch (error) {
        // Si on a une erreur lors de la récupération d'un fichier, on l'affiche dans la console.
        console.error("Erreur lors de la récupération de l'objet " + listObjectIDs[index] + " : " + error);
      }
    }

    // On créé le json de réponse.
    const requete = {
      "rq_user": "",
      "rq_nboeuvre": objects.length, // On récupère le nombre d'oeuvres.
      "rq_arg": filtreRecherche, // On récupère les arguments de la recherche.
      "rq_result": objects // On récupère les oeuvres.
    }
  
    res.send(requete);
  } catch (error) {
    // Si on a une erreur lors de la récupération DES fichiers, on l'affiche dans la console.
    console.error(error);
    res.status(500).json({ error: 'Une erreur à occuré pendant la récupération des données.' });
  }

});

module.exports = router;