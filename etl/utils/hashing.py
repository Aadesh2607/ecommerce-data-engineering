import hashlib


def generate_hash(value):
    """
    Generate SHA256 hash.
    """

    return hashlib.sha256(str(value).encode()).hexdigest()


def dataframe_hash(df):
    """
    Hash an entire dataframe.
    """

    return hashlib.sha256(df.to_csv(index=False).encode()).hexdigest()
