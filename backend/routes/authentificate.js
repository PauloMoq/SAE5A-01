// Importation des modules nécessaires.
var express = require('express');
const axios = require('axios');
const {MongoClient} = require('mongodb');
const bcrypt = require('bcrypt');
var router = express.Router();
const mongoose = require('mongoose');

// Connexion à la base de données MongoDB
const mongoUri = process.env.MONGO_URI || 'mongodb://mongodb-container:27017/';

async function main() {
  const client = new MongoClient(mongoUri, { useUnifiedTopology: true, useNewUrlParser: true });
  try {
    await client.connect();
    return client.db("test");
  } catch (error) {
    console.error(error);
  }
}

// Définition du modèle User
const UserSchema = new mongoose.Schema({
    id:{
      type: Number,
      required:true,
      unique:true
    },
    username: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    }
});

const User = mongoose.model('User', UserSchema);

// Route d'inscription
router.post('/register', async (req, res) => {
    const { username, password } = req.body;
      
    // Vérifier si l'utilisateur existe déjà
    const db = await main();
    const existingUser = await db.collection("User").findOne({ username });
  
    if (existingUser) {
      return res.status(400).json({ error: 'L\'utilisateur existe déjà.' });
    }
    
    // Générer un nouvel ID basé sur le maximum actuel dans la collection
    const maxIdResult = await db.collection("User").aggregate([
        { $group: { _id: null, maxId: { $max: "$id" } } }
    ]).toArray();

    let newUserId;
    if (maxIdResult.length > 0) {
        newUserId = maxIdResult[0].maxId + 1;
    } else {
        // Si la collection est vide, commencer par l'ID 1
        newUserId = 1;
    }

    // Hasher le mot de passe
    const hashedPassword = await bcrypt.hash(password, 10);

    // Insérer le nouvel utilisateur avec le nouvel ID généré
    const newUser = {
        id: newUserId,
        username : username,
        password: hashedPassword,
    };
  
    try {
      // Sauvegarder l'utilisateur dans la base de données
      await db.collection("User").insertOne(newUser);
      res.status(201).json({ message: 'Inscription réussie.' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Erreur lors de l\'inscription.' });
    }
});

// Route de connexion
router.post('/login', async (req, res) => {
  const { username, password } = req.body;

  // Vérifier si l'utilisateur existe dans la base de données
  const db = await main();
  const user = await db.collection("User").findOne({ username: username });
  
  // Si l'utilisateur n'existe pas, renvoyer une erreur
  if (!user) {
      return res.status(401).json({ error: 'Ce nom d\'utilisateur est incorrect.' });
  }

  // Comparer le mot de passe fourni avec le mot de passe haché stocké
  const passwordMatch = await bcrypt.compare(password, user.password);

  if (!passwordMatch) {
      // Si les mots de passe ne correspondent pas, renvoyer une erreur
      return res.status(401).json({ error: 'Nom d\'utilisateur ou mot de passe incorrect.' });
  }

  // Authentification réussie
  res.status(200).json({ message: 'Connexion réussie.' });
});

module.exports = router;
