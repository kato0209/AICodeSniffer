
        order, stack = [], []
        stack.append(trie.root)
        colors = ['white'] * len(trie)
        while len(stack) > 0:
            index = stack[-1]
            color = colors[index]
            if color == 'white': # вершина ещё не обрабатывалась
                colors[index] = 'grey'
                for child in