use Mush
db.createCollection("User", {
  validator: {
    $jsonSchema: {
      type: "object",
      properties: {
        id: {
          type: "number",
          multipleOf: 1 
        },
		    username: {
          type: "string"
        },
        password: {
          type: "string"
        }
      },
      required: ["id", "username", "password"]
    }
  }
})

db.createCollection("JSON", {
  validator: {
    $jsonSchema: {
      type: "object",
      properties: {
        id: {
          type: "number",
          multipleOf: 1
        },
        nb_oeuvres: {
          type: "number",
          multipleOf: 1
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
              lien_oeuvre: { type: "string" }
            },
            required: ["date_oeuvre", "auteur_oeuvre", "support_oeuvre", "zonegeo_oeuvre", "lien_oeuvre"],
            additionalProperties: false
          }
        }
      },
      required: ["id", "nb_oeuvres", "rq_result"],
      additionalProperties: false
    }
  }
})


db.createCollection("Request", {
  validator: {
    $jsonSchema: {
      type: "object",
      properties: {
        id: {
          type: "number",
          multipleOf: 1
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
              support: { type: "string" }
            },
            required: ["date_debut", "date_fin", "artiste", "zonegeo", "support"],
            additionalProperties: false
          }
        }
      },
      required: ["id", "rq_arg"],
      additionalProperties: false
    }
  }
})