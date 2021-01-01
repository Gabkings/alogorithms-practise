class StripeString:
    def stripString(self, s, chars):
        return "".join(c for c in s if c not in chars)