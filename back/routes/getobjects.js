var express = require('express');
const axios = require('axios');
var router = express.Router();

/* A way to get objects */
router.get('/', function(req, res, next) {
  res.send('here will be objects normally');
});

module.exports = router;
