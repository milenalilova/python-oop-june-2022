class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.memory_used = 0
        self.apps = []
        self.is_on = False

    def install(self, app, memory):
        memory_left = self.memory - self.memory_used
        if memory_left > memory and self.is_on:
            self.apps.append(app)
            self.memory_used += memory
            return f'Installing {app}'
        if memory_left > memory and not self.is_on:
            return f'Turn on your phone to install {app}'

        return f'Not enough memory to install {app}'

    def power(self):
        self.is_on = not self.is_on

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory - self.memory_used}'


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
