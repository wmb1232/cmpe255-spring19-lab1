users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0
    name = ''
    for u in users:
        if u.get('id') == user:
            name = u.get('name')
    for x in friendship:
        if x[0] == user or x[1] == user:
            count += 1
        else:
            continue
    #print('{} has {} friends'.format(name, count))
    return count


def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    ex. Dunn has 4 friends

    '''
    rank = {}
    names = {}
    for u in users:
        names[u.get('id')] = u.get('name')
        rank[u.get('name')] = num_friends(u.get('id'))
        sorted_by_value = sorted(rank.items(), key=lambda sorted_rank: sorted_rank[1], reverse=True)

    for value in sorted_by_value:
        print('{} has {} friends'.format(value[0], value[1]))
    print('\n')


sort_by_num_friends()