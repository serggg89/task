from models import SignInBody, InvalidCredentialsResponse

AUTH_ENDPOINT = '/api/auth/login'

INVALID_CREDENTIALS = SignInBody(login='hello@world.com', password='12345678')
EXPECTED_RESPONSE = InvalidCredentialsResponse({
    "success": False,
    "errors": {
        "email": [""],
        "password": [""],
        "message": "The password and email you entered don't match. If you forgot your password, "
                   "use \"Forgot Password\""
    }
})
# according to REST specification
UNAUTHORIZED_STATUS_CODE = 401