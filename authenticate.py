from pymessenger.bot import Bot


ACCESS_TOKEN = "EAANwtWmfWRQBALXLx9iEBJaoly7TFLEjoKPk7Ecww22UkzzOHT7ZBSCq2c5wxSg7IoIVQrR97k8oiGV2ODRFdPtpGPLnK5OZAh8ADgNtERhD88jW8WbmrosqY144htAKBiZArEIqWFMFwxtBkSHOEQ3PkxzZBDDQUPOZArMXrZBCtTZAg2abrX00oUm3gzLC6gZD"
VERIFY_TOKEN = "rohzanpoudeldtryuiuyvgfchhvcfgdcfhvjbknjjvghchgh"

def verify_bot_access():
    return Bot(ACCESS_TOKEN)

def verify_token(request):
    token_received = request.args.get("hub.verify_token")
    if token_received == VERIFY_TOKEN:
        return request.args.get("hub.challange")
    else:
        return "Access Denied"
        
    

