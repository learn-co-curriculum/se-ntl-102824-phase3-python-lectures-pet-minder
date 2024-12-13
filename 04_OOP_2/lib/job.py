class Job:

    # SINGLE-SOURCE OF TRUTH
    all = []

    @classmethod
    def all_pets(cls):
        return [job.pet for job in cls.all]

    def __init__(self, time, duration, request, pet, handler):
        self.time = time
        self.duration = duration
        self.request = request
        self.pet = pet
        self.handler = handler
        self.__class__.all.append(self)

    def fee(self):
        return self.handler.hourly_rate * self.duration

    def __repr__(self):
        return f"<Job pet: {self.pet.name} | Handler: {self.handler.name}>"
