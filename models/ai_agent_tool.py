# -*- coding: utf-8 -*-
from odoo import models, fields


class AiAgentTool(models.Model):
    _name = 'ai.agent.tool'
    _description = 'AI Agent capability / tool'

    name = fields.Char(string='Tool Name', required=True)
    description = fields.Text(string='Description', required=True)

    tool_type = fields.Selection([
        ('read_odoo', 'Read Odoo Data'),
        ('write_odoo', 'Write Odoo Data'),
        ('web_search', 'Web Search'),
        ('custom_python', 'Custom Python Code')
    ], string='Type', required=True, default='read_odoo')

    target_model_id = fields.Many2one(
        'ir.model', 
        string='Target Model',
        help="If the tool interacts with Odoo, specify the model."
    )

    python_code = fields.Text(
        string='Python Code',
        help="Custom Python code if Type is 'Custom Python Code'."
    )
