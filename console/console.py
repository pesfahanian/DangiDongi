import typer

from console.messages import Messages


class Console:
    white = typer.colors.WHITE
    green = typer.colors.GREEN
    magenta = typer.colors.MAGENTA

    @classmethod
    def Info(cls) -> None:
        typer.secho('Info:\t'.rstrip('\n'), fg=cls.green, bold=True, nl=False)

    @classmethod
    def _Info(cls) -> None:
        return typer.secho('\nInfo:\t'.rstrip('\n'),
                           fg=cls.green,
                           bold=True,
                           nl=False)

    @classmethod
    def log(cls, message: str) -> None:
        cls.Info()
        typer.secho(message, fg=cls.white, bold=True)

    @classmethod
    def confirmation(cls) -> None:
        confirm = typer.confirm(Messages.Confirm)
        return confirm

    @classmethod
    def start_message(cls) -> None:
        cls.Info()
        typer.secho(Messages.Start, fg=cls.magenta, bold=True)

    @classmethod
    def exit_message(cls) -> None:
        cls._Info()
        typer.secho(Messages.Exit, fg=cls.magenta, bold=True)
