class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the Programming Language."""
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"

# In the client code
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the string representation of each language
print(python)
print(ruby)
print(visual_basic)

# Create a list of ProgrammingLanguage objects
languages = [python, ruby, visual_basic]

# Print the names of all dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)