from jsonobject import JsonObject, StringProperty, ObjectProperty, ListProperty, BooleanProperty


class SignInBody(JsonObject):
    login = StringProperty(required=True)
    password = StringProperty(required=True)


class _InvalidCredentialsErrors(JsonObject):
    email = ListProperty(StringProperty, required=True)
    password = ListProperty(StringProperty, required=True)
    message = StringProperty(required=True)

    def __eq__(self, other):
        # email and password lists should be sorted before comparing
        return sorted(self.email) == sorted(other.email) and sorted(self.password) == sorted(other.password) and \
               self.message == other.message


class InvalidCredentialsResponse(JsonObject):
    success = BooleanProperty(required=True)
    errors = ObjectProperty(_InvalidCredentialsErrors)

    def __eq__(self, other):
        return self.success == other.success and self.errors == other.errors