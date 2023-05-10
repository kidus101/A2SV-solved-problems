class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        in_degrees = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        queue = collections.deque()
        result = []
        
        for supply in supplies:
            in_degrees[supply] = 0
            queue.append(supply)
        
        
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                in_degrees[recipe] += 1

        while queue:
            node = queue.popleft()
            if node in recipes:
                result.append(node)
            
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
            
        return result