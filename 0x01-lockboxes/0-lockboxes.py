#!/usr/bin/python3



def canUnlockAll(boxes):
    unlocked_boxes = set([0])  # Starting with box 0 unlocked
    keys = set(boxes[0])       # Starting with keys from box 0

    # Continue while we have keys to try
    while keys:
        # Track if we made progress in this iteration
        made_progress = False

        # Try to unlock boxes with the keys we have
        for key in list(keys):  # List conversion to avoid RuntimeError
            if key < len(boxes) and key not in unlocked_boxes:
                # Unlock the box with the current key
                unlocked_boxes.add(key)
                # Add new keys from the unlocked box
                keys.update(boxes[key])
                # Since we used this key, remove it from our keyring
                keys.remove(key)
                # Mark progress
                made_progress = True

        # If no progress is made and keys remain, they cannot unlock new boxes
        if not made_progress:
            break

    # If all boxes are unlocked, return True
    return len(unlocked_boxes) == len(boxes)
