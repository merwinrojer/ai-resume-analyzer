import json
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def get_cached_analysis(resume_id: int):
    cached_data = redis_client.get(f"resume_analysis:{resume_id}")

    if cached_data:
        return json.loads(cached_data)

    return None


def set_cached_analysis(resume_id: int, data: dict):
    redis_client.set(
        f"resume_analysis:{resume_id}",
        json.dumps(data),
        ex=3600
    )