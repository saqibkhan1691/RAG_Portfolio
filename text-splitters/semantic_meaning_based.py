from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    embedding=OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",    ## This is the type of threshold to use for identifying breakpoints. The "standard_deviation" option uses the standard deviation of the embeddings to determine breakpoints, while the "mean" option uses the mean of the embeddings.
    breakpoint_threshold_amount=1  ## This is the number of standard deviations away from the mean that a breakpoint must be to be considered significant. A higher value will result in fewer breakpoints being identified, while a lower value will result in more breakpoints being identified.
)

sample = """
Farmers were struggling to make ends meet due to the unpredictable weather patterns that affected their crops. The government introduced new policies to support sustainable farming practices, which included subsidies for organic fertilizers and training programs for modern agricultural techniques. As a result, many farmers were able to increase their yields and improve their livelihoods, contributing to the overall growth of the agricultural sector in the region. The Indian Premier League (IPL) also played a significant role in promoting sports and providing entertainment to millions of fans across the country. The league's popularity has led to increased investment in cricket infrastructure and talent development, further boosting the sport's growth in India.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)