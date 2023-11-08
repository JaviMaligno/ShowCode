class Trader:
    def fill_pattern(self, pattern, contracts):
        if not pattern:
            return 0
        if not contracts:
            return sum(a*10 for a in pattern)
        # Convert contracts to binary format
        contracts_bin = [sum(1 << i for i, x in enumerate(contract) if x == 'X') for contract in contracts]

        # Initialize the minimum cost and the coverage
        self.min_cost = float('inf')
        coverage = [0] * len(pattern)

        # Define the recursive function
        def dfs(cost, coverage):
            # Calculate the total coverage
            total_coverage = sum(coverage)

            # Update the minimum cost
            self.min_cost = min(self.min_cost, cost + (sum(pattern) - total_coverage) * 10)

            # Try all contracts
            for contract in contracts_bin:
                # Calculate the new coverage
                new_coverage = coverage.copy()
                if all(pattern[i] - new_coverage[i] >= (contract & (1 << i) > 0) for i in range(len(pattern))):
        # If yes, add the contract to the coverage
                    for i in range(len(pattern)):
                        new_coverage[i] = min(pattern[i], new_coverage[i] + (contract & (1 << i) > 0))

                # Only continue if the new coverage is greater than the old coverage
                if sum(new_coverage) > total_coverage:
                    dfs(cost + 1, new_coverage)

        # Call the recursive function
        dfs(0, coverage)

        # Return the minimum cost
        return self.min_cost



