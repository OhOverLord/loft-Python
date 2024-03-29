import os
import pygame as pg
from constants import LIGHT_ORANGE


class Button(object):
    """A fairly straight forward button class."""
    def __init__(self, rect=None, color=None, function=None, **kwargs):
        self.rect = pg.Rect(rect)
        self.function = function
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.text = None
        self.process_kwargs(kwargs)
        self.render_text()
        if color:
            self.color = color
        else:
            self.color = LIGHT_ORANGE

        Button.push_sound = pg.mixer.Sound(os.path.join('sound', "push.wav"))
        Button.release_sound = pg.mixer.Sound(os.path.join('sound', "release.wav"))
        Button.hover_sound = pg.mixer.Sound(os.path.join('sound', "hover.wav"))

    def process_kwargs(self, kwargs):
        """Various optional customization you can change by passing kwargs."""
        settings = {"text": None,
                    "font": pg.font.SysFont('Comic Sans MS', 42),
                    "call_on_release": True,
                    "hover_color": None,
                    "clicked_color": None,
                    "font_color": pg.Color("white"),
                    "hover_font_color": None,
                    "clicked_font_color": None,
                    "click_sound": None,
                    "hover_sound": None}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def render_text(self):
        """Pre render the button text."""
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True,color)
            self.text = self.font.render(self.text, True, self.font_color)

    def check_event(self, event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            Button.push_sound.play()
            if not self.call_on_release:
                self.function()

    def on_release(self, event):
        Button.release_sound.play()
        if self.clicked and self.call_on_release:
            self.function()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if Button.hover_sound:
                    Button.hover_sound.play()
        else:
            self.hovered = False

    def update(self, surface):
        """Update needs to be called every frame in the main loop."""
        color = self.color
        text = self.text
        self.check_hover()
        if self.clicked and self.clicked_color:
            color = self.clicked_color
            if self.clicked_font_color:
                text = self.clicked_text
        elif self.hovered and self.hover_color:
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text
        surface.fill(pg.Color("black"), self.rect)
        surface.fill(color, self.rect.inflate(-4, -4))
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text,text_rect)

    def draw(self, screen):
        self.update(screen)
