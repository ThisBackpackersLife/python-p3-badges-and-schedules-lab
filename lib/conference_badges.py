def badge_maker(name):
    return f"Hello, my name is { name }."

def batch_badge_creator(names):
    # batch_names = []
    # for name in names:
    #     batch_names.append( f"Hello, my name is { name }." )
    # return batch_names
    return [ f'Hello, my name is { name }.' for name in names ]


def assign_rooms(names):
    # assigned_rooms = []
    # for i, name in enumerate( names, start=1 ):
    #     message = f"Hello, { name }! You'll be assigned to room { i }!"
    #     assigned_rooms.append( message )
    # return assigned_rooms
    return [ f"Hello, { name }! You'll be assigned to room { i }!" for i, name in enumerate( names, start=1 )]

def printer(names):
    for name in batch_badge_creator( names ):
        print( name )
    
    for room in assign_rooms( names ):
        print( room )