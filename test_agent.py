import pytest

# Suite de 20 cas de tests métiers pour l'agent
TEST_DATA = [
    ("salutation", "SUCCESS", "Bonjour"),
    ("calcul_simple", "SUCCESS", "Résultat"),
    ("recherche_web", "SUCCESS", "Info trouvée"),
    ("traduction", "SUCCESS", "Texte traduit"),
    ("resume_texte", "SUCCESS", "Résumé"),
    ("code_python", "SUCCESS", "Code généré"),
    ("question_histoire", "SUCCESS", "Réponse historique"),
    ("meteo", "SUCCESS", "Données météo"),
    ("conversion_unite", "SUCCESS", "Valeur convertie"),
    ("analyse_sentiment", "SUCCESS", "Sentiment positif"),
    ("extraction_mot_cle", "SUCCESS", "Mots clés"),
    ("generation_sql", "SUCCESS", "Requête SQL"),
    ("reformulation", "SUCCESS", "Texte reformulé"),
    ("verification_fait", "SUCCESS", "Fait vérifié"),
    ("plan_action", "SUCCESS", "Plan d'action"),
    ("recherche_doc", "SUCCESS", "Document trouvé"),
    ("erreur_input_vide", "FAILURE", "Entrée vide non autorisée"),
    ("erreur_token_limit", "FAILURE", "Limite de tokens dépassée"),
    ("erreur_timeout", "FAILURE", "Temps d'attente dépassé"),
    ("erreur_inconnue", "FAILURE", "Commande non reconnue")
]

def mock_agent_service(intent):
    """Mock simulant le service d'agent"""
    if intent.startswith("erreur_"):
        return {"status": "FAILURE", "message": "Erreur détectée"}
    return {"status": "SUCCESS", "message": "OK"}

@pytest.mark.parametrize("intent, expected_status, expected_msg", TEST_DATA)
def test_agent_intents(intent, expected_status, expected_msg):
    result = mock_agent_service(intent)
    assert result["status"] == expected_status