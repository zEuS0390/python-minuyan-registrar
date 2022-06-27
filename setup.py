from cx_Freeze import setup, Executable
import sys

setup(
    name="Minuyan Registrar Program",
    version="0.1",
    description="Minuyan National High School formerly Goldenville HS - 307505 Registrar Program",
    options={
        "build_exe": {
            "packages":["os"],
            "excludes":["tkinter"],
            "includes":[
                "PyQt5",
                "sqlalchemy",
                "sqlalchemy.sql.default_comparator",
                "sqlalchemy.dialects.sqlite"
            ],
            "include_files":[
                ("cfg/app.cfg", "cfg/app.cfg")
            ],
            "optimize": 2
        }
    },
    executables=[
        Executable(
            script="main.py",
            target_name="minuyanreg.exe",
            base="Win32GUI" if sys.platform == "win32" else None,
            icon="img/icons/main.ico"
        )
    ]
)