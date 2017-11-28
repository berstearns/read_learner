def evalQFunc(state):
	return Q

def move(state):
	state[0][-1] = 3
	return state

def stop_criteria(state):
	if state[0][-1] == 3:
		return True
	else:
		return False

def simulate(initial_state):
	last_state = initial_state
	it_state = initial_state
	i = 0
	while(not stop_criteria(it_state)):
		it_state = move(it_state)
		i+=1
		print(i)

i_state = [ [3,1,1,1,1,2],[0,0,0,0,0,0],[0,0,0,0,0,0]]
simulate(i_state)
