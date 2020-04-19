from random import randint

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from hn_users.models import HNUser, User
from links.models import Link, Vote

faker = Faker()


class Command(BaseCommand):
    help = "Generate Links from a small user subset"

    def add_arguments(self, parser):
        parser.add_argument("no_of_users", type=int, nargs="?", default=4)
        parser.add_argument("no_of_links", type=int, nargs="?", default=20)

    @transaction.atomic()
    def handle(self, *args, **options):
        no_of_users = options.get("no_of_users")
        no_of_links = options.get("no_of_links")

        for user in range(no_of_users):
            user = self._create_user()
            hn_user = self._create_hn_user(django_user=user)

        for link in range(no_of_links):
            generated_link = self._create_link()
            generated_link.refresh_from_db()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Link {generated_link.url} generated with {generated_link.link_votes.count()} votes"
                )
            )

    def _create_link(self):

        all_users_count = HNUser.objects.count()
        number_of_users_who_voted = randint(1, all_users_count)  # nosec
        randomly_ordered_users = HNUser.objects.all().order_by("?")  # nosec
        random_users = randomly_ordered_users[:number_of_users_who_voted]

        hn_user = HNUser.objects.all().order_by("?").first()
        link = Link()
        link.posted_by = hn_user
        link.url = faker.url()
        link.description = faker.text()
        link.save()

        for random_user in random_users:
            vote = Vote()
            vote.link = link
            vote.user = random_user
            vote.save()

        return link

    def _create_user(self):
        simple_profile = faker.simple_profile()
        user = User()
        user.email = simple_profile["mail"]
        user.username = simple_profile["username"]
        user.first_name = simple_profile["name"].split(" ")[0]
        user.last_name = simple_profile["name"].split(" ")[-1]
        user.set_password(faker.password())
        user.save()
        return user

    def _create_hn_user(self, django_user):
        hn_user = HNUser()
        hn_user.bio = faker.text()
        hn_user.django_user = django_user
        hn_user.save()
