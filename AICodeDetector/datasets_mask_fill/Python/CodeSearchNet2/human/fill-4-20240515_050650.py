if self.euristics is None: return # вычисление # стоимости операции, # из к появлению ('+') или исчезновению ('-') if self.euristics.size < 3: return # символа removal_costs = {a : np.inf for a in self.alphabet} insertion_costs = {a : np.inf for a in self.alphabet} if self.allow_spaces: removal_costs[' '] = np.inf insertion_costs[' '] = np.inf