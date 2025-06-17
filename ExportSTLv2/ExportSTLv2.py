# This is an add-on for Autodesk Fusion that exports the active design to an STL file.
# It saves the file to the user's Desktop with the design's name, not including the version number.
# Created by: Tommi Lehtomaa aka Catrik.
# License: MIT License

import adsk.core, adsk.fusion, traceback, os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        # Get the ExportManager from the active design.
        exportMgr = design.exportManager
        
        desktopDir = os.path.join(os.path.expanduser('~'), 'Desktop')

        # Get the name of the currently active component and remove the version number
        designName = design.activeComponent.name.split(' v')[0]

        # Create an STLExportOptions object and do the export.
        stlOptions = exportMgr.createSTLExportOptions(design.rootComponent, os.path.join(desktopDir, f'{designName}.stl'))
        res = exportMgr.execute(stlOptions)
        
        ui.messageBox(f'Design exported to: {os.path.join(desktopDir, f"{designName}.stl")}')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))