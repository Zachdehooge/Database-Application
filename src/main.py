import sqlite3
import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def databaseadd(databasename: Annotated[str, typer.Option("", help="Database name")] = "default.sqlite"):
    """
        Command for creating a new database // default database if left empty is "default.sqlite"

        Usage: databasecreate <databasename>
    """

    conn = sqlite3.connect(f'{databasename}')

    conn.commit()

    conn.close()


@app.command()
def databasedelete(databasename: Annotated[str, typer.Argument("")] = "default.sqlite"):
    """
        Command for deleting a database // default database if left empty is "default.sqlite"
    """

    print(f"Deleting database {databasename}")
    # pathlib.Path(f'{databasename}.sqlite').unlink()


@app.command()
def tableadd(databasename: Annotated[str, typer.Option("{databasename}", help="Database name")] = "default.sqlite",
                tablename: Annotated[str, typer.Option("{tablename}", help="Table name")] = "default_table",
                columnname: Annotated[str, typer.Option("{columnname}", help="Column name")] = "default",
                datatype: Annotated[str, typer.Option("{datatype}", help="DataType name")] = "TEXT"
                ):
    """
        Command for creating a table in a database // default table if left empty is "default"
    """

    conn = sqlite3.connect(f"{databasename}")
    c = conn.cursor()
    # Create table
    c.execute(f'''CREATE TABLE if not exists "{tablename}" ("{columnname}" "{datatype}")''')

    conn.commit()

    conn.close()


@app.command()
def columnadd(databasename: Annotated[str, typer.Option("{databasename}", help="Database name")] = "default.sqlite",
              tablename: Annotated[str, typer.Option("{tablename}", help="Table name")] = "default_table",
              columnname: Annotated[str, typer.Option("{columnname}", help="Column name")] = "default",
              datatype: Annotated[str, typer.Option("{datatype}", help="DataType name")] = "TEXT"
              ):
    """
        Command for adding a column in a database
    """

    conn = sqlite3.connect(f"{databasename}")
    c = conn.cursor()
    # TODO: Implement a way to pass multiple column args, if not then while loop
    # Create table
    c.execute(f'''ALTER TABLE "{tablename}" ADD COLUMN "{columnname}" "{datatype}"''')

    conn.commit()

    conn.close()


@app.command()
def columndelete(databasename: Annotated[str, typer.Option("{databasename}", help="Database name")] = "default.sqlite",
                 tablename: Annotated[str, typer.Option("{tablename}", help="Table name")] = "default_table",
                 columnname: Annotated[str, typer.Option("{columnname}", help="Column name")] = "default",
                 datatype: Annotated[str, typer.Option("{datatype}", help="DataType name")] = "TEXT"
                 ):
    """
        Command for deleting a column in a database
    """

    conn = sqlite3.connect(f"{databasename}")
    c = conn.cursor()
    # Create table
    c.execute(f'''ALTER TABLE "{tablename}" DROP COLUMN "{columnname}"''')

    conn.commit()

    conn.close()


@app.command()
def valueadd(databasename: Annotated[str, typer.Option("{databasename}", help="Database name")] = "default.sqlite",
             tablename: Annotated[str, typer.Option("{tablename}", help="Table name")] = "default_table",
             columnname: Annotated[str, typer.Option("{columnname}", help="Column name")] = "default",
             value: Annotated[str, typer.Option("{value}", help="DataType name")] = ""
             ):
    """
        Command for adding a value in a table
    """

    conn = sqlite3.connect(f"{databasename}")
    c = conn.cursor()
    # Create table
    c.execute(f'''INSERT INTO "{tablename}" ("{columnname}") VALUES ("{value}")''')

    conn.commit()

    conn.close()


@app.command()
def valuedelete(databasename: Annotated[str, typer.Option("{databasename}", help="Database name")] = "default.sqlite",
                tablename: Annotated[str, typer.Option("{tablename}", help="Table name")] = "default_table",
                columnname: Annotated[str, typer.Option("{columnname}", help="Column name")] = "default",
                value: Annotated[str, typer.Option("{value}", help="DataType name")] = ""
                ):
    """
        Command for removing a value in a table
    """

    conn = sqlite3.connect(f"{databasename}")
    c = conn.cursor()
    # Create table
    c.execute(f'''DELETE FROM "{tablename}" WHERE ("{columnname}") = ("{value}")''')

    conn.commit()

    conn.close()


@app.command()
def tabledelete(databasename: Annotated[str, typer.Option("{databasename}", help="Database name")] = "default.sqlite",
                tablename: Annotated[str, typer.Option("{tablename}", help="Table name")] = "default_table"):
    """
        Command for deleting a table in a database // default table if left empty is "default"
    """

    conn = sqlite3.connect(f"{databasename}")
    c = conn.cursor()

    # Create table
    c.execute(f'''DROP TABLE IF EXISTS {tablename}''')

    conn.commit()

    conn.close()


# TODO: Implement inserting values to a column

# TODO: Implement dropping values from a table

# TODO: Implement persistence with the application after a command is run (while loop)

app()
