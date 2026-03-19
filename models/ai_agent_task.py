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
        Calls the LLM with the provided task context and agent prompt.
        """
        self.ensure_one()
        
        prompt = self.action_code or "No specific instruction provided. Please just acknowledge."
        
        # In a real scenario with complex triggers, we would inject Odoo data context here.
        # For this PoC, we send the Action Code directly.
        
        try:
            response_text, tokens = self.agent_id._call_llm(prompt)
            state = 'success'
        except Exception as e:
            response_text = str(e)
            tokens = 0
            state = 'failed'

        # Log execution
        self.env['ai_manager.log'].create({
            'agent_id': self.agent_id.id,
            'task_id': self.id,
            'input_data': f"Manual Trigger:\n{prompt}",
            'state': state,
            'output_data': response_text,
            'cost_tokens': tokens
        })
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Agent Triggered',
                'message': f"Agent {self.agent_id.name} finished execution. Check logs.",
                'type': 'success' if state == 'success' else 'danger',
                'sticky': False,
            }
        }
