#!/usr/bin/env python
import os
import sys
import django

from pathlib import Path


BASE_PATH = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(f"{BASE_PATH}")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

django.setup()


def main():
    from chatbot.models import UserState

    safdaf = UserState.objects.all()
    for dsaf in safdaf:
        print(dsaf)
    print("Done!")


if __name__ == "__main__":
    main()
