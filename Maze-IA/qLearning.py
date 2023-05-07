import numpy as np
import csv
from constants import *

def read_csv():
    states = []
    file = open("vertex.csv", "r")
    reader = csv.reader(file, delimiter=";")
    for state in reader:
        aux = state[1].strip().replace("(", "").replace(")", "").replace(" ","").split(',')
        states.append((int(aux[0]), int(aux[1])))
    file.close()
    return states

def is_terminal_state(current_row, current_column):
    if rewards[current_row][current_column] == -1:
        return False
    else:
        return True
    
def get_starting_location():
    current_row = np.random.randint(rows)
    current_column = np.random.randint(columns)
    while is_terminal_state(current_row, current_column):
        current_row = np.random.randint(rows)
        current_column = np.random.randint(columns)
    return current_row, current_column

def get_next_action(current_row, current_column, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row, current_column])
    else:
        return np.random.randint(4)
    
def get_next_location(current_row, current_column, action_index):
    new_row = current_row
    new_column = current_column
    if actions[action_index] == 'up' and current_row > 0:
        new_row -= 1
    elif actions[action_index] == 'right' and current_column < columns - 1:
        new_column += 1
    elif actions[action_index] == 'down' and current_row < rows -1:
        new_row += 1
    elif actions[action_index] == 'left' and current_column > 0:
        new_column -= 1
    return new_row, new_column

def get_path(star_row, start_column):
    if is_terminal_state(star_row, start_column):
        return []
    else:
        current_row, current_column = star_row, start_column
        path = []
        path.append((current_row, current_column))
        while not is_terminal_state(current_row, current_column):
            action_index = get_next_action(current_row, current_column, 1)
            current_row, current_column = get_next_location(current_row, current_column, action_index)
            path.append((current_row, current_column))
        return path
    
# Variaveis Gerais
epsilon = 0.9
discount_factor = 0.9
learning_rate = 0.9


# Definindo o ambiente
rows = 12
columns = 16
q_values = np.zeros((rows, columns, 4))
#print(q_values)

# Definindo ações
# 0 -> up, 1 -> right, 2 -> down, 3 -> left
actions = ['up', 'right', 'down', 'left']

# Definindo Recompensas -> Estados pintados = -100; Estados em branco = -1; Estado final = 100
rewards = np.full((rows, columns), -100)
states = read_csv()

for state in states:
    position = list(state)
    rewards[position[0]][position[1]] = -1

rewards[row_final][col_final] = 100

for episode in range(1000):
    row_index, column_index = get_starting_location()
    while not is_terminal_state(row_index, column_index):
        action_index = get_next_action(row_index, column_index, epsilon)
        old_row_index, old_column_index = row_index, column_index
        row_index, column_index = get_next_location(row_index, column_index, action_index)

        reward = rewards[row_index, column_index]
        old_q_value = q_values[old_row_index, old_column_index, action_index]
        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, column_index])) - old_q_value

        new_q_value = old_q_value + (learning_rate * temporal_difference)
        q_values[old_row_index, old_column_index, action_index] = new_q_value


list_tuple = get_path(0, 0)
with open('Outputs/qLearning_path.txt', 'w') as file:
    for tuple in list_tuple:
        file.write(str(tuple) + '\n')
