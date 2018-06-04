from django.test import TestCase

# Create your tests here.
a=[{'permissions__url': '/users/',
  'permissions__group_id': 1,
  'permissions__action': 'list'},

 {'permissions__url': '/users/add/',
  'permissions__group_id': 1,
  'permissions__action': 'add'},

 {'permissions__url': '/users/delete/(\\d+)',
  'permissions__group_id': 1,
  'permissions__action': 'delete'},

 {'permissions__url': 'users/edit/(\\d+)',
  'permissions__group_id': 1,
  'permissions__action': 'edit'},

 {'permissions__url': '/roles/',
  'permissions__group_id': 2,
  'permissions__action': 'list'}

 ]

