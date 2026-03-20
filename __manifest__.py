# -*- coding: utf-8 -*-

{
    'name': 'AI Agent Manager',
    'version': '4.0',
    'category': 'Productivity/AI',
    'summary': 'Generate and deploy automated actions using AI.',
    'description': """
        AI Automated Action Generator
        =============================
        Allow non-technical users to create, test, and deploy AI-generated Python scripts as Odoo Automated Actions (base_automation).
    """,
    'author': 'LPDE / Antigravity',
    'depends': ['base', 'mail', 'web', 'base_automation'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/ai_agent_menus.xml',
        'views/ai_agent_views.xml',
        'views/ai_agent_task_views.xml',
        'views/ai_agent_tool_views.xml',
        'views/ai_agent_log_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
