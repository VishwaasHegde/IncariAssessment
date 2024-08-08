from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from components.incari_util import IncariUtil
from fastapi import FastAPI

class ChatData(BaseModel):
    requirement: str

class EvaluationData(BaseModel):
    actual: str
    predicted: str


app = FastAPI()


# Add the CORS middleware with the allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later change this to "origins"
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)

@app.post("/chat")
async def code_chat_api(body: ChatData):
    """
    Returns the sequence of nodes in string format
    :param body: request body
    :type body: CharData
    :return: response from the LLM (sequence of nodes)
    :rtype: dict
    """
    requirement = body.requirement
    incari_util = IncariUtil()
    response = incari_util.generate_nodes(requirement)

    return {'response': response}


@app.post("/evaluate")
async def evaluate(body: EvaluationData):
    """
    Evaluates the prediction
    :param body: request body for evaluation
    :type body: EvaluationData
    :return: Scores for bleu, rouge and minimum edit distance
    :rtype: dict
    """
    actual = body.actual
    predicted = body.predicted
    incari_util = IncariUtil()
    bleu_score, rouge_score, ed_score = incari_util.evaluate_score(actual, predicted)

    return {'response': {'BLEU': bleu_score, 'ROUGE': rouge_score, 'EDIT_DISTANCE': ed_score}}