import sys

# Node: State inside the search
class Node():
    def __init__(self, state, parent, action):
        self.state = state # current state / where we are currently
        self.parent = parent # which Node we came from
        self.action = action # action we took to arrive at this state

    # Example: state = (1, 1) -> action = "right"

# StackFrontier() = A collection of Nodes who: 1. it's already been found; 2. haven't been explored
class StackFrontier():
    def __init__(self):
        self.frontier = [] # for storage the nodes

    # Add a new node in last of list
    def add(self, node):
        self.frontier.append(node)

    # Check if any node inside of the list has the state we are looking for
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier) # any return True if at least one element meets the condition
    
        # Example: frontier = [Node A, Node B, Node C] -> contains_state((2, 3)) -> if any node has state = (2, 3) return True

    # Check if the list is empty
    def empty(self):
        return len(self.frontier) == 0 # if not have nodes = True

    # Before remove a node, checking if frontier is empty. If not, remove the last element in list (LIFO)
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] # -1 = the last element
            self.frontier = self.frontier[:-1] # :-1 = take all the elements except the last
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# Represents and manages the maze
class Maze():
    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1: # count how many times "A" appears in the file
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines() # divide the text in lines
            # Example: "####\n" and "A B#\n" turn ["####", "A B#"]

        self.height = len(contents) # how many lines of labirint
        self.width = max(len(line) for line in contents) # determine the width of labirint

        # Keep track of walls
        self.walls = [] # each line goes represented one list
        for i in range(self.height): # go through every line of the maze
            row = [] # actually line
            for j in range(self.width): # go through column line of the maze
                try:
                    if contents[i][j] == "A": # the initial position
                        self.start = (i, j) # save the starting position
                        row.append(False) # isn't a wall
                    elif contents[i][j] == "B": # the objective
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ": # clear path
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError: # Some lines might be shorter than others. If we try to access a position that doesn't exist, we'll get an IndexError
                    row.append(False)
            self.walls.append(row) # Before end one line, add her in list of walls

        self.solution = None # initially haven't a solution

    def print(self):
        solution = self.solution[1] if self.solution is not None else None # if exists a solution (self.solution = (actions, cells)) [1] take only "cells"
        print()
        for i, row in enumerate(self.walls): # go through each line
            for j, col in enumerate(row): # go through each column
                if col: # if it's a wall
                    print("â–ˆ", end="")
                elif (i, j) == self.start: # if we are in initial position
                    print("A", end="")
                elif (i, j) == self.goal: # if we are in last position
                    print("B", end="")
                elif solution is not None and (i, j) in solution: # if this position belongs a solution, we put "*" for show the way founded
                    print("*", end="")
                else:
                    print(" ", end="")
            print() # before finished one line, go for other
        print()

    def neighbors(self, state):
        row, col = state # the actual position
            # Example: state = (3, 5) -> line 3 column 5

        # Create all possible actions from the current position
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = [] # list who storage only the valid ways

        # Check all possibilities
        for action, (r, c) in candidates: # go through
            # r >= 0: we can't go out the top
            # r < self.height: we can't go out the down
            # c >= 0 and c < self.width: we can't go out the sides
            # not self.walls[r][c]: the position can't be a wall

            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c))) # if the movement is valid, we add in list "result"
                    # Example: ("right", (3, 6))
        return result # return to us all the possible moves

    def solve(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state = self.start, parent = None, action = None) # creating a node corresponding to the initial state
        frontier = StackFrontier() # we choose who search strategy we would use (DFS or BFS)
        frontier.add(start) # add the initial state in frontier

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier (don't have any nodes to explore), then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal: # we arrived?
                actions = [] # here goes put the realized actions
                cells = [] # here goes put the positions travelled

                while node.parent is not None: # We start at the goal and go back through the parents until we reach the initial state. Inverse way
                    actions.append(node.action) # storaged the action who led to the current Node
                    cells.append(node.state) # actually position
                    node = node.parent # return to previous node

                # reversing again because we took the opposite path in the previous While
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells) # storaged the solution who found
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state): # get all valid neighboring states from the current state
                if not frontier.contains_state(state) and state not in self.explored: # only add the new state if: 1. He isn't at the frontier yet; 2.He haven't been explored
                    
                    # Create a new child Node.
                    # state = the new state
                    # parent = the current node
                    # action = the action taken from the current node to the new state
                    child = Node(state = state, parent = node, action = action)
                    frontier.add(child) # put the new node on frontier

    def output_image(self, filename, show_solution = True, show_explored = False):
        from PIL import Image, ImageDraw # for create and draw an image
        cell_size = 50 # for cell in labirint is 50x50 pixels
        cell_border = 2 # space to separated visualy the cells

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size), # the dimension depends the size of labirint
            "black"
        )
        draw = ImageDraw.Draw(img) # used object to draw in imagem

        solution = self.solution[1] if self.solution is not None else None # take the cells belonging to the solution
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col: # if this cells is a wall = True
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution: # if the cell belonging the solution and show_solution is True = paint this cell as part of the path
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored: # ff we want to show the explored states and this cell has been explored: colour the cell to indicate it has been visited
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw retangle belonging of the cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename) # save the image in file specifying

# sys.argv contains the arguments passed by the terminal
    # Example: Terminal = python maze.py maze1.txt; Python = sys.argv[0] = "maze.py" and sys.argv[1] = "maze1.txt"

# if haven't 2 elements
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt") # end the program

# create an object Maze using the file provided by the user in the terminal
m = Maze(sys.argv[1])

# show the original labirint
print("Maze:")
m.print()

# start the search
print("Solving...")
m.solve()

print("States Explored:", m.num_explored) # all the explorated nodes before to find the solution

# show again the labirint but, now, resolved
print("Solution:")
m.print()

# create an image called "maze.png"
m.output_image("maze.png", show_explored=True) # "show_explored = True" -> it means we also want to see the states that were explored during the search.