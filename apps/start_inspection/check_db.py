# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/19 9:06 下午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
import sys
from apps.main import db
from apps.models.user import User


def check_super_admin():
    # Check if admin is existed in db.
    try:
        user = User.query.filter_by(username='super_admin').first()
        # If user is none.
        if user is None:
            # Create admin user if it does not existed.
            user = User(username='super_admin', password='viAlDVjLiNxd23PAT66l',
                        email='help@zouri.net', user_role='super_admin')

            # Add user to session.
            db.session.add(user)
            # Commit session.
            db.session.commit()
            # Print admin user status.
            print("Super admin was set.")
        else:
            # Print admin user status.
            print("Super admin already set.")
    except Exception as e:
        print("databases connect Error!!!")
        print(e)
        sys.exit(1)