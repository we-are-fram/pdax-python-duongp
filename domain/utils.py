from datetime import datetime


SEQ_REPOSITORY = {}


def generate_sequence_id(entity):
    if entity not in SEQ_REPOSITORY:
        SEQ_REPOSITORY[entity] = 1

    current_sequence_id = SEQ_REPOSITORY[entity]
    SEQ_REPOSITORY[entity] += 1

    return current_sequence_id


def time_as_string(dt: datetime = None, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    if dt:
        return dt.strftime(fmt)

    return ""