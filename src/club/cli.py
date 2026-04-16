"""

Authors
-------
Alberto Zancanaro <alberto.zancanaro@uni.lu>

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import typer

from . import club

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Inizialize the main app
app = typer.Typer(
    name = "club",
    help = "A CLI wrapper for the caveman compression tool. Use 'club llm', 'club mlm' or 'club nlp' for the respective compression methods.",
    epilog = "For more information, visit https://github.com/jesus-333/club and https://github.com/wilpel/caveman-compression"
)

# Register the command as cli command
app.command("llm")(club.club_llm)
app.command("mlm")(club.club_mlm)
app.command("nlp")(club.club_nlp)
app.command("compress")(club.club_compress)
app.command("decompress")(club.club_decompress)

if __name__ == "__main__" :
    app()
