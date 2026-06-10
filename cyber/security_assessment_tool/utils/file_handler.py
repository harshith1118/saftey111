import hashlib

def calculate_sha256(file):
    """
    Calculate the SHA256 hash of an uploaded file.
    """
    sha256_hash = hashlib.sha256()
    # Read the file in chunks to handle large files efficiently
    for byte_block in iter(lambda: file.read(4096), b""):
        sha256_hash.update(byte_block)
    
    # Reset file pointer after reading
    file.seek(0)
    return sha256_hash.hexdigest()

def validate_file_type(filename):
    """
    Check if the file extension is allowed (.exe, .zip, .pdf).
    """
    allowed_extensions = {'.exe', '.zip', '.pdf'}
    import os
    _, ext = os.path.splitext(filename.lower())
    return ext in allowed_extensions
