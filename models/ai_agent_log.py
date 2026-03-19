# -*- coding: utf-8 -*-
from odoo import models, fields


class AiAgentLog(models.Model):
    _name = 'ai.agent.log'
    _description = 'AI Agent Execution Log'
    _order = 'create_date desc'

    agent_id = fields.Many2one('ai.agent', string='Agent', required=True, ondelete='cascade')
    task_id = fields.Many2one('ai.agent.task', string='Trigger Task')

    input_data = fields.Text(string='Input / Context')
    output_data = fields.Text(string='Output / Response')
    
    state = fields.Selection([
        ('pending', 'Pending (Human Validation)'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ], string='Status', default='success', required=True)

    cost_tokens = fields.Integer(string='Tokens Used', default=0)

    def action_validate(self):
        for log in self:
            if log.state == 'pending':
                # Execute the proposed action here
                log.write({'state': 'success'})

    def action_reject(self):
        for log in self:
            if log.state == 'pending':
                log.write({'state': 'failed', 'output_data': log.output_data + "\n\n[REJECTED BY HUMAN]"})
