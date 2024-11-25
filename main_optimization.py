from datetime import datetime


start = datetime.now()

# Open the text file and read its content
with open("numbers.txt", "r") as file:
    content = file.read()

# Split the content into a list of numbers
numbers_list = content.split('\n')

print(numbers_list)

# Set dict with first two numbers as keys
first_two_dict = {}

for num in numbers_list:
    key = str(num)[:2]
    if key in first_two_dict:
        first_two_dict[key].append(num)  # Append to the existing list
    else:
        first_two_dict[key] = [num]

print(first_two_dict)

# All chains
longest_chain = []

# For each starting number, explore all chains
for num in numbers_list:
    start_number = num
    stack = [(start_number, [start_number])]  # Stack to manage the chains

    while stack:
        current_number, current_chain = stack.pop()

        # Get the last two digits of the current number to find possible continuations
        key = current_number[-2:]

        if key in first_two_dict:
            # Explore all possible next numbers for this key
            for next_number in first_two_dict[key]:
                if next_number not in current_chain:  # Avoid loops by not revisiting numbers in the current chain
                    new_chain = current_chain + [next_number]
                    stack.append((next_number, new_chain))  # Add the new chain to stack

                    # Update longest chain if the new chain is longer
                    if len(new_chain) > len(longest_chain):
                        longest_chain = new_chain
        else:
            # If no further matches, check the chain length (not stored anymore)
            if len(current_chain) > len(longest_chain):
                longest_chain = current_chain

# Manage answer to string
result = str(longest_chain[0])
for i in range(1, len(longest_chain)):
    result += str(longest_chain[i])[2:]

finish = datetime.now()

func_time = finish - start

print(len(longest_chain))

print(f'Time for execution is {round(func_time.total_seconds(),2)} seconds')

print(f'Result: {result}')