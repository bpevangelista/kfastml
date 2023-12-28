import uuid
from datetime import datetime

from fastapi.responses import JSONResponse

from kfastml.engine.inference_engine import InferenceTaskResult


def gen_request_id(api_name: str) -> str:
    return f'{api_name}_{uuid.uuid4().hex}'


def build_json_response(request_id: str, job_result: InferenceTaskResult) -> JSONResponse:
    return JSONResponse({
        'created': f'{datetime.now()}',
        'id': request_id,

        'finished_reason': job_result.finished_reason,
        'result': job_result.result,
    })