curr_agenda = [(self.root, [], 0)] for i, a in enumerate(s): next_agenda = [] for curr, borders, cost in curr_agenda: if cost >= max_count: <extra_id_0> <extra_id_1> = self.graph[curr][self.alphabet_codes[a]]