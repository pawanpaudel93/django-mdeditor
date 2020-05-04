# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

DEFAULT_CONFIG = {
    'language': 'en',  # zh / en
    'mode': "gfm",
    'value': "",
    'goto_line': True,
    'code_fold': False,
    'watch': True,  # Live preview
    'theme': "",
    'preview_theme': "",
    'editor_theme': "default",
    'line_wrapping': False,  # lineWrapping
    'line_numbers': False,  # lineNumbers,
    'width': '100%',
    'height': 500,
    'auto_height': False,
    'auto_focus': True,
    'placeholder': "",
    'auto_close_tags': True,
    'sync_scrolling': True,
    'tab_size': 4,
    'indent_unit': 4,
    'auto_close_brackets': True,
    'show_trailing_space': True,
    'match_brackets': True,
    'indent_with_tabs': True,
    'style_selected_text': True,
    'match_word_highlight': True,
    'style_active_line': True,
    'dialog_lock_screen': True,
    'dialog_show_mask': True,
    'dialog_draggable': True,
    'dialog_maskbg_color': "#fff",
    'dialog_mask_opacity': 0.1,
    'font_size': "13px",
    
    'plugin_path': "",
    'delay': 300,
    'search_replace': True,

    'image_upload': True,
    'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                             "PNG", "bmp", "BMP", "webp", "WEBP"],
    'image_folder': 'editor',
    'image_upload_url': "/mdeditor/uploads/",
    'cross_domain_upload': False,
    'upload_callbackurl': "",

    'toc': True,
    'tocm': False,
    'toc_title': "",
    'toc_dropdown': False,
    'toc_container': "",
    'toc_startlevel': 1,

    'emoji': True,
    'tex': True,
    'task_list': True,
    'flow_chart': True,
    'sequence': True,
    'preview_code_highlight': True,

    'html_decode': True,
    'page_break': True,
    'at_link': True,
    'email_link': True,

    'toolbar_icons': "full"
}


class MDConfig(dict):

    def __init__(self, config_name='default'):
        self.update(DEFAULT_CONFIG)
        self.set_configs(config_name)

    def set_configs(self, config_name='default'):
        """
        set config item
        :param config_name:
        :return:
        """
        # Try to get valid config from settings.
        configs = getattr(settings, 'MDEDITOR_CONFIGS', None)
        if configs:
            if isinstance(configs, dict):
                # Make sure the config_name exists.
                if config_name in configs:
                    config = configs[config_name]
                    # Make sure the configuration is a dictionary.
                    if not isinstance(config, dict):
                        raise ImproperlyConfigured('MDEDITOR_CONFIGS["%s"] \
                                        setting must be a dictionary type.' %
                                                   config_name)
                    # Override defaults with settings config.
                    self.update(config)
                else:
                    raise ImproperlyConfigured("No configuration named '%s' \
                                    found in your CKEDITOR_CONFIGS setting." %
                                               config_name)
            else:
                raise ImproperlyConfigured('MDEDITOR_CONFIGS setting must be a\
                                dictionary type.')
