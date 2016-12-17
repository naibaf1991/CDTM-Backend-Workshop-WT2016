class Task(object):
    allowed_stati = ['normal','completed']
    def __init__(self,id,title,list,status,description,due,revision):
        self.id = id
        self.title = title
        self.list = list
        if status in self.allowed_stati:
            self.status = status
        else:
            self.status = 'normal'
        self.description = description
        self.due = due
        self.revision = revision