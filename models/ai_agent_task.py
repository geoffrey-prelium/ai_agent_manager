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
        ('automated', 'Automated Action (Model Event)'),
    ], string='Trigger Type', default='manual', required=True)

    action_code = fields.Text(
        string='Action Code (Context)',
        help="Provide context or specific instructions to the agent when triggered."
    )

    def action_trigger_agent(self):
        """
        Manually trigger the agent for this task.
        Calls the LLM execution engine with the provided task context and agent prompt.
        """
        self.ensure_one()
        
        prompt = self.action_code or "No specific instruction provided. Please just acknowledge."
        
        # Test the execution engine. Pass the task itself as the context `record` so the AI has an Odoo object to interact with.
        success = self.agent_id.execute_action(self, prompt)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Agent Triggered',
                'message': f"Agent {self.agent_id.name} finished execution. Check logs.",
                'type': 'success' if success else 'danger',
                'sticky': False,
            }
        }
