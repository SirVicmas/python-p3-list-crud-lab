# Function to create an empty list
def create_an_empty_list():
    return []

# Function to create a list with four elements
def create_a_list():
    return [1, 5, 8, 5]

# Function to add an element to the end of a list and return the updated list
def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    return my_list

# Function to add an element to the start of a list
def add_element_to_start_of_list(my_list, element):
    my_list.insert(0, element)

# Function to remove the last element from a list
def remove_element_from_end_of_list(my_list):
    my_list.pop()

# Function to remove the first element from a list
def remove_element_from_start_of_list(my_list):
    del my_list[0]

# Function to retrieve the first element from a list
def retrieve_first_element_from_list(my_list):
    return my_list[0]

# Function to retrieve an element from a specific index in a list
def retrieve_element_from_index(my_list, index):
    if index < len(my_list):
        return my_list[index]
    else:
        return None  # Return None if the index is out of bounds

# Function to retrieve the last element from a list
def retrieve_last_element_from_list(my_list):
    if len(my_list) > 0:
        return my_list[-1]
    else:
        return None  # Return None if the list is empty

