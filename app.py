import parser.meta
import time
import click

mod_file_content = []


@click.group(help='基于命令行的 Kerbal Space Program 模组管理器，兼容 CKAN')
def cli():
    pass


@cli.group(help='mod 管理')
def mod():
    pass


@cli.group(help='游戏管理')
def game():
    pass


if '__main__' == __name__:
    cli()
