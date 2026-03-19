# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    ai_agent_openai_api_key = fields.Char(string='OpenAI API Key', groups="base.group_system")
