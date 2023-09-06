import cProfile
import memory_profiler
import resource.sample as sample
import contextlib
# import sys

# Function to run and profile space complexity
@memory_profiler.profile
def profile_space_complexity():
    n = 10000
    sample.some_function(n)

def determine_complexity(n):
    # You can make an educated guess about the complexity here
    # based on your analysis of the code.
    if n > 1000:
        return "O(n^2)"
    else:
        return "O(n)"

if __name__ == "__main__":
    # Redirect stdout to a file
    with open("Output/result.txt", "w") as f:
        with contextlib.redirect_stdout(f):
            print("Time Complexity:")
            # This will print a detailed time complexity analysis
            # of the some_function() in sample.py to result.txt
            cProfile.run("sample.some_function(10000)", sort='cumulative')

            print("\nSpace Complexity:")
            # This will print a detailed space complexity analysis
            # of the some_function() in sample.py to result.txt
            profile_space_complexity()

            # Determine and print the complexity notation
            complexity = determine_complexity(10000)
            print(f"\nComplexity Notation (educated guess): {complexity}")

    print("Time and space complexity analysis results saved to result.txt.")
