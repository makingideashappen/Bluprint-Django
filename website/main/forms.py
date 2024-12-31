from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm 
import logging

logger = logging.getLogger(__name__)

class MyCustomSignupForm(SignupForm):
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        logger.info(f"Verification email sent to {user.email}")


        # You must return the original result.
        return user
    
class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)
    

class MyCustomResetPasswordForm(ResetPasswordForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save(request)

        # Add your own processing here.

        # Ensure you return the original result
        return email_address