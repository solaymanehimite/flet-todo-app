from flet import *

class Task(UserControl):

  def __init__(self, input_text, remove_task):
    super().__init__()
    self.input = input_text
    self.remove_task = remove_task

  def build(self):
    self.checkbox = Checkbox(label=self.input,
                             expand=True)
    self.field = TextField(value=self.input,
                             expand=True,
                             border_width=0)
    
    self.TaskView = Row(
      visible=True,
      controls=[
        self.checkbox,
        IconButton(icon=icons.CREATE, on_click=self.edit_clicked),
        IconButton(icon=icons.DELETE, on_click=self.remove_clicked),
      ]
    )
    
    self.EditView = Row(
      visible=False,
      controls=[
        self.field,
        IconButton(icon=icons.CHECK, on_click=self.save_clicked)
      ]
    )

    return Column(
      controls=[
        self.TaskView,
        self.EditView
      ]
    )

  def edit_clicked(self, e):
    self.TaskView.visible = False
    self.EditView.visible = True
    self.update()

  def remove_clicked(self, e):
    self.remove_task(self)

  def save_clicked(self, e):
    self.checkbox.label = self.field.value
    self.TaskView.visible = True
    self.EditView.visible = False
    self.update()

class ToDo(UserControl):
  
  def build(self):
    self.input = TextField(hint_text='Task name', border_width=0)
    self.tasks = Column()

    view = Column(
      horizontal_alignment=CrossAxisAlignment.CENTER,
      controls=[
        Text(value='To-Do app', theme_style=TextThemeStyle.HEADLINE_LARGE),
        Row(
          alignment=MainAxisAlignment.SPACE_BETWEEN,
          controls=[
            self.input,
            IconButton(icon=icons.ADD, on_click=self.add_clicked)
          ]
        ),
        self.tasks
      ]
    )

    return view

  def add_clicked(self, e):
    if self.input.value:
      task = Task(self.input.value, self.remove)
      self.tasks.controls.append(task)
      self.input.value = ''
    self.update()
  
  def remove(self, task):
    self.tasks.controls.remove(task)
    self.update()

def main(page: Page):

  page.window_width = 400
  page.window_height = 600

  todo = ToDo()

  page.add(todo)

app(target=main)