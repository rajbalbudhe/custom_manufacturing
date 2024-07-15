odoo.define('custom_manufacturing.custom_scripts', function(require) {
    'use strict';

    var FormView = require('web.FormView');
    var rpc = require('web.rpc');

    FormView.include({
        init: function() {
            this._super.apply(this, arguments);
            console.log('Custom script loaded');

            // Example: Add event listener to a button
            var button = document.querySelector('button');
            if (button) {
                button.addEventListener('click', function() {
                    alert('Button clicked!');
                });
            }
        },

        renderButtons: function($node) {
            this._super($node);
            var self = this;

            if (this.$buttons) {
                var btn = this.$buttons.find('.o_form_button_custom');
                if (btn.length) {
                    btn.on('click', function() {
                        self.do_action({
                            type: 'ir.actions.client',
                            tag: 'reload',
                        });
                    });
                }
            }
        },
    });
});
