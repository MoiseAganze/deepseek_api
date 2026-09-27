# API Deepseek

## Endpoint `/message`

**URL (production) :** `https://ai.mapsante.cd/message`
**Méthode :** `POST`
**Content-Type :** `application/json`

### Requête

```json
{
  "message": "Bonjour, comment vas-tu ?"
}
```

### Réponse

```json
{
  "status": "ok",
  "user_message": "Bonjour, comment vas-tu ?",
  "ai_response": "..."
}
```

### Exemple curl

```bash
curl -X POST https://ai.mapsante.cd/message \
  -H "Content-Type: application/json" \
  -d '{"message": "Bonjour, comment vas-tu ?"}'
```
