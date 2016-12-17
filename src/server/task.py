class Task(object):
    allowed_stati = ['normal','completed']

    def __init__(self, title, list, id='', status=allowed_stati(0), description='', due='', revision=1):
        self.id = id
        self.title = title
        self.list = list
        self.status = status
        self.description = description
        self.due = due
        self.revision = revision