# -*- coding: utf-8 -*-
{
    # Información básica del módulo
    'name': 'Nombre del Módulo',
    'version': '14.0.1.0.0',  # Formato: version_odoo.mayor.menor.parche.build
    'category': 'Accounting/Accounting',  # Categorías comunes abajo
    'summary': 'Resumen corto del módulo (una línea)',
    'description': """
        Descripción detallada del módulo
        =================================
        
        Este módulo permite:
        -------------------
        * Funcionalidad 1
        * Funcionalidad 2
        * Funcionalidad 3
        
        Características principales:
        ---------------------------
        - Característica A
        - Característica B
        - Característica C
        
        Notas técnicas:
        --------------
        Información adicional relevante para desarrolladores
    """,
    
    # Información del autor/empresa
    'author': 'Tu Nombre o Empresa',
    'website': 'https://www.tuempresa.com',
    'maintainer': 'Nombre del Mantenedor',
    'license': 'LGPL-3',  # Opciones: LGPL-3, GPL-3, OPL-1, Other proprietary license
    
    # Dependencias
    'depends': [
        'base',           # Siempre necesario
        'account',        # Si trabajas con contabilidad
        'sale',           # Si trabajas con ventas
        'purchase',       # Si trabajas con compras
        'stock',          # Si trabajas con inventario
        'hr',             # Si trabajas con recursos humanos
        # Agrega otras dependencias según necesites
    ],
    
    # Siempre cargados
    'data': [
        # Seguridad (SIEMPRE primero)
        'security/security_groups.xml',           # Grupos de seguridad
        'security/ir.model.access.csv',           # Permisos de acceso
        'security/security_rules.xml',            # Reglas de registro
        
        # Datos maestros (segundo)
        'data/data.xml',                          # Datos iniciales
        'data/sequences.xml',                     # Secuencias
        'data/email_templates.xml',               # Plantillas de correo
        'data/cron_jobs.xml',                     # Tareas programadas
        
        # Vistas (tercero)
        'views/menu_views.xml',                   # Menús principales
        'views/modelo_views.xml',                 # Vistas de modelos
        'views/modelo2_views.xml',                # Más vistas
        'views/assets.xml',                       # Assets CSS/JS
        
        # Reportes (cuarto)
        'reports/report_templates.xml',           # Plantillas de reportes
        'reports/report_actions.xml',             # Acciones de reportes
        
        # Wizards (quinto)
        'wizards/wizard_views.xml',               # Vistas de wizards
    ],
    
    # Solo se cargan en modo demostración
    'demo': [
        'demo/demo_data.xml',
    ],
    
    # Assets web (JS, CSS, SCSS)
    'qweb': [
        'static/src/xml/template.xml',
    ],
    
    # Imágenes y recursos
    'images': [
        'static/description/icon.png',            # Ícono del módulo (debe ser 256x256)
        'static/description/banner.png',
    ],
    
    # Configuración adicional
    'installable': True,              # Si el módulo es instalable
    'application': False,             # True si es una aplicación principal, False si es módulo
    'auto_install': False,            # True si se instala automáticamente cuando se cumplen dependencias
    'active': False,                  # Deprecado, usar installable
    
    # Precio (si es módulo de pago en Odoo Apps)
    'price': 0.00,
    'currency': 'USD',
    
    # URLs externas
    'external_dependencies': {
        'python': [
            # 'requests',             # Librerías Python requeridas
            # 'pandas',
        ],
        'bin': [
            # 'wkhtmltopdf',          # Binarios requeridos
        ]
    },
    
    # Información para Odoo Apps Store
    'live_test_url': 'https://demo.tuempresa.com',
    'support': 'soporte@tuempresa.com',
}


# =============================================================================
# CATEGORÍAS MÁS COMUNES (para el campo 'category'):
# =============================================================================
# 'Accounting/Accounting'          - Contabilidad
# 'Sales/Sales'                    - Ventas
# 'Inventory/Inventory'            - Inventario
# 'Purchase'                       - Compras
# 'Human Resources'                - Recursos Humanos
# 'Manufacturing'                  - Manufactura
# 'Project'                        - Proyectos
# 'Services/Project'               - Servicios/Proyectos
# 'Marketing'                      - Marketing
# 'Point of Sale'                  - Punto de Venta
# 'Website'                        - Sitio Web
# 'Customizations'                 - Personalizaciones
# 'Hidden'                         - Oculto (para módulos técnicos)
# 'Technical'                      - Técnico

# =============================================================================
# LICENCIAS DISPONIBLES:
# =============================================================================
# 'LGPL-3'    - GNU Lesser General Public License v3.0 (Más común para Odoo)
# 'GPL-3'     - GNU General Public License v3.0
# 'AGPL-3'    - GNU Affero General Public License v3.0
# 'OPL-1'     - Odoo Proprietary License (para módulos comerciales)
# 'Other proprietary license' - Otras licencias propietarias

# =============================================================================
# FORMATO DE VERSIÓN (Recomendado):
# =============================================================================
# {version_odoo}.{major}.{minor}.{patch}.{build}
# Ejemplo: 14.0.1.0.0
#   14.0  = Versión de Odoo
#   1     = Versión mayor (cambios significativos)
#   0     = Versión menor (nuevas funcionalidades)
#   0     = Parche (correcciones de bugs)
#   0     = Build (opcional)

# =============================================================================
# ORDEN DE CARGA RECOMENDADO EN 'data':
# =============================================================================
# 1. security/          (Grupos y permisos)
# 2. data/              (Datos maestros, secuencias)
# 3. views/             (Vistas, menús)
# 4. reports/           (Reportes)
# 5. wizards/           (Asistentes)

# =============================================================================
# NOTAS IMPORTANTES:
# =============================================================================
# - El archivo debe llamarse __manifest__.py (Odoo 10+) o __openerp__.py (Odoo 9-)
# - Debe estar en la raíz del módulo
# - La codificación UTF-8 es obligatoria
# - Los archivos XML deben cargarse en el orden correcto para evitar errores
# - Siempre incluye 'base' en depends