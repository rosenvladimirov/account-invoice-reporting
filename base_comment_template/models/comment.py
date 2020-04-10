# Copyright 2014 Guewen Baconnier (Camptocamp SA)
# Copyright 2013-2014 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


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

    @api.multi
    def get_value(self, partner_id=False, field_name='text'):
        self.ensure_one()
        lang = None
        if partner_id:
            lang = self.env['res.partner'].browse(partner_id).lang
        return getattr(self.with_context({'lang': lang}), field_name)
