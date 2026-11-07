import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "lesson_memory.db"
)


def init_db():
    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS lesson_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT,
                score INTEGER,
                passed BOOLEAN,
                attempts INTEGER,
                feedback TEXT,
                created_at TEXT
            )
        """)


def save_run(topic, score, passed, attempts, feedback):
    init_db()

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO lesson_history
            (topic, score, passed, attempts, feedback, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            topic,
            score,
            passed,
            attempts,
            str(feedback),
            datetime.now().isoformat()
        ))


def get_learning_notes(topic):
    init_db()

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("""
            SELECT feedback
            FROM lesson_history
            WHERE topic = ? AND passed = 0
            ORDER BY id DESC
            LIMIT 5
        """, (topic,)).fetchall()

    return [row[0] for row in rows]


def save_rejection(topic, lesson, score, feedback, attempt):
    init_db()

    log_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "outputs",
        "rejection_log.txt"
    )

    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    with open(log_path, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(f"Topic: {topic}\n")
        file.write(f"Attempt: {attempt}\n")
        file.write(f"Score: {score}\n")
        file.write(f"Feedback: {feedback}\n")
        file.write("Rejected lesson:\n")
        file.write(lesson + "\n")


def get_history():
    init_db()

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("""
            SELECT topic, score, passed, attempts, feedback, created_at
            FROM lesson_history
            ORDER BY id DESC
        """).fetchall()

    return rows