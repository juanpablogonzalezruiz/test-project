# Hello World program in Python
import json    


str = "{\"answers\": [{\"questions\": [\"how many tickets buy\"], \"answer\": \"Please visit out ticketing section at the next link for more information about ticket sales.\", \"score\": 50.67, \"id\": 46, \"source\": \"Editorial\", \"metadata\": [{\"name\": \"intent\", \"value\": \"buy many\"}, {\"name\": \"category\", \"value\": \"tickets\"}]}, {\"questions\": [\"ticket prices\", \"ticket how much\"], \"answer\": \"Our ticket prices range from $101-$550 dollars. For more information visit http://tottenham.com/tickets\", \"score\": 48.95, \"id\": 51, \"source\": \"Editorial\", \"metadata\": [{\"name\": \"intent\", \"value\": \"prices\"}, {\"name\": \"category\", \"value\": \"ticket\"}]}, {\"questions\": [\"ticket disponibility\", \"ticket availability\", \"tickets left\"], \"answer\": \"To check for ticket availability please go to our website http://www.tottenham.com/tickets/stock\", \"score\": 42.33, \"id\": 56, \"source\": \"Editorial\", \"metadata\": [{\"name\": \"intent\", \"value\": \"availability\"}, {\"name\": \"category\", \"value\": \"tickets\"}]}, {\"questions\": [\"missing tickets\", \"lost tickets\", \"i cant find my tickets\", \"loose ticket\", \"miss ticket\"], \"answer\": \"please call the Ticket Office on 0344 844 0102 (UK) or from overseas on +44 20 7998 1068, selecting option 2. Lines are open from Monday - Friday, 09:30 - 17:00.\", \"score\": 40.89, \"id\": 47, \"source\": \"Editorial\", \"metadata\": [{\"name\": \"intent\", \"value\": \"missing\"}, {\"name\": \"category\", \"value\": \"tickets\"}]}, {\"questions\": [\"ticket delivery time\", \"ticket shipping time\", \"ticket arrival time\", \"when delivery ticket\", \"when arriving ticket\"], \"answer\": \"Any tickets purchased on the ticket hotline or on the Club website will be held for collection on matchday. These tickets can be collected from our Collection Office based at our new unit outside the Tottenham Community Sports Centre.\", \"score\": 39.67, \"id\": 49, \"source\": \"Editorial\", \"metadata\": [{\"name\": \"intent\", \"value\": \"delivery\"}, {\"name\": \"category\", \"value\": \"ticket\"}, {\"name\": \"subcategory\", \"value\": \"time\"}]}]}"

response = json.loads(str)
print("response:")
#print(response['answers'][0]['questions'])
for answer in response['answers']:
    print("QUESTION ")
    for question in answer['questions']:
        print(" - " + question)
    print("ANSWER   : " + answer['answer'] )
    print("SCORE    : " + repr(answer['score']) )
    print('\n')