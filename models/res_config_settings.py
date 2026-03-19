# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ai_agent_openai_api_key = fields.Char(
        related='company_id.ai_agent_openai_api_key',
        readonly=False,
    )
    ai_agent_gemini_api_key = fields.Char(
        related='company_id.ai_agent_gemini_api_key',
        readonly=False,
    )
    ai_agent_claude_api_key = fields.Char(
        related='company_id.ai_agent_claude_api_key',
        readonly=False,
    )
