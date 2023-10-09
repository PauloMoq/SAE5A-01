var express = require('express');
const axios = require('axios');
var router = express.Router();

/* A way to get objects */
router.get('/', async function(req, res, next) {
  const filtreRecherche = {
    "date_debut": "1800",
    "date_fin": "1802",
    "artiste": "",
    "zone_geo": "",
    "support": ""
  };
  
  const baseUrl = "https://collectionapi.metmuseum.org/public/collection/v1/search";
  
  // Créer une liste des paramètres de la recherche à partir des valeurs remplies.
  const queryParams = Object.entries(filtreRecherche)
    .filter(([key, value]) => value !== "")
    .map(([key, value]) => `${key}=${encodeURIComponent(value)}`);
  
  // Construire l'URL complète
  const queryString = queryParams.length > 0 ? `?${queryParams.join('&')}` : '';
  const fullUrl = `${baseUrl}${queryString}`;
  const query = fullUrl.replace()

  res.send(fullUrl);


  /* try {
    const response = await axios.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/45734');
    
    if (response.data.primaryImage) {
      let oeuvre = {
        "date_oeuvre": response.data.objectDate,
        "auteur_oeuvre": response.data.artistDisplayName,
        "support_oeuvre": response.data.objectName,
        "zonegeo_oeuvre": response.data.country,
        "lien_oeuvre": response.data.primaryImage
      }

      res.json(oeuvre);
    } else {
      res.json('No Image.');
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Une erreur à occuré pendant la récupération des données.' });
  } */
});

module.exports = router;