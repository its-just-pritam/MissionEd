{
    'name': "MissionEd Placement",
    'version': '1.0',
    'depends': ['base'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/placement_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'author': "MissionEd Developers Team",
    'category': 'Website',
    'website': 'https://missioned-forum.web.app/welcome',
    'description': """
    A PLacement portal by MissionEd to bring together recruitters and candidates.
    """,
    'application': True,
    'installable': True,
    'summary': 'Placement Portal',
    "company": 'MissionEd',
    "license" : 'LGPL-3',
    
}