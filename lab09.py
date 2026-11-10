# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.

def two_sum(nums, target):
    # Outline (write your plan here first):
    # Use a nested for loop to compare pairs of numbers in nums.
    # Start with the first number and compare it with every number after it.
    # If no matching sum is found, move to the next number and repeat the process.
    # Only compare numbers that come after the current number to avoid checking the same pair twice.
    # When a pair adds up to target, return the indices of the two numbers.
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    pass

def max_profit(prices):
    # Outline:
    # Start by setting the maximum profit to 0.
    # Use a nested for loop to compare each buying day with every day that comes after it.
    # Calculate the profit by subtracting the buying price from the selling price.
    # If the calculated profit is greater than the maximum profit, update the maximum profit.
    # Return the maximum profit after checking all possible pairs.
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def max_subarray(nums):
    # Outline:
    # Check if nums contains only one number. If so, return that number.
    # Set the maximum sum to the first number in nums.
    # Use a nested for loop to check every possible contiguous block of numbers.
    # Start at each index and keep adding the numbers that come after it.
    # If the current sum is greater than the maximum sum, update it.
    # Return the maximum sum after checking all possible blocks.
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    if len(nums) == 1:
        return nums[0]
    max_sum = nums[0]
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # Create an empty list to keep track of opening brackets.
    # Create a dictionary matching each opening bracket to its closing bracket.
    # Loop through each character in s.
    # If the character is an opening bracket, add it to the list.
    # If the character is a closing bracket, check if the list is empty.
    # Check if the closing bracket matches the most recent opening bracket.
    # If they don't match, return False.
    # If they match, remove the opening bracket.
    # Return True if the list is empty after checking all characters.
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    already_checked = []
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for item in s:
        if item in brackets:
            already_checked += [item]
        elif item in ")]}":
            if len(already_checked) == 0:
                return False
            opening = already_checked[-1]
            if brackets[opening] != item:
                return False
            already_checked = already_checked[:-1]
    return len(already_checked) == 0

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass

if __name__ == "__main__":
    main()