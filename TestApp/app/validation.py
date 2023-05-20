from config import GPT_CHUNKS_SIZE


def chunks_size_validation(chunk_size):
    if chunk_size > GPT_CHUNKS_SIZE:
        raise ValueError
    return chunk_size
