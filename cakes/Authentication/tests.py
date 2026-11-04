from django.test import TestCase

from types import SimpleNamespace

from .models import RoleChoices
from .permission import IsAdmin, IsUser


class RolePermissionTests(TestCase):
    def test_admin_role_is_allowed_to_create_cakes(self):
        request = SimpleNamespace(
            user=SimpleNamespace(is_authenticated=True, role=RoleChoices.ADMIN)
        )

        self.assertTrue(IsAdmin().has_permission(request, None))

    def test_regular_user_role_is_not_allowed_to_create_cakes(self):
        request = SimpleNamespace(
            user=SimpleNamespace(is_authenticated=True, role=RoleChoices.USER)
        )

        self.assertFalse(IsAdmin().has_permission(request, None))

    def test_regular_user_permission_matches_user_role_choice(self):
        request = SimpleNamespace(
            user=SimpleNamespace(is_authenticated=True, role=RoleChoices.USER)
        )

        self.assertTrue(IsUser().has_permission(request, None))
