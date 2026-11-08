from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# write python code in text variable
text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name

    def is_passing(self):
        return self.grade >= 6.0

# Example usage
# student1 = Student("Alice", 15, 8.5)
# print(student1.get_details())  # Output: Alice
# print(student1.is_passing())   # Output: True        

"""

splitter = RecursiveCharacterTextSplitter.from_language(
##  language=Language.PYTHON, # Language.PYTHON is used to split the text based on the structure of the Python code, such as classes, methods, and comments
    language=Language.MARKDOWN, # Language.MARKDOWN is used to split the text based on the structure of the Markdown document, such as headings, paragraphs, and code blocks
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

print(f"Number of chunks: {len(chunks)}")
print(chunks)