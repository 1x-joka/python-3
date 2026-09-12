# ============== Explaining the topics ==============
# -> The AI agent must explore possible actions/states to find a solution to a problem how make the requisited task, from how go point A to B to make a tic-tac-toe to seek one way how movement he will be. = Search
# -> Our AI will be able to know and represented our informations, and more, extract inferences to informations, use his informations and draw conclusions aditionals. = Knowledge
# -> What happened when the computer haven't sure of the fact or have sure embasement in probability.  =Uncertainty
# -> When exists various ways to resolve the problem/requisition and the computer have to think the better way, if it's possible. = Optimization
# -> Make the computer learning with datas, based on the information given, what’s the best thing to do for execute the task getting better and better with based on datas (ex.: spam box in email). = Machine Learning
# -> Computational models composed of interconnected layers of units that learn patterns from data by adjusting weights = Neural Networks
# -> Studying the human languagens and how the computer understand it. = Language

# ============== SEARCH 1 ==============
# -> Ex.: Sliding Puzzle Game (the task is alining all number for his stay aligned in corret order)
# -> Ex2.: Finding the Exit in Labirint (the task is search a way for exit the stay 0 and reach the goal)
# -> Ex3.: Routes Google Maps (like a labirint)
# -> agent: entity that perceives its environment and acts upon that environment (ex.: person who trying to resolve the puzzle or car in google maps)
# -> state: a configuration of the agent and its environment (ex.: anyway state of the numbers on puzzle)
# -> initial state: the state in which the agent begins
# -> actions: choices that can be made in a state (how is our next pass to resolve the problem)
    # -> actions: function ACTIONS(s) returns the set of actions that can be executed in state "s" (ex.: 4 actions in puzzle game: up, down, left and right)
# -> transition model: a description of what state results from performing any applicable action in any state (how states and actions relate to each other)
    # -> transition model: function RESULTS(s, a) returns the state resulting from performing action "a" in state "s" (ex.: see the actual state of puzzle (matrix or two-dimensional matrix to our numbers) and sliding the number 2 for left; the results is the actual state after alter)
    # -> visually representing: the circles is states and arrows is actions
# -> goal test: way to determinate whether a given state is a goal state (for our AI know when "arrived")
# -> path cost: numerical cost associated with a given path (a way to represent the "cost" of this action, to know the numerical cost associated with a particular sequence of actions. A basic problem can have 1 solution, how the puzzle, but complexs problems can have multiples solutions, and the computer decided the better solution through the prices/costs/values assigned of each way)
# -> solution: a sequence of actions that leads from the initial state to a goal state (regardless of the difficulty, time or mistakes)
# -> optimal solution: a solution that has the lowest path cost among all solutions (in complexs problems, can have multiple optimal solutions, but a optimal solution it just means there was no way to have done better in terms of searching)

# ============== NODE ==============
# -> a data structure that keeps track of: a state, a parent (node that generated this node), an action (action applied to parent to get node) and a path cost (registed all the values from initial state to node)

# ============== APPROACH ==============
# -> Start with a frontier that contains the initial state
# -> Start with an empty explored set (why are the states who we explored? initially empty, we use this for keep a record of what we've already explored, that is, so we don't get stuck in an endless cycle of actions, like in the sliding puzzle, I can move piece A to the right and then back to the left endlessly, so we use this to avoid it)
# -> Repeat:
    # -> If the frontier is empty, then no solution (exists problems who the AI don't think how resolve, and is it normal)
    # -> Remove a node from the frontier
        # -> If node contains goal state, return the solution
        # -> Add the node to the explored set
        # -> Expand node (see all the "neighboors" of this node, consider all the possible actions I could take from the state this node represents and which nodes I could go to from there), add resulting nodes to the frontier if they aren't already in the frontier of the explored set
# -> frontier is a collection of nodes that have been discovered but have not yet been explored.

# ============== STACK ==============
# -> last-in-first-out data type = LIFO (the first thing i add in frontier who the last thing i removed, in this case, this thing is the node who i explored)
    # -> in this case, we are could storaged all the frontiers explored and recued if the route is wrong and finish exploring the other options)

# ============== DEPTH-FIRST SEARCH (DFS) ==============
# -> search algorithm that always expands the deepest node in the frontier
# -> explore a path until you reach a conclusion (less memory than BFS, but it does not guarantee the optimal solution)

# ============== BREADTH-FIRST SEARCH (BFS) ==============
# -> search algorithm that always expands the shallowest node in the frontier
# -> explore both paths until you reach a conclusion (the closest)

# ============== QUEUE ==============
# -> first-in-first-out data type

# ============== SEARCH 2 ==============
# -> uninformed search: search strategy that uses no problem-specific knowledge
# -> informed search: search strategy that uses problem-specific knowledge to find solutions more efficiently
# -> greedy best-first search: search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)