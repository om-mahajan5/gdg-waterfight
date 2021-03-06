import json, random
import matplotlib.pyplot as plt
data = '''{
   "_links":{
      "self":{
         "href":"https://python-bot-jxkeswruca-em.a.run.app/"
      }
   },
   "arena":{
      "dims":[
         13,
         9
      ],
      "state":{
         "https://nodejskrs-bot-7juvvzwy4q-uc.a.run.app":{
            "x":0,
            "y":0,
            "direction":"S",
            "wasHit":false,
            "score":-3
         },
         "https://python-bot-ksvj7q4wga-em.a.run.app":{
            "x":7,
            "y":0,
            "direction":"W",
            "wasHit":false,
            "score":-59
         },
         "https://python-bot-dnuf5dybaq-em.a.run.app/":{
            "x":5,
            "y":7,
            "direction":"E",
            "wasHit":false,
            "score":-14
         },
         "https://python-bot-wzf2k7csnq-wl.a.run.app":{
            "x":7,
            "y":2,
            "direction":"S",
            "wasHit":false,
            "score":16
         },
         "https://94e9-172-105-34-203.ngrok.io":{
            "x":12,
            "y":1,
            "direction":"W",
            "wasHit":false,
            "score":-25
         },
         "https://python-bot-xpu2myq57q-uc.a.run.app":{
            "x":12,
            "y":0,
            "direction":"E",
            "wasHit":false,
            "score":-4
         },
         "https://python-bot-jxkeswruca-em.a.run.app/":{
            "x":6,
            "y":6,
            "direction":"E",
            "wasHit":false,
            "score":-49
         },
         "https://jay-bot-4rmtwapiia-uc.a.run.app":{
            "x":11,
            "y":3,
            "direction":"S",
            "wasHit":false,
            "score":146
         },
         "https://nodejs-bot-n33wt2kama-as.a.run.app":{
            "x":10,
            "y":0,
            "direction":"W",
            "wasHit":false,
            "score":-25
         },
         "https://python-bot-j4bgsvwz3a-uc.a.run.app":{
            "x":0,
            "y":6,
            "direction":"N",
            "wasHit":true,
            "score":-72
         },
         "https://nodejs-bot-44oaeskbqa-as.a.run.app":{
            "x":4,
            "y":3,
            "direction":"S",
            "wasHit":false,
            "score":-19
         },
         "https://python-bot-adlhc57fcq-de.a.run.app":{
            "x":0,
            "y":8,
            "direction":"N",
            "wasHit":false,
            "score":116
         },
         "https://java-springboot-bot-t34nqg3eqq-as.a.run.app":{
            "x":6,
            "y":2,
            "direction":"W",
            "wasHit":false,
            "score":-21
         },
         "https://java-springboot-bot-r5lsmc2n3q-an.a.run.app":{
            "x":10,
            "y":7,
            "direction":"W",
            "wasHit":false,
            "score":-15
         },
         "https://java-springboot-bot-gwlv4a5zxa-as.a.run.app":{
            "x":2,
            "y":7,
            "direction":"N",
            "wasHit":true,
            "score":-16
         },
         "https://python-bot-oskyweulvq-as.a.run.app/":{
            "x":9,
            "y":8,
            "direction":"S",
            "wasHit":false,
            "score":4
         },
         "https://python-bot-iiqpxb2opq-uc.a.run.app":{
            "x":7,
            "y":3,
            "direction":"N",
            "wasHit":false,
            "score":-22
         },
         "https://python-bot-36ufadraiq-as.a.run.app":{
            "x":0,
            "y":4,
            "direction":"E",
            "wasHit":false,
            "score":-62
         },
         "https://nodejs-bot-gqugfjrxja-uc.a.run.app":{
            "x":2,
            "y":5,
            "direction":"S",
            "wasHit":false,
            "score":124
         }
      }
   }
}'''
info = []
myinfo = []
mydata = json.loads(data)
X= [mydata['arena']['state'][key]['x'] for key in mydata['arena']['state'].keys()]
Y= [mydata['arena']['state'][key]['y'] for key in mydata['arena']['state'].keys()]
D= [mydata['arena']['state'][key]['direction'] for key in mydata['arena']['state'].keys()]
wasHit= [mydata['arena']['state'][key]['wasHit'] for key in mydata['arena']['state'].keys()]
score = [mydata['arena']['state'][key]['score'] for key in mydata['arena']['state'].keys()]
info = list(zip(X,Y,D,wasHit,score))

def southCheck():
   pass

def checkForward(myinfo):
    aheadMe = []
    if myinfo[2] == "S":
        for x in info[1:]:
            if x[0] == myinfo[0] and x[1] > myinfo[1]:
                if x[1]-myinfo[1] <= 3:
                    aheadMe.append(x)
                    print(aheadMe)
                    return "T"
    elif myinfo[2] == "N":
        for x in info[1:]:
            if x[0] == myinfo[0] and x[1] < myinfo[1]:
                if myinfo[1]-x[1] <= 3:
                    aheadMe.append(x)
                    print(aheadMe)
                    return "T"
    elif myinfo[2] == "E":
        for x in info[1:]:
            if x[0] > myinfo[0] and x[1] == myinfo[1]:
                if x[0]-myinfo[0] <= 3:
                    aheadMe.append(x)
                    print(aheadMe)
                    return "T"
    elif myinfo[2] == "W":
        for x in info[1:]:
            if x[0] < myinfo[0] and x[1] == myinfo[1]:
                if myinfo[0]-x[0] <= 3:
                    aheadMe.append(x)
                    print(aheadMe)
                    return "T"
    print(aheadMe)
    return ["L", "R"][random.randrange(2)]

myinfo = info[3] #6 7 9 11
print("My coordinates are :" + str(myinfo))
print(checkForward(myinfo))
print(info)
plt.gca().invert_yaxis()
plt.scatter(X,Y)
plt.scatter(myinfo[0],myinfo[1],marker="s")
plt.show()