# Copyright 2014 Guewen Baconnier (Camptocamp SA)
# Copyright 2013-2014 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


class BaseCommentTemplate(models.Model):
    _name = "base.comment.template"
    _description = "Base comment template"

    name = fields.Char('Comment summary', required=True)
    position = fields.Selection([('before_lines', 'Before lines'),
                                 ('after_lines', 'After lines'),
                                 ('narration', 'Narration')
                                 ],
                                'Position',
                                required=True,
                                default='before_lines',
                                help="Position on document")
    text = fields.Html('Comment', translate=True, required=True)
    short = fields.Char('Short comment', translate=True)
    use = fields.Boolean('Copy to note')
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self: self.env['res.company']._company_default_get('base.comment.template'))

    @api.multi
    def get_value(self, partner_id=False, field_name='text', res=False):
        self.ensure_one()
        lang = None
        if partner_id:
            lang = self.env['res.partner'].browse(partner_id).lang
        source = getattr(self.with_context({'lang': lang}), field_name)
        if res:
            source = safe_eval(source, {'object': res, 'context': self._context})
        return source
