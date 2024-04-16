#!/usr/bin/python3
""" Lock boxes """


def canUnlockAll(boxes):
    """check README for more understanding"""
    unlocked_rooms = [0]  # Start with room 0 unlocked
    keys = set(boxes[0])  # Start with keys from room 0

    # As long as we have keys to try, continue
    while keys:
        new_keys_added = False  # Flag to track if we find new keys

        # Copy the keys to a list to avoid modifying the set while iterating
        for key in list(keys):
            # If the key corresponds to a locked room, unlock it
            if key not in unlocked_rooms and key < len(boxes):
                unlocked_rooms.append(key)  # Add room to the list of unlocked rooms
                keys.update(boxes[key])     # Add new keys from the unlocked room
                keys.remove(key)            # Remove the used key
                new_keys_added = True       # Set flag to True as we found new keys

        # If no new keys were added and rooms remain locked, break the loop
        if not new_keys_added:
            break

    # Check if the number of unlocked rooms matches the total number of rooms
    return len(unlocked_rooms) == len(boxes)

