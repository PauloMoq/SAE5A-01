db.createCollection("User", {
  validator: {
    $jsonSchema: {
      type: "object",
      properties: {
        id: {
          type: "number",
          multipleOf: 1,
        },
        username: {
          type: "string",
        },
        password: {
          type: "string",
        },
      },
      required: ["id", "username", "password"],
    },
  },
});

db.createCollection("JSON", {
  validator: {
    $jsonSchema: {
      type: "object",
      properties: {
        id: {
          type: "number",
          multipleOf: 1,
        },
        nb_oeuvres: {
          type: "number",
          multipleOf: 1,
        },
        rq_result: {
          type: "array",
          items: {
            type: "object",
            properties: {
              date_oeuvre: { type: "string" },
              auteur_oeuvre: { type: "string" },
              support_oeuvre: { type: "string" },
              zonegeo_oeuvre: { type: "string" },
              lien_oeuvre: { type: "string" },
            },
          },
        },
      },
      required: ["id", "nb_oeuvres", "rq_result"],
      additionalProperties: true,
    },
  },
});

db.createCollection("Request", {
  validator: {
    $jsonSchema: {
      type: "object",
      properties: {
        id: {
          type: "number",
          multipleOf: 1,
        },
        rq_arg: {
          type: "array",
          items: {
            type: "object",
            properties: {
              date_debut: { type: "string" },
              date_fin: { type: "string" },
              artiste: { type: "string" },
              zonegeo: { type: "string" },
              support: { type: "string" },
            },
          },
        },
      },
      required: ["id", "rq_arg"],
      additionalProperties: true,
    },
  },
});

db.Request.insertOne({
  id: 1,
  rq_arg: [
    {
      _id: 1,
      date_debut: "dateBegin",
      date_fin: "dateEnd",
      artiste: "q",
      zonegeo: "geoLocation",
      support: "medium",
    }
  ]
})