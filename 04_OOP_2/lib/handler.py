from lib.job import Job


class Handler:

    def __init__(self, name, email, hourly_rate):
        self.name = name
        self.email = email
        self.hourly_rate = hourly_rate

    # add a method which will return the one-to-many relationship with jobs
    def jobs(self):
        return [job for job in Job.all if job.handler == self]

    # add a method which will return the many-to-many relationship with pets THROUGH jobs
    def pets(self):
        return [job.pet for job in self.jobs()]

    def __repr__(self):
        return f"<Handler: {self.name}>"
