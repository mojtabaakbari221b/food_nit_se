from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, is_admin=False, is_staff=False, is_active=False, **extra_fields):
        if not password:
            raise ValueError("User must have a password")

        return self.create_new_user(
            email=email,
            password=password,
            is_admin=is_admin,
            is_staff=is_staff,
            is_active=is_active,
            **extra_fields,
        )
        
    def create_superuser(self, password=None, **extra_fields):
        if not password:
            raise ValueError("User must have a password")

        return self.create_new_user(
            password=password,
            is_admin=True,
            is_staff=True,
            is_active=True,
            **extra_fields,
        )
    
    def create_new_user(self, email, is_admin, is_staff, is_active, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.is_superuser = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user
