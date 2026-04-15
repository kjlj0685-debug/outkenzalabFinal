
import re
import secrets
import string
import hashlib
import requests
import pyotp
import qrcode
import io
import base64
from fastapi.responses import Response
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Password Security Module")


@app.get("/qr-image")
def get_qr():
    data = generate_totp_secret()
    image_bytes = base64.b64decode(data["qr_code"])
    return Response(content=image_bytes, media_type="image/png")

# =========================
# REQUEST MODEL
# =========================

class PasswordRequest(BaseModel):
    password: str

# =========================
# PASSWORD STRENGTH CHECK
# =========================

def check_password(password: str) -> dict:
    """
    Evaluate password strength.
    """

    score = 0
    total = 5
    results = []

    if len(password) >= 12:
        results.append("Length >= 12")
        score += 1

    if re.search("[A-Z]", password):
        results.append("Contains uppercase")
        score += 1

    if re.search("[a-z]", password):
        results.append("Contains lowercase")
        score += 1

    if re.search("[0-9]", password):
        results.append("Contains number")
        score += 1

    if re.search("[@#$%^&*!]", password):
        results.append("Contains symbol")
        score += 1

    security = (score / total) * 100

    strength = "Weak" if score <= 2 else "Medium" if score <= 4 else "Strong"

    return {
        "score": score,
        "security_percentage": security,
        "strength": strength,
        "checks_passed": results
    }

# =========================
# PASSWORD GENERATOR
# =========================

def generate_password(length: int = 12) -> str:
    """
    Generate secure password with all character types.
    """

    if length < 4:
        return "Length must be at least 4"

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("@#$%^&*!")
    ]

    all_chars = string.ascii_letters + string.digits + "@#$%^&*!"
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

# =========================
# PASSPHRASE GENERATOR (WORDLIST)
# =========================

def generate_passphrase(num_words: int = 4) -> str:
    """
    Generate Diceware-like passphrase using wordlist file.
    """

    try:
        with open("wordlist.txt", "r") as f:
            word_list = [line.strip() for line in f if line.strip()]
    except:
        return "Error: wordlist.txt not found"

    if len(word_list) < num_words:
        return "Not enough words in wordlist"

    return ' '.join(secrets.SystemRandom().sample(word_list, num_words))

# =========================
# TOTP 2FA + QR CODE
# =========================

def generate_totp_secret() -> dict:
    """
    Generate TOTP secret with QR Code.
    """

    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(
        name="user@example.com",
        issuer_name="SecurityApp"
    )

    qr = qrcode.make(uri)

    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return {
        "secret": secret,
        "current_code": totp.now(),
        "qr_code": qr_base64,
        "uri": uri
    }

# =========================
# CHECK BREACHED PASSWORD
# =========================

def check_pwned_password(password: str) -> dict:
    """
    Check if password is leaked using HIBP API.
    """

    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    res = requests.get(url, timeout=5)

    if res.status_code != 200:
        return {"error": "API error"}

    hashes = (line.split(":") for line in res.text.splitlines())

    for h, count in hashes:
        if h == suffix:
            return {"breached": True, "count": int(count)}

    return {"breached": False}

# =========================
# API ENDPOINTS
# =========================

@app.get("/")
def home():
    return {"message": "Password Security API"}

@app.post("/check-password")
def api_check_password(data: PasswordRequest):
    return check_password(data.password)

@app.get("/generate-password")
def api_generate_password(length: int = 12):
    if length < 8:
        return {"error": "Length should be at least 8"}
    return {"password": generate_password(length)}

@app.get("/generate-passphrase")
def api_generate_passphrase(words: int = 4):
    return {"passphrase": generate_passphrase(words)}

@app.get("/generate-2fa")
def api_generate_2fa():
    return generate_totp_secret()

@app.post("/check-breach")
def api_check_breach(data: PasswordRequest):
    return check_pwned_password(data.password)