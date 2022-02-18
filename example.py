#!/usr/bin/env python3
"""Example Python module.

This module simply prints a nice message when executed."""


import os


def say_hi():
    """Say hello to the user."""
    user = os.environ.get('USER', 'world')
    print(f"Hello, {user}!")


if __name__ == "__main__":
    say_hi()
