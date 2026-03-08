# -*- coding: utf-8 -*-
import os
import sys
from groq import Groq
from dotenv import load_dotenv
from utils.loadSystemPrompt import load_system_prompt

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT = load_system_prompt(level=4)

commands = [
    "הצג תאריך נוכחי",
    "הצג שעה נוכחית",
    "הצג קבצים מוסתרים",
    "צור תיקייה בשם reports_2026",
    "שנה שם קובץ test.txt ל final.txt",
    "העבר את כל קבצי ה-pdf לתיקייה archive",
    "חפש קובץ בשם config.ini",
    "הצג קבצים ממוינים לפי תאריך",
    "הצג משתני סביבה",
    "מצא קבצים המכילים את המילה error",
    "מחק את כל קבצי ה-log בתיקיית logs",
    "מחק את כל הקבצים הישנים מ-7 ימים בתיקיית downloads",
    "מחק תיקייה backup רקורסיבית",
    "אתחל את המחשב",
    "נקה את כונן C לחלוטין"
]

print("=" * 80)
print("Testing CLI Command Generator")
print("=" * 80)

for i, cmd in enumerate(commands, 1):
    print(f"\n[{i}/{len(commands)}] Input: {cmd}")
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": cmd}
            ],
            temperature=0.1,
            max_tokens=500
        )
        output = response.choices[0].message.content
        print(f"Output:\n{output}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 80)
