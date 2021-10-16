class Job(object):
    """Job to put in the job queue."""

    def __init__(self, url, current_depth=None, max_depth=5):
        self.url = url
        self.current_depth = current_depth
        self.max_depth = max_depth

    def __repr__(self):
        return f"<Job: {self.url}>"

