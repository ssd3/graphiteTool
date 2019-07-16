from django.utils import timezone
from tradeTools.models import AuthUser, Category


def initdata_users():
    user = AuthUser(username='testUser', password='testUser', date_joined=timezone.now(),
                        is_active=True, is_staff=True, is_superuser=True)
    user.save()

    user = AuthUser(username='testUser2', password='testUser2', date_joined=timezone.now(),
                        is_active=True, is_staff=True, is_superuser=True)
    user.save()

'''
def initdata_categories():
    user = AuthUser(username='testUser', password='testUser', date_joined=timezone.now(),
                    is_active=True, is_staff=True, is_superuser=True)
    user.save()

    category = Category(title='Category1', userid=user, created=timezone.now())
    category.save()
'''