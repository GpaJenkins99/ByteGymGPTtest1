import contextlib
import io
import flet as ft

def main(page: ft.Page):
    page.title = "Byte Gym"
    page.scroll = ft.ScrollMode.AUTO

    def go_to_lesson(e):
        page.clean()

        title = ft.Text("Lesson 1: Print in Python", size=24, weight="bold")
        instructions = ft.Text("Type your Python code belo try : print('Hello, Byte Gym!')",size=16)

        code_input = ft.TextField(
            label="Your code",
            multiline=True,
            min_lines=5,
            max_lines=10,
            expand=True,
        )
        output_display = ft.Text(value="", selectable=True)
        def run_code(e):
            buffer = io.StringIO()
            try:
                with contextlib.redirect_stdout(buffer):
                    exec(code_input.value, {})
                output_display.value = buffer.getvalue()
            except Exception as err:
                output_display.value = f"Error: {err}"
            page.update()

        run_button = ft.ElevatedButton("Run Code", on_click=run_code)

        lesson_content = ft.Column(
            controls=[
                title,
                instructions,
                code_input,
                run_button,
                ft.Text("Output:"),
                output_display,
            ],
            expand=True,
        )

        page.add(
            title,
            instructions,
            code_input,
            run_button,
            ft.Text("Output:"),
            output_display,
        )
        page.add(lesson_content)

    #Home Page
    welcome_text = ft.Text("Welcome to Byte Gym", size=30)
    start_button = ft.ElevatedButton("Start Learning", on_click=go_to_lesson)

    home = ft.Column([welcome_text, start_button], alignment=ft.MainAxisAlignment.CENTER, expand=True)
    page.add(home)

    page.add(welcome_text, start_button)

ft.app(target=main)