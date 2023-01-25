from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        x = "" + user.pk + timestamp
        return(
            x
        )
    
generate_token = TokenGenerator()