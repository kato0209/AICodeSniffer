if s == "": return s # получена через curr_cash = self._descendance_cash[curr] answer = curr_cash.get(s, None) if answer is not None: return answer # для послучения, перед дублируем код res = curr for a in s: res = self.graph[res][self.alphabet_codes[a]]