"""
ULauncher Generator Extension
"""
import logging
import secrets
from ulauncher.api.client.extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

LOGGER = logging.getLogger(__name__)

class GeneratorExtension(Extension):
    def __init__(self):
        LOGGER.info('Starting Generator Extension')
        super(GeneratorExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def generate_random(self, text):
        final = ""
        length = text
        try:
            length = int(length)
            final = secrets.token_hex(length)
        except:
            length = 0
            final = "Invalid length. Please type a number"

        return [
                ExtensionResultItem(icon='images/key.png',
                                    name=final,
                                    description="Crypto-Random as Hex String",
                                    highlightable=False,
                                    on_enter=CopyToClipboardAction(final))
        ]

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        text = event.get_argument()
        kw = event.get_keyword()
        if kw == "gen":
            items = extension.generate_random(text)
        return RenderResultListAction(items)

if __name__ == "__main__":
    GeneratorExtension().run()

