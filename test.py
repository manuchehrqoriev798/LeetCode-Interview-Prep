def solve(pos, dir, idx, commands):
    if idx == len(commands):
        return {pos}

    positions = set()

    if commands[idx] == 'F':
        positions |= solve(pos + dir, dir, idx + 1, commands)
        positions |= solve(pos - dir, -dir, idx + 1, commands)
    elif commands[idx] == 'R':
        positions |= solve(pos, -dir, idx + 1, commands)
        positions |= solve(pos, dir, idx + 1, commands)  # Allow staying still after turning
    else:  # 'L'
        positions |= solve(pos, dir, idx + 1, commands)
        positions |= solve(pos, -dir, idx + 1, commands)  # Allow staying still after turning

    return positions

def count_possible_positions(commands):
    positions = set()

    for i in range(len(commands)):
        original_command = commands[i]
        for c in ['F', 'L', 'R']:
            if c != original_command:
                modified_commands = commands[:i] + c + commands[i+1:]
                positions |= solve(0, 1, 0, modified_commands)

    positions.discard(0)

    return len(positions)

# Input reading and function call
N = int(input())
commands = input().strip()

print(count_possible_positions(commands))
