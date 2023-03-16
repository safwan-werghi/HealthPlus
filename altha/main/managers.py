from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,email,first_name,last_name,gender,birthday,phone_number,password):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        if not first_name:
            raise ValueError(_("enter your firstname"))
        if not last_name:
            raise ValueError(_("enter your lastname"))
        if not gender:
            raise ValueError(_("select your gender"))
        if not birthday:
            raise ValueError(_("enter your birthday date"))
        if not phone_number:
            raise ValueError(_("enter your phone number"))
        

        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,gender=gender,birthday=birthday,phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user



            
    def create_superuser(self,email,first_name,last_name,gender,birthday,phone_number,password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not password:
            raise ValueError('SuperUser must have password')
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday,
            phone_number=phone_number,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.email = email
        user.save(using=self._db)
        return user

	





