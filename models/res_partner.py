from odoo import models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        
        # Trigger Agents listening to partner creation
        for record in records:
            tasks = self.env['ai_manager.task'].sudo().search([
                ('trigger_type', '=', 'automated'),
                ('active', '=', True),
            ])
            for task in tasks:
                # Execute all automated tasks for the created contacts
                task.agent_id.with_user(self.env.uid).execute_action(record, task.action_code)

        return records
