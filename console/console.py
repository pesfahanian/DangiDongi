import typer

from console.messages import Messages


class Console:
    red = typer.colors.RED
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
    def Error(cls) -> None:
        typer.secho('Error:\t'.rstrip('\n'), fg=cls.red, bold=True, nl=False)

    @classmethod
    def log(cls, message: str) -> None:
        cls.Info()
        typer.secho(message, fg=cls.white, bold=False)

    @classmethod
    def error(cls, message: str) -> None:
        cls.Error()
        typer.secho(message, fg=cls.white, bold=False)

    @classmethod
    def start_message(cls) -> None:
        cls.Info()
        typer.secho(Messages.Start, fg=cls.magenta, bold=True)

    @classmethod
    def exit_message(cls, reason: str, nl: bool) -> None:
        if nl:
            cls._Info()
        else:
            cls.Info()
        typer.secho(f'{reason} {Messages.Exit}', fg=cls.magenta, bold=True)
