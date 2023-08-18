from MCSL2Lib.publicFunctions import isDarkTheme

class SPEIconsSetter:
    def Undo() -> str:
        return (
            ":/speIcons/Undo_White.svg" if isDarkTheme() else ":/speIcons/Undo_Black.svg"
        )

    def Redo() -> str:
        return (
            ":/speIcons/Redo_White.svg" if isDarkTheme() else ":/speIcons/Redo_Black.svg"
        )

class SPEVariables:
    speVersion = "1.0.0"
    undoDict = {}
    redoDict = {}