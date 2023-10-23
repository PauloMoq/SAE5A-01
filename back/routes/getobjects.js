var express = require('express');
const axios = require('axios');
var router = express.Router();

/* A way to get objects */
router.get('/', async function (req, res, next) {
  const filtreRecherche = {
    "date_debut": "",
    "date_fin": "",
    "artiste": "Claude Monet",
    "zone_geo": "",
    "support": "",
    "titre": ""
  };

  const baseUrl = "https://collectionapi.metmuseum.org/public/collection/v1/search";

  // Créer une liste des paramètres de la recherche à partir des valeurs remplies.
  const queryParams = Object.entries(filtreRecherche)
    .filter(([key, value]) => value !== "")
    .map(([key, value]) => `${key}=${encodeURIComponent(value)}`);

  // Construire l'URL complète
  const queryString = queryParams.length > 0 ? `?${queryParams.join('&')}` : '';
  var fullUrl = `${baseUrl}${queryString}`;
  // On fait ici le remplacement des chaînes pour que cela fasse la requête que l'on souhaite à l'API
  fullUrl = fullUrl.replace("zone_geo", "geoLocation").replace("support", "medium").replace("artiste", "q").replace("date_fin", "dateEnd").replace("date_debut", "dateBegin").replace("titre", "title") + "&hasImages=true";

  try {

    const responseSearch = await axios.get(fullUrl);

    console.log(fullUrl);

    const listObjectIDs = responseSearch.data.objectIDs;

    const objects = [];

    for (let index = 0; index < listObjectIDs.length; index++) {
      try {
        
        const object = await axios.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + listObjectIDs[index]);
        if (object.data.primaryImage === ""){
          console.error("L'objet " + listObjectIDs[index] + " n'a pas d'image, il ne sera pas ajouté au json.");
          continue;
        }

        const object_data = 
        {
          "date_oeuvre": object.data.objectDate,
          "auteur_oeuvre": object.data.artistDisplayName,
          "support_oeuvre": object.data.medium,
          "zonegeo_oeuvre": object.data.country,
          "lien_oeuvre": object.data.primaryImage
        };
        objects.push(object_data);

      } catch (error) {
        console.error("Erreur lors de la récupération de l'objet " + listObjectIDs[index] + " : " + error);
      }
    }
  
    const requete = {
      "rq_user": "",
      "rq_nboeuvre": objects.length,
      "rq_arg": filtreRecherche,
      "rq_result": objects
    }
  
    res.send(requete);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Une erreur à occuré pendant la récupération des données.' });
  }

});

module.exports = router;