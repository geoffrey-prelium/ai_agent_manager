# -*- coding: utf-8 -*-

{
    'name': 'AI Agent Manager',
    'version': '1.0',
    'category': 'Productivity/AI',
    'summary': 'Deploy user-defined AI agents to automate tasks.',
    'description': """
        AI Agent Manager
        ================
        Allow non-technical users to create, configure and deploy AI agents within Odoo.
        - Define custom system prompts.
        - Assign specific Odoo tools for granular access.
        - Trigger agents manually, via cron or webhooks.
        - Human-in-the-loop validation for sensitive actions.
        - Execute and track costs.
    """,
    'author': 'Prelium',
    'depends': ['base', 'mail', 'web'],
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
