class Median:
    # Inicializator with a list of numbers (input)
    def __init__(self, numbers):
        self.numbers = numbers

    # Sorting the list with a bubble sort algorithm
    def bubble_sort(self):
        n = len(self.numbers)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]

    # Calculating the median - different approaches with odd and even numbers
    def calculate_median(self):
        self.bubble_sort()
        n = len(self.numbers)
        mid = n // 2
        
        if n % 2 == 0:
            return (self.numbers[mid - 1] + self.numbers[mid]) / 2
        else:
            return self.numbers[mid]

if __name__ == "__main__":
    while True:
        try:
            # User input for numbers separated by space
            user_input = input("Enter numbers separated by space: ")
            numbers = list(map(float, user_input.split()))  # Allow decimal numbers
            break
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")
    
    calculator = Median(numbers)
    median = calculator.calculate_median()
    print(f"Your median is: {median}")
