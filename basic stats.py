def basic_stats(data):

    def mean(data):
        return sum(data) / len(data)
    
    def median(data):
        sorted_data = sorted(data) # Sorts the data in ascending order
        n = len(sorted_data) # Calculates the length of sorted data
        mid = n // 2 # finds the middle index
        if n % 2 == 0:
            return (sorted_data[mid-1] + sorted_data[mid]) / 2 # If n is even median is the average of the two middle values
        else:
            return sorted_data[mid] # If n is odd median is the middle value.
        
    def mode(data):
        frequency = {} # Empty dictionary to store how often each number appears
        for num in data: # Loops to see if number is in dataset
            if num in frequency: # Loops to see if the number is in dictionary or not
                frequency[num] += 1 # If it is in the dictionary already increase count by one
            else:
                frequency[num] = 1 # If not add a count of 1
        max_freq = max(frequency.values()) # Finds highest frequency of occurrences in the dictionary.
        modes = [key for key, val in frequency.items() if val == max_freq] # Creates a list of all numbers that occurs max_freq times.
        if len(modes) == 1: # If there is only one mode
            return modes[0] # return the single mode
        return modes # If multiple return a list of modes
    
    def variance(data):
        mean_value = mean(data)
        return sum((x - mean_value) ** 2 for x in data) / len(data) # Calculates the squared difference between each value in the data and the mean and then summed.
    
    def standard_deviation(data):
        return variance(data) ** 0.5
    
    stats = {
        "Mean": mean(data),
        "Median": median(data),
        "Mode": mode(data),
        "Variance": variance(data),
        "Standard Variance": standard_deviation(data)
    }

    return stats

# Sample data
data = [1, 2, 2, 3, 4, 4, 4, 5, 6]

statistics = basic_stats(data)

for stat, value in statistics.items():
    print(f"{stat}: {value}")