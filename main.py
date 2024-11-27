from decorators.time_measure_decor import time_measure


def get_numbers_from_file(file):
    """ Open the text file and read its content and returns as a list"""
    try:
        with open(file, "r") as file:
            return file.read().split('\n')
    except FileNotFoundError as error:
        print(f"File {file} not found")
        return []



def first_two_dict(numbers):
    """ Creates dict with first two numbers as keys and values are numbers"""
    first_two_dict = {}
    for num in numbers:
        key = str(num)[:2]
        if key in first_two_dict:
            first_two_dict[key].append(num)  # Append to the existing list
        else:
            first_two_dict[key] = [num]
    return first_two_dict


@time_measure
def get_longest_chain(numbers, dict_numbers):
    """Main logic for searching longest chain"""
    longest_chain = []

    # For each starting number, explore all chains
    for num in numbers:
        start_number = num
        stack = [(start_number, [start_number])]  # Stack to manage the chains

        while stack:
            current_number, current_chain = stack.pop()

            # Get the last two digits of the current number to find possible continuations
            key = current_number[-2:]
            if key in dict_numbers:
                # Explore all possible next numbers for this key
                for next_number in dict_numbers[key]:
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
    return longest_chain

def fix_chain(chain):
    """Manage answer to string"""
    result = str(chain[0])
    for i in range(1, len(chain)):
        result += str(chain[i])[2:]
    return result


def main():
    file_path = "numbers.txt"
    numbers = get_numbers_from_file(file_path)
    two_dict = first_two_dict(numbers)
    longest_chain = get_longest_chain(numbers, two_dict)
    result = fix_chain(longest_chain)
    print(f"Longest chain length: {len(longest_chain)} numbers")
    print(f'Result: {result}')
    print(f'There are {len(result)} characters in result')


if __name__ == "__main__":    # pragma: no cover
    main()
