# Lockboxes problem

## 1. OVERVEIW

Imagine you're in a large office building where each room represents a lockbox. To enter a room, you need a key that matches the room's number. You start in room 0, which is already open, and inside each room, there are keys to other rooms (lockboxes).

The goal is to figure out if you can eventually enter every room in the building. You can only move to a new room if you have the key to it, and you can only get more keys by entering new rooms and checking what's inside.


### Now, let's walk through the scenarios given in your problem statement:

For the first example with ``boxes = [[1], [2], [3], [4], []]``:

- You start in room 0 and find a key to room 1.
- You go to room 1 and find a key to room 2.
- In room 2, you find a key to room 3.
- You enter room 3 and find a key to room 4.
- Finally, you use the key to enter room 4, which is empty.
- You've managed to open all rooms, so the function should `return True`.

In the second example with ``boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]``:

- Start in room 0 and find keys to rooms 1, 4, and 6.
You can directly go to room 1, find a key to room 2, and open it.
- Inside room 2, you find keys to rooms 0, 4, and 1, but you've already opened those.
- Then you go to room 4, find a key to room 3, and open it.
You can also go to room 6, but it doesn't help you open new rooms.
- Room 3 is now accessible, and inside you find keys to rooms 5 and 6, which you can now open.
- Room 5 also has keys to rooms 4 and 1, but those are already open.
- All rooms have been opened, so the function should `return True`.

For the final example with ``boxes = [[1, 4], [2], [3], [], [1], [6], []]``:

- Start in room 0, find keys to rooms 1 and 4.

- In room 1, find a key to room 2.

- In room 2, find a key to room 3.

- Room 3 has no keys.

- Room 4 is accessible from room 0's key but only contains a key to room 1, which we've already opened.

- Rooms 5 and 6 cannot be accessed because we haven't found their keys.

In this revised scenario, the function would `return False` because rooms 5 and 6 remain locked, and we have no way to access them. This demonstrates a situation where not all rooms can be unlocked with the available keys.


## Analogy:


Here's a step-by-step approach to solve the problem:

- Begin by unlocking Box 0 and collecting its keys.

- Track which boxes you've unlocked and which keys you currently have.

- Use the keys you have to unlock more boxes, collecting new keys as you go.

- Continue this process until you either unlock all boxes or cannot unlock any new ones.

- If you unlock all boxes, return True; if there are still locked boxes and you have no keys to unlock them, return False.

## Python Method Implementation:

```py
def canUnlockAll(boxes):

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

```
## Test Results Explanation:

The first list of boxes [[1], [2], [3], [4], []] returns True because each box contains the key to the next box, and all boxes can be sequentially unlocked.

The second list of boxes [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]] also returns True as there are enough keys to unlock all boxes even though the keys are not in sequential order.

The third list of boxes [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]] returns False because box 5, which is required to unlock box 6, cannot be unlocked (there is no key for box 5 in the available keys).

This method should correctly determine if all boxes can be opened for any given configuration of keys within the boxes.