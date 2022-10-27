import click
import sys


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    # UI
    if ctx.invoked_subcommand is None:
        from {{cookiecutter.slug}} import main

        sys.exit(main.main())