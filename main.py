import typer
from signal import signal, SIGINT

from commands.new_tab import _new_tab

from console import Console

from schema import Item

from utils import catch_exit_application

app = typer.Typer()


@app.command()
def new_tab() -> None:
    Console.log(message='Adding a new tab...')
    _new_tab()
    Console.log(message='Finished adding the new tab!')


@app.command()
def query_tab():
    tab_name = typer.prompt('Tab name',
                            confirmation_prompt=True,
                            hide_input=False)
    Console.log(message=f'Querying tab with name {tab_name}...')


if __name__ == '__main__':
    signal(SIGINT, catch_exit_application)
    Console.start_message()
    while True:
        app()
