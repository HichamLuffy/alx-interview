#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status = [200, 301, 400, 401, 403, 404, 405, 500]
status_codes = {str(code): 0 for code in status}
line_count = 0


def print_stats():
    """Function to print the statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(signum, frame):
    """Signal handler for printing the stats before exiting."""
    print_stats()


# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        try:
            # Split the line by double quotes to isolate the parts we need
            parts = line.split('"')
            if len(parts) > 1:
                # Further split the first part to extract IP,
                # date and the last part for status and size
                ip_date_part = parts[0].split()
                status_size_part = parts[2].strip().split()

                if len(ip_date_part) > 1 and len(status_size_part) > 1:
                    ip = ip_date_part[0]
                    date = ip_date_part[1].strip('[]')
                    status = status_size_part[0]
                    size = status_size_part[1]
                    # Update the total size and the status code count
                    # if status and size are valid
                    if status.isdigit() and size.isdigit():
                        total_size += int(size)
                        if status in status_codes:
                            status_codes[status] += 1
                    else:
                        continue  # Skip the line if status
                        # or size are not valid numbers
                else:
                    # Skip the line if the parts do not contain enough elements
                    continue
            else:
                # Skip the line if it does not follow the expected format
                continue

            # Increment the line counter after processing
            line_count += 1

            # After every 10 lines, print the statistics
            if line_count % 10 == 0:
                print_stats()

        except Exception as e:
            # If any other exception occurs, skip the line
            continue


except KeyboardInterrupt:
    # If we get a keyboard interrupt, print the stats before exiting
    print_stats()
    pass

# Print the final stats if we didn't exit due to a keyboard interrupt
print_stats()
