# -*- coding:utf-8 -*-
#
# Created Time: 2020/6/27 7:30 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import click
from flask.cli import AppGroup

from apps.dao.user import UserDao


UDao = UserDao()

user_cli = AppGroup('user')


@user_cli.command('hello')
@click.option('--n', default=1)
def hello(n):
    click.echo('hello' * n)


@user_cli.command('create')
@click.option('--u', prompt='User name', help='User name')
@click.option('--p', hide_input=True, prompt='User password', help='User Password')
@click.option('--e', prompt='User email', help='Mail address')
@click.option('--r', default='user', prompt='User role', help='User role')
def create_user(u, p, e, r):
    """Create User"""
    u_data = {
        'username': u,
        'password': p,
        'email': e,
        'role': r
    }
    if UDao.add_user(u_data):
        print(f"create user {u} success.")
    else:
        print(f"create user {u} fail.")


@user_cli.command('ch-passwd')
@click.option('--u', prompt='User name', help='User name')
@click.option('--p', hide_input=True, prompt='New password', help='New Password')
def create_user(u, p, e, r):
    """Change User Password"""
    u_data = {
        'username': u,
        'password': p,
        'email': e,
        'role': r
    }
    if UDao.add_user(u_data):
        print(f"create user {u} success.")
    else:
        print(f"create user {u} fail.")
