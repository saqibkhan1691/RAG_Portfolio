from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration is the ongoing discovery and exploration of celestial structures in outer space by means of continuously evolving and growing space technology.

While the study of space is carried out mainly by astronomers with telescopes, the physical exploration of space is conducted both by unmanned robotic probes and human spaceflight.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # In text structured based splitting if chunk size is small then it try to split the text into characters and if chunk size is large then it try to split the text into paragraphs.
    chunk_overlap=20
)

# Split the text into chunks
chunks = splitter.split_text(text)

print(f"Number of chunks: {len(chunks)}")
print(chunks)