"""
Level definition - a list of the levels

Each level is a hash with 2 keys: obs for obstacles and floors for the floors

obs are a hash with 3 or 4 keys:
    * type (money, tree, grave, house, police)
    * floor (number 0 to 2)
    * x as a float between 0 and 1 to define where the obstacle is horizontally
    * if the obstacle is a police, then it needs a speed to set how fast the policeman moves

floors are a list of 3 lists, one for each floor. 
Each floor is a list of tuples that have a start and end position (defined as a fraction of 1) so that platforms (or holes) can be created)
"""
levels = [
        {
            'obs' : [
            {
                'type' : 'money',
                'floor' : 0,
                'x' : 0.5,
            },
            {
                'type' : 'tree',
                'floor' : 1,
                'x' : 0.3,
            },
            {
                'type' : 'grave',
                'floor' : 2,
                'x' : 0.75,
            } ],
            'floors' :
            [
                [(0,1)],
                [(0,1)],
                [(0,1)],
            ],
        },
        {
            'obs' : [
            {
                'type' : 'house',
                'floor' : 1,
                'x' : 0.3,
            },
            {
                'type' : 'money',
                'floor' : 0,
                'x' : 0.7,
            },
            {
                'type' : 'tree',
                'floor' : 1,
                'x' : 0.8,
            },
            {
                'type' : 'grave',
                'floor' : 2,
                'x' : 0.3,
            } ],
            'floors' :
            [
                [(0,0.35),(0.6,1)],
                [(0,1)],
                [(0,1)],
            ],
        },
        {
            'obs':
            [
            {
                'type' : 'grave',
                'floor' : 1,
                'x' : 0.8,
            },
            {
                'type' : 'police',
                'floor' : 0,
                'x' : 0.5,
                'speed' : 0.5,
            },
            {
                'type' : 'house',
                'floor' : 2,
                'x' : 0.5,
            },
            {
                'type' : 'money',
                'floor' : 2,
                'x' : 0.8,
            },
            ],
            'floors':
            [
                [(0,1)],
                [(0,0.3),(0.5,1)],
                [(0,1)],
            ]
        },
        {
            'obs':
            [
            {
                'type' : 'grave',
                'floor' : 0,
                'x' : 0.28,
            },
            {
                'type' : 'house',
                'floor' : 0,
                'x' : 0.67,
            },
            {
                'type' : 'police',
                'floor' : 1,
                'x' : 0.3,
                'speed' : 0.4,
            },
            {
                'type' : 'house',
                'floor' : 2,
                'x' : 0.5,
            },
            {
                'type' : 'money',
                'floor' : 1,
                'x' : 0.8,
            },
            {
                'type' : 'money',
                'floor' : 2,
                'x' : 0.3,
            },
            ],
            'floors':
            [
                [(0,1)],
                [(0,0.35),(0.55,1)],
                [(0,1)],
            ]
        },
]
