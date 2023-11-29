// Importation de modules Node.js pour la gestion des erreurs HTTP, le framework Express,
// la gestion des chemins, la gestion des cookies, et le logging.
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const cors = require('cors');

// Importation des routes définies dans le dossier 'routes'.
var getObjectsRouter = require('./routes/getobjects');
const authRoutes = require('./routes/authentificate'); 

// Création de l'application Express.
var app = express();
app.use(cors());

// Configuration du moteur de vue (view engine) et du dossier des vues.
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// Utilisation de divers middleware pour la gestion des requêtes et des réponses.
app.use(logger('dev'));  // Middleware de logging en mode développement.
app.use(express.json());  // Middleware pour parser les données JSON dans les requêtes.
app.use(express.urlencoded({ extended: false }));  // Middleware pour parser les données des formulaires.
app.use(cookieParser());  // Middleware pour parser les cookies.
app.use(express.static(path.join(__dirname, 'public')));  // Middleware pour servir des fichiers statiques depuis le dossier 'public'.

// Attribution des routes aux gestionnaires correspondants.
app.use('/getObjects', getObjectsRouter);
app.use('/auth', authRoutes);
// app.use('/login', authRoutes);

// Middleware pour gérer les erreurs 404 (non trouvées) et les rediriger vers le gestionnaire d'erreurs.
app.use(function (req, res, next) {
  next(createError(404));
});

// Middleware pour gérer les erreurs, configuré pour fournir des informations d'erreur dans l'environnement de développement.
app.use(function (err, req, res, next) {
  // Définition des variables locales pour les messages d'erreur et les détails de l'erreur.
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // Renvoi de la page d'erreur avec le statut HTTP correspondant.
  res.status(err.status || 500);
  res.render('error');
});

// Exportation de l'application Express pour être utilisée dans d'autres modules.
module.exports = app;
