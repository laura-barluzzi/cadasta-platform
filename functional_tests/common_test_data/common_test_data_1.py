import random


def get_test_data():

    def get_rand_bool():
        return random.randrange(2) == 1

    test_data = {}

    # Define 1 superuser and 9 other users
    users = []
    users.append({
        'username': 'superuser',
        'password': 'password3',
        '_is_superuser': True,
    })
    for uid in range(1, 10):
        users.append({
            'username': 'default' + str(uid),
            'password': 'password1',
        })
    test_data['users'] = users
    test_data['superuser'] = users[0]

    # Define 2 orgs and their members
    test_data['orgs'] = [
        {
            'name': "UNESCO",
            'slug': 'unesco',
            'description': (
                "United Nations Educational, Scientific, " +
                "and Cultural Organization"
            ),
            'logo': (
                'https://upload.wikimedia.org/wikipedia/commons/' +
                'thumb/b/bc/UNESCO_logo.svg/320px-UNESCO_logo.svg.png'
            ),
            '_members': (1, 2, 3, 4),
            '_admins': (1,),
        },
        {
            'name': "UNICEF",
            'slug': 'unicef',
            'description': "United Nations Children's Emergency Fund",
            '_members': (5, 6, 7, 8),
            '_admins': (5,),
        },
    ]

    # Define 4 projects and their user roles
    test_data['projects'] = [
        {
            'name': "Project Gutenberg",
            'slug': 'project-gutenberg',
            'description': (
                "Public project of UNESCO."
                if get_rand_bool() else ''
            ),
            'country': ('PH' if get_rand_bool() else ''),
            'access': 'public',
            '_org': 0,
            '_managers': (2, 3),
        },
        {
            'name': "Wikipedia",
            'slug': 'wikipedia',
            'description': (
                "Private project of UNESCO."
                if get_rand_bool() else ''
            ),
            'country': ('AT' if get_rand_bool() else ''),
            'access': 'private',
            '_org': 0,
            '_managers': (4,),
        },
        {
            'name': "OpenStreetMap",
            'slug': 'openstreetmap',
            'description': (
                "Public project of UNICEF."
                if get_rand_bool() else ''
            ),
            'country': ('DE' if get_rand_bool() else ''),
            'access': 'public',
            '_org': 1,
            '_managers': (6, 7),
        },
        {
            'name': "Linux Kernel",
            'slug': 'linux-kernel',
            'description': (
                "Private project of UNICEF."
                if get_rand_bool() else ''
            ),
            'country': ('KE' if get_rand_bool() else ''),
            'access': 'private',
            '_org': 1,
            '_managers': (8,),
        },
    ]

    return test_data
