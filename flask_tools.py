# Load API Keys from .env file
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

class NotionHabitEvents:
    
    # hard coding the database id for now
    habit_events = '39ef2f1b-c246-46d6-b35f-00ca76128c02'
    pills = '46c7d9bb-db60-488f-bbe1-084de549dfbc'
    
    water = "💧 Drink Water"
    weed = "🌿 Smoke Weed"
    meal = "🍽️ Eat a Meal"
    sleep = "😴 Sleep"
    wake = "🌅 Wake Up"
    work = "💼 Work"
    short_break = "🏖️ Take a Break"
    exercise = "🏋️ Exercise"
    meditate = "🧘 Meditate"
    clean = "🧹 Clean"
    cook = "🍳 Cook"
    socialize = "🤝 Socialize"
    relax = "🛀 Relax"
    study = "📚 Study"
    shop = "🛒 Shop"
    feed_nova = "🐶 Feed Nova"
    concerta = "💊 Take Concerta"
    
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {os.getenv('NOTION_API_KEY')}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
    
    def update_db_entry(self, db_id:str, properties:dict) -> dict:
        data = {"parent": {"database_id": db_id}, "properties": properties}
        req = requests.post(f'https://api.notion.com/v1/pages', json=data, headers=self.headers)
        return req.json()
    
    def add_habit_event(self, event:str) -> dict:
        properties = {"Event": {"title": [{"text": {"content": event}}]}}
        return self.update_db_entry(self.habit_events, properties)
    
    
    


from flask import Flask

app = Flask(__name__)
notion = NotionHabitEvents()

@app.route('/')
def hello():
   return 'Hello, World!'

@app.route('/water')
def drink_water():
    notion.add_habit_event(notion.water)
    return 'Water logged!'

@app.route('/weed')
def smoke_weed():
    notion.add_habit_event(notion.weed)
    return 'Weed logged!'

@app.route('/eat')
def eat_meal():
    notion.add_habit_event(notion.meal)
    return 'Meal logged!'


@app.route('/concerta')
def take_concerta():
    notion.add_habit_event(notion.concerta)
    return 'Concerta logged!'

@app.route('/wake')
def wake_up():
    notion.add_habit_event(notion.wake)
    return 'Woken up logged!'

@app.route('/feed_nova')
def feed_nova():
    notion.add_habit_event(notion.feed_nova)
    return 'Fed Nova logged!'

@app.route('/clean')
def clean():
    notion.add_habit_event(notion.clean)
    return 'Cleaning logged!'

@app.route('/cook')
def cook():
    notion.add_habit_event(notion.cook)
    return 'Cooking logged!'

if __name__ == '__main__':
<<<<<<< HEAD
   app.run(port=5000) 
=======
   app.run(port=5000)
>>>>>>> 4c2235900596e4be8295380957a9190e24a0b567
