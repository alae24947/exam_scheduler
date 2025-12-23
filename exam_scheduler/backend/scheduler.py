import random
from backend.db import get_conn
from datetime import date, timedelta, time

def generate_exam_schedule():
    """
    Generate random exam schedule for all modules.
    """
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # Get all modules, professors, and rooms
            cur.execute("SELECT id FROM modules")
            modules = cur.fetchall()

            cur.execute("SELECT id FROM professeurs")
            profs = cur.fetchall()

            cur.execute("SELECT id FROM salles")
            salles = cur.fetchall()

            start_date = date.today()

            for i, m in enumerate(modules):
                # Random exam date and time
                exam_date = start_date + timedelta(days=i % 10)
                exam_time = time(9 + (i % 3)*2, 0)

                # Insert exam into database
                cur.execute("""
                    INSERT INTO examens (module_id, prof_id, salle_id, date_exam, heure, duree)
                    VALUES (%s, %s, %s, %s, %s, 120)
                """, (
                    m[0],
                    random.choice(profs)[0],
                    random.choice(salles)[0],
                    exam_date,
                    exam_time
                ))

        # Commit after all inserts
        conn.commit()
    finally:
        conn.close()
