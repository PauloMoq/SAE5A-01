// Importation des modules nécessaires.
var express = require('express');
const axios = require('axios');
const {MongoClient} = require('mongodb');
const mongoose = require('mongoose');
var router = express.Router();


/* Un moyen de récupérer les oeuvres recherchés */
router.get('/', async function (req, res, next) {
  const mongoUri = process.env.MONGO_URI || 'mongodb://mongodb-container:27017/';
  
  async function main() {
    const client = new MongoClient(mongoUri, { useUnifiedTopology: true, useNewUrlParser: true  });
  
    try {
      await client.connect();
      
      const database = client.db("test");

      const request = database.collection("Request");
      
      const apiParams = await request.findOne({id: 1});
      
      return apiParams.rq_arg[0];
  
    } catch (error) {
      console.error(error);
    }
  }

  var params = await main().catch(console.error);

  console.log(req.body)

  // On récupère les paramètres de la recherche.
  const filtreRecherche = req.query.length === 0 ? {
    "date_debut": "",
    "date_fin": "",
    "artiste": "Claude Monet",
    "zone_geo": "",
    "support": "",
    "titre": ""
  } : req.query;

  // Ici, on créé "baseUrl", qui est la base de l'URL de recherche.
  const baseUrl = "https://collectionapi.metmuseum.org/public/collection/v1/search";

  // Créer une liste des paramètres de la recherche à partir des valeurs remplies.
  const queryParams = Object.entries(filtreRecherche)
    .filter(([key, value]) => value !== "")
    .map(([key, value]) => `${key}=${encodeURIComponent(value)}`);

  // Construire l'URL complète avec les paramètres.
  const queryString = queryParams.length > 0 ? `?${queryParams.join('&')}` : '';
  var fullUrl = `${baseUrl}${queryString}`;
  // On fait ici le remplacement des chaînes de caractères pour que cela fasse la requête que l'on souhaite à l'API.
  fullUrl = fullUrl.replace("zone_geo", params.zone_geo).replace("support", params.support).replace("artiste", params.artiste).replace("date_fin", params.date_fin).replace("date_debut", params.date_debut).replace("titre", "title") + "&hasImages=true";

  try {
    // On fait la requête à l'API.
    const responseSearch = await axios.get(fullUrl);

    // On récupère la liste des objectIDs.
    const listObjectIDs = responseSearch.data.objectIDs;

    const objects = [];

    // On récupère les informations de chaque œuvre.
    for (let index = 0; index < listObjectIDs.length; index++) {
      try {
        // On récupère l'œuvre.
        const object = await axios.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + listObjectIDs[index]);
        if (object.data.primaryImage === "") {
          // Si l'œuvre n'a pas d'image, on ne l'ajoute pas au JSON.
          console.error("L'objet " + listObjectIDs[index] + " n'a pas d'image, il ne sera pas ajouté au JSON.");
          continue;
        }

        const objectData =
        { // On récupère les informations de l'œuvre.
          "date_oeuvre": object.data.objectDate,
          "auteur_oeuvre": object.data.artistDisplayName,
          "support_oeuvre": object.data.medium,
          "zonegeo_oeuvre": object.data.country,
          "lien_oeuvre": object.data.primaryImage
        };
        // On ajoute l'œuvre à la liste des œuvres.
        objects.push(objectData);

      } catch (error) {
        // Si on a une erreur lors de la récupération d'un fichier, on l'affiche dans la console.
        console.error("Erreur lors de la récupération de l'objet " + listObjectIDs[index] + " : " + error);
      }
    }

    // On créé le JSON de réponse.
    const requete = {
      "rq_user": "",
      "rq_nboeuvre": objects.length, // On récupère le nombre d'œuvres.
      "rq_arg": filtreRecherche, // On récupère les arguments de la recherche.
      "rq_result": objects // On récupère les œuvres.
    }

    res.send(requete);
  } catch (error) {
    // Si on a une erreur lors de la récupération DES fichiers, on l'affiche dans la console.
    console.error(error);
    res.status(500).json({ error: 'Une erreur a eu lieu pendant la récupération des données.' });
  }

});

// Exportation du routeur pour être utilisé dans d'autres modules.
module.exports = router;
