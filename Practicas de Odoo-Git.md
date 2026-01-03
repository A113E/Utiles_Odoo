# Buenas practicas para Git Odoo[TIPO] módulo: descripción breve

- Detalle 1 del cambio
- Detalle 2 del cambio
- Fix #123 (si arregla un issue)

TIPOS comunes:
[ADD] → Nueva funcionalidad
[IMP] → Mejora de existente
[FIX] → Corrección de bug
[REF] → Refactorización
[MOV] → Mover código
[REM] → Eliminar código

# Configurar Debug VS CODE Odoo 14

# Archivo settings:

{
"python.useBundledDebugpy": false,

    "python.analysis.extraPaths": [
        "C:\\Odoo14\\server\\odoo",
        "C:\\Odoo14\\server\\addons",
        "C:\\Odoo14\\server\\custom-addons"
    ],

    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/.git": true
    },

    "xml.fileAssociations": [
        {
            "pattern": "**/views/*.xml",
            "systemId": "https://raw.githubusercontent.com/odoo/odoo/14.0/odoo/addons/base/data/ir_ui_view.xsd"
        }
    ]

}

# Archivo launch:

{
"version": "0.2.0",
"configurations": [
{
"name": "Odoo 14 (Debug)",
"type": "python",
"request": "launch",
"python": "C:/Odoo14/venv/Scripts/python.exe",
"program": "C:/Odoo14/server/odoo-bin",
"args": [
"--config=C:/Odoo14/server/odoo.conf",
"--dev=all",
"--log-level=debug",
],
"console": "integratedTerminal",
"justMyCode": false,
"env": {
"PYTHONUNBUFFERED": "1"
}
}
]
}

# Instalar versión 2023 10.0 de Python

# Opcional:

pip uninstall debugpy
pip install debugpy==1.6.7
pip install watchdog
