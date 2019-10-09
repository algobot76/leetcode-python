from collections import deque, defaultdict


class Solution:
    def __init__(self):
        self.combs = defaultdict(list)

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(len(word)):
                self.combs[word[:i] + '*' + word[i + 1:]].append(word)

        start_queue = deque([(beginWord, 1)])
        end_queue = deque([(endWord, 1)])
        start_visisted = {beginWord: 1}
        end_visited = {endWord: 1}

        while start_queue and end_queue:
            start_word, dist = start_queue.popleft()
            for i in range(len(start_word)):
                temp = start_word[:i] + "*" + start_word[i + 1:]
                for word in self.combs[temp]:
                    if word in end_visited:
                        return dist + end_visited[word]
                    if word not in start_visisted:
                        start_visisted[word] = dist + 1
                        start_queue.append((word, dist + 1))

            end_word, dist = end_queue.popleft()
            for i in range(len(start_word)):
                temp = end_word[:i] + "*" + end_word[i + 1:]
                for word in self.combs[temp]:
                    if word in start_visisted:
                        return dist + start_visisted[word]
                    if word not in end_visited:
                        end_visited[word] = dist + 1
                        end_queue.append((word, dist + 1))

        return 0
