

from itertools import chain

def flatten_and_sort(arr):
    flatten = lambda lst: list(chain.from_iterable(lst))
    sort = lambda lst: sorted(lst)
    return sort(flatten(arr))

example_array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flatten_and_sort(example_array)
print(result)

# How does this solution ensure data immutability?
# - The solution ensures data immutability by not modifying any input data. 
#   The functions `flatten` and `sort` create and return new lists rather than 
#   altering the original input list. All operations result in new data being produced,
#   which adheres to the principle of immutability.

# Is this solution a pure function? Why or why not?
# - Yes, this solution is a pure function because it always produces the same output 
#   given the same input, and it does not cause any side effects (such as modifying 
#   external variables or printing to the console within the function). The functions 
#   do not rely on or alter any state outside of their scope, making them pure.

# Is this solution a higher order function? Why or why not?
# - No, the `flatten_and_sort` function itself is not a higher-order function. 
#   A higher-order function is a function that either takes another function 
#   as an argument or returns a function as its result. In this case, 
#   `flatten_and_sort` only uses lambda functions internally but does not 
#   take a function as an argument or return one.

# Would it have been easier to solve this problem using a different programming style?
# - It might have been easier to solve this problem using an imperative programming style, 
#   where you would iterate over the list and accumulate the results in a mutable list, 
#   and then sort that list. However, the functional approach offers a more declarative 
#   style, focusing on "what" the function should do rather than "how" to do it.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# - Functional programming is helpful in this case because it promotes the use of 
#   pure functions and immutability, which lead to more predictable and testable code. 
#   Since the functions do not have side effects or rely on external state, 
#   reasoning about the code becomes simpler. Additionally, combining small, 
#   reusable functions (like flatten and sort) makes the code more modular 
#   and easier to maintain or extend.



#OBJECT ORIENTED PROMPT

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

podracer = Podracer(500, "perfect", 1000)
anakin_pod = AnakinsPod(700, "perfect", 1500)
anakin_pod.boost()
sebulba_pod = SebulbasPod(600, "perfect", 1200)
sebulba_pod.flame_jet(podracer)

print(f"Anakin's Pod: Speed = {anakin_pod.max_speed}, Condition = {anakin_pod.condition}")
print(f"Sebulba's Pod: Speed = {sebulba_pod.max_speed}, Condition = {sebulba_pod.condition}")
print(f"Generic Podracer: Speed = {podracer.max_speed}, Condition = {podracer.condition}")


# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# Encapsulation:
# - This solution demonstrates encapsulation by bundling the data (attributes like max_speed, condition, and price)
#   and the methods (repair, boost, flame_jet) that operate on that data within classes. This keeps the internal
#   representation of the podracers hidden and provides a controlled interface for interacting with them.

# Abstraction:
# - Abstraction is shown by the `Podracer` class which represents a general concept of a podracer. The specific
#   details of how `boost` or `flame_jet` methods work are abstracted away in the `AnakinsPod` and `SebulbasPod`
#   classes, allowing users to interact with these objects without needing to understand their internal workings.

# Inheritance:
# - Inheritance is used here with the `AnakinsPod` and `SebulbasPod` classes, which inherit from the `Podracer` class.
#   This allows these specific types of podracers to reuse the code from the `Podracer` class while adding their own
#   specialized methods (`boost` and `flame_jet`), demonstrating the reusability aspect of OOP.

# Polymorphism:
# - This solution does not explicitly demonstrate polymorphism as the classes do not override shared methods in a
#   polymorphic way. However, polymorphism could be applied if there were methods that could be overridden in 
#   the child classes with different implementations.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# - It might have been possible to implement a solution using a different coding style, such as procedural programming,
#   but it would likely result in more repetitive and less organized code. Without OOP, managing different types of
#   podracers and their specific behaviors would require more conditional logic and global state management, making the
#   code harder to maintain and extend.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# - Object-Oriented Programming assisted in this problem by allowing the definition of a clear structure for podracers 
#   and their specific behaviors. Inheritance reduced redundancy by enabling the reuse of the `Podracer` class's 
#   attributes and methods. Encapsulation ensured that the details of the podracer's attributes and methods were kept 
#   together, making the code more modular and easier to manage. The ability to define specific behaviors in the child 
#   classes (`boost` and `flame_jet`) while still sharing a common structure from the `Podracer` class made the solution 
#   both flexible and organized.        




#REFLECTION

#Is one of these coding paradigms "better" than the other? Why or why not?
#They both have their uses and it depends on overal architecture the developer is aiming for. 

#Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
#They both seem about the same, neither is more appealing than the other because they both have their ups and downs

#Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
#I think you'll use both. Functional will be good for small static methods/functions which may be used in multiple places
#While object oriented programming may be better for architecturing larger systems

#Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
#They both are easy to understand. You can only deepen your understanding by writing more applications with them.

