import pandas as pd
from backend.db import get_conn

def global_kpis():
    """
    Global university indicators
    """
    conn = get_conn()
    query = """
    SELECT
        (SELECT COUNT(*) FROM etudiants) AS total_etudiants,
        (SELECT COUNT(*) FROM professeurs) AS total_professeurs,
        (SELECT COUNT(*) FROM formations) AS total_formations,
        (SELECT COUNT(*) FROM modules) AS total_modules,
        (SELECT COUNT(*) FROM examens) AS total_examens,
        (SELECT COUNT(*) FROM salles) AS total_salles
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def salle_utilisation():
    """
    Room usage statistics
    """
    conn = get_conn()
    query = """
    SELECT
        s.nom AS salle,
        s.capacite,
        COUNT(e.id) AS nb_examens,
        ROUND(COUNT(e.id) / NULLIF((SELECT COUNT(*) FROM examens),0) * 100, 2) AS taux_utilisation
    FROM salles s
    LEFT JOIN examens e ON e.salle_id = s.id
    GROUP BY s.nom, s.capacite
    ORDER BY taux_utilisation DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def charge_professeurs():
    """
    Number of surveillances per professor
    """
    conn = get_conn()
    query = """
    SELECT
        CONCAT(p.nom, ' ', p.prenom) AS professeur,
        d.nom AS departement,
        COUNT(e.id) AS nb_surveillance
    FROM professeurs p
    JOIN departements d ON p.dept_id = d.id
    LEFT JOIN examens e ON e.prof_id = p.id
    GROUP BY professeur, departement
    ORDER BY nb_surveillance DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def conflits_professeurs():
    """
    Professors exceeding 3 exams per day
    """
    conn = get_conn()
    query = """
    SELECT
        CONCAT(p.nom, ' ', p.prenom) AS professeur,
        e.date_exam,
        COUNT(e.id) AS nb_examens
    FROM examens e
    JOIN professeurs p ON e.prof_id = p.id
    GROUP BY professeur, e.date_exam
    HAVING COUNT(e.id) > 3
    ORDER BY nb_examens DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def conflits_etudiants():
    """
    Students with more than one exam per day
    """
    conn = get_conn()
    query = """
    SELECT
        CONCAT(et.nom, ' ', et.prenom) AS etudiant,
        ex.date_exam,
        COUNT(ex.id) AS nb_examens
    FROM etudiants et
    JOIN formations f ON et.formation_id = f.id
    JOIN modules m ON m.formation_id = f.id
    JOIN examens ex ON ex.module_id = m.id
    GROUP BY etudiant, ex.date_exam
    HAVING COUNT(ex.id) > 1
    ORDER BY nb_examens DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def conflits_par_departement():
    """
    Conflict count by department
    """
    conn = get_conn()
    query = """
    SELECT
        d.nom AS departement,
        COUNT(e.id) AS nb_examens
    FROM examens e
    JOIN professeurs p ON e.prof_id = p.id
    JOIN departements d ON p.dept_id = d.id
    GROUP BY d.nom
    ORDER BY nb_examens DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def planning_filtre(departement=None, formation=None):
    """
    Filtered exam schedule
    """
    conn = get_conn()
    query = """
    SELECT
        d.nom AS departement,
        f.nom AS formation,
        m.nom AS module,
        e.date_exam,
        e.heure,
        s.nom AS salle
    FROM examens e
    JOIN modules m ON e.module_id = m.id
    JOIN formations f ON m.formation_id = f.id
    JOIN departements d ON f.dept_id = d.id
    JOIN salles s ON e.salle_id = s.id
    """
    conditions = []
    params = []

    if departement:
        conditions.append("d.nom = %s")
        params.append(departement)
    if formation:
        conditions.append("f.nom = %s")
        params.append(formation)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df

def examens_par_jour():
    """
    Exams per day distribution
    """
    conn = get_conn()
    query = """
    SELECT
        date_exam,
        COUNT(*) AS nb_examens
    FROM examens
    GROUP BY date_exam
    ORDER BY date_exam
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df
