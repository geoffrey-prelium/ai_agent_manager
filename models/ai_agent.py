# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AiAgent(models.Model):
    _name = 'ai.agent'
    _description = 'AI Agent'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('archived', 'Archived')
    ], string='Status', default='draft', required=True, tracking=True)

    llm_model = fields.Selection([
        ('gpt-4o', 'GPT-4o (OpenAI)'),
        ('gpt-4o-mini', 'GPT-4o Mini (OpenAI)'),
    ], string='LLM Model', default='gpt-4o', required=True, tracking=True)

    system_prompt = fields.Text(
        string='System Prompt',
        required=True,
        default="You are a helpful AI agent within Odoo.",
        tracking=True
    )

    color = fields.Integer("Color Index")

    tool_ids = fields.Many2many('ai.agent.tool', string='Tools / Capabilities')
    task_ids = fields.One2many('ai.agent.task', 'agent_id', string='Tasks / Triggers')
    log_ids = fields.One2many('ai.agent.log', 'agent_id', string='Execution Logs')

    success_count = fields.Integer(string="Successful Executions", compute='_compute_stats')
    fail_count = fields.Integer(string="Failed Executions", compute='_compute_stats')

    @api.depends('log_ids.state')
    def _compute_stats(self):
        for agent in self:
            agent.success_count = len(agent.log_ids.filtered(lambda l: l.state == 'success'))
            agent.fail_count = len(agent.log_ids.filtered(lambda l: l.state == 'failed'))

    def action_activate(self):
        for record in self:
            record.write({'state': 'active'})

    def action_draft(self):
        for record in self:
            record.write({'state': 'draft'})

    def action_archive(self):
        for record in self:
            record.write({'state': 'archived', 'active': False})

    def action_open_sandbox(self):
        self.ensure_one()
        # Allows to open a wizard or special view to chat with the agent
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Sandbox'),
                'message': _('Sandbox interface will be implemented here.'),
                'type': 'info',
                'sticky': False,
            }
        }
