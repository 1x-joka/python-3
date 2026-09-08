# ============== Explaining the topics ==============
# -> The AI must search in every ways how make the requisited task, from how go point A to B to make a tic-tac-toe to seek one way how movement he will be. = Search
# -> Our AI will be able to know and represented our informations, and more, extract inferences to informations, use his informations and draw conclusions aditionals. = Knowledge
# -> What happened when the computer haven't sure of the fact or have sure embasement in probability.  =Uncertainty
# -> When exists various ways to resolve the problem/requisition and the computer have to think the better way, if it's possible. = Optimization
# -> Make the computer learning with datas, based on the information given, what’s the best thing to do for execute the task getting better and better with based on big datas (ex.: spam box in email). = Machine Learning
# -> Aproximing the computer to a human in decisions, resolutions, etc. = Neural Networks
# -> Studying the human languagens and how the computer understand it. = Language

# ============== SEARCH (PROBLEMS) ==============
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
# -> path cost: numerical cost associated with a given path (a way to represent the "cost" of this action, to know how difficult or later is. A basic problem can have 1 solution, how the puzzle, but complexs problems can have multiples solutions, and the computer decided the better solution through the prices/costs/values assigned of each way)
# -> solution: a sequence of actions that leads from the initial state to a goal state (regardless of the difficulty, time or mistakes)
# -> optimal solution: a solution that has the lowest path cost among all solutions (in complexs problems, can have multiple optimal solutions, but a optimal solution it just means there was no way to have done better in terms of searching)

# ============== NODE ==============