import os
import logging
import random
from flask import Flask, request
import json
data='''{
   "_links":{
      "self":{
         "href":"https://python-bot-jxkeswruca-em.a.run.app/"
      }
   },
   "arena":{
      "dims":[
         10,
         7
      ],
      "state":{
         "https://python-bot-jinxto7chq-em.a.run.app":{
            "x":2,
            "y":6,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://java-springboot-bot-vt7gk6uhyq-em.a.run.app":{
            "x":9,
            "y":0,
            "direction":"W",
            "wasHit":false,
            "score":0
         },
         "https://nodejs-bot-zx4wpxe3oq-em.a.run.app":{
            "x":7,
            "y":2,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-3h4xit75ca-uc.a.run.app":{
            "x":6,
            "y":5,
            "direction":"N",
            "wasHit":false,
            "score":0
         },
         "https://nodejs-bot-tmozo7xwqa-as.a.run.app":{
            "x":3,
            "y":5,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://java-springboot-bot-oaiu5q5ata-de.a.run.app":{
            "x":4,
            "y":4,
            "direction":"S",
            "wasHit":false,
            "score":0
         },
         "https://java-quarkus-bot-nallqtvrbq-de.a.run.app":{
            "x":4,
            "y":3,
            "direction":"N",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-ucfpygglmq-an.a.run.app/":{
            "x":4,
            "y":1,
            "direction":"N",
            "wasHit":false,
            "score":0
         },
         "https://nodejs-bot-q7wdicztsa-uc.a.run.app/":{
            "x":0,
            "y":3,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-lt7kzp4ajq-an.a.run.app/":{
            "x":7,
            "y":5,
            "direction":"W",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-jxkeswruca-em.a.run.app/":{
            "x":5,
            "y":4,
            "direction":"S",
            "wasHit":false,
            "score":0
         },
         "https://java-springboot-bot-aoj52cfs3a-em.a.run.app/":{
            "x":3,
            "y":6,
            "direction":"W",
            "wasHit":false,
            "score":0
         }
      }
   }
}'''
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  