# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AiAgentTask(models.Model):
    _name = 'ai_manager.task'
    _description = 'AI Agent Task / Trigger'

    name = fields.Char(string='Task Name', required=True)
    agent_id = fields.Many2one('ai_manager.agent', string='AI Agent', required=True, ondelete='cascade')
    active = fields.Boolean(default=True)

    trigger_type = fields.Selection([
        ('manual', 'Manual Action'),
        ('cron', 'Scheduled (Cron)'),
        ('webhook', 'Webhook'),
    ], string='Trigger Type', default='manual', required=True)

    action_code = fields.Text(
        string='Action Code (Context)',
        help="Provide context or specific instructions to the agent when triggered."
    )

    def action_trigger_agent(self):
        """
        Manually trigger the agent for this task.
        In a real scenario, this would gather context and call the LLM.
        """
        self.ensure_one()
        # Mocking an execution log creation
        self.env['ai_manager.log'].create({
            'agent_id': self.agent_id.id,
            'task_id': self.id,
            'input_data': f"Triggered manually with code: {self.action_code}",
            'state': 'success',
            'output_data': "Simulated response from LLM.",
            'cost_tokens': 150
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Agent Triggered',
                'message': f"Agent {self.agent_id.name} triggered successfully.",
                'type': 'success',
                'sticky': False,
            }
        }
