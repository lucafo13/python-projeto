# fonts.py
# Jacob Laframboise
# June 14th, 2018
# This file creates the text surfaces and fonts to be used in the program

import pygame as pg
from settings import *

pg.init()

font_name = pg.font.match_font('arial')


def draw_text(surf, text, size, col, x, y):
    '''A function to render and display text'''
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_text2(surf, text_surface, x, y):
    '''A function to display a pre-rendered surface with text'''
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# make the font object for the title, render the surface
intro_title_font = pg.font.Font(font_name, INTRO_TEXT_SIZE)
intro_title_font_surface = intro_title_font.render(TITLE, True, INTRO_TEXT_COLOUR)

intro_name_font = pg.font.Font(font_name, INTRO_NAME_FONT_SIZE)
intro_name_font_surface = intro_name_font.render('By Jacob Laframboise', True, INTRO_NAME_FONT_COLOUR)
small_name_font = pg.font.Font(font_name, SMALL_NAME_FONT_SIZE)
small_name_font_surface = small_name_font.render('Jacob Laframboise', True, SMALL_NAME_FONT_COLOUR)

small_title_font = pg.font.Font(font_name, SMALL_TITLE_FONT_SIZE)
small_title_font_surface = small_title_font.render(TITLE, True, SMALL_TITLE_FONT_COLOUR)

# make the subfont font object
intro_title_subfont = pg.font.Font(font_name, INTRO_SUBTEXT_SIZE)

# render the surfaces for each subtext
intro_title_subfont_surface = intro_title_subfont.render('Press R for Instructions.', True, INTRO_TEXT_COLOUR)
intro_title_subfont_surface2 = intro_title_subfont.render('OR', True, INTRO_TEXT_COLOUR)
intro_title_subfont_surface3 = intro_title_subfont.render('Press Space to Play!', True, INTRO_TEXT_COLOUR)

# instructions
lines = ['Bem-vindo ao {}.'.format(TITLE),
'O objetivo do jogo é capturar todos os Pokémon.',

'Você move seu treinador para frente com W e para trás com S.',

'Você pode virar para a esquerda e para a direita com A e D.',

'Se o seu treinador encontrar um Pokémon, uma batalha começará.',

'Seu primeiro encontro decidirá qual será o seu Pokémon inicial,',

'e nas próximas batalhas, as coisas ficarão um pouco mais difíceis.',

'Você pode controlar seu Pokémon usando as teclas IJKL como setas,',

'e pode pressionar M para fazer seu Pokémon atacar.',

'Para capturar o Pokémon, vire seu treinador usando A e D,',

'e pressione ESPAÇO para lançar uma Pokébola no Pokémon adversário!',

'Você pode trocar seu Pokémon ativo usando Q.',

'Cuidado, seu Pokémon pode desmaiar se receber ataques demais,',

'e você não pode capturar um Pokémon se já tiver 8 Pokémon, ou se derrotá-lo.',

'Se ocorrer algum erro durante a batalha, pressione 0 para sair dela.',

'Agora vá lá e capture todos!']

# make font object for instructions
intro_inst_font = pg.font.Font(font_name, INTRO_INST_TEXT_SIZE)
# make list of rendered instructions surfaces, one line per surface
instruction_lines_surfaces = [intro_inst_font.render(x, True, INTRO_INST_TEXT_COLOUR) for x in lines]

# make font object for stats
stats_font = pg.font.Font(font_name, MENU_FONT_SIZE)
# make a list of rendered name surfaces for each possible name
name_lines_surfaces = [stats_font.render('Name: ' + x, True, MENU_FONT_COLOUR) for x in POKEMON_LIST]
# repeat for the type
type_lines_surfaces = [stats_font.render('Type: ' + x, True, MENU_FONT_COLOUR) for x in TYPE_LIST]

health_lines = [stats_font.render('Health: {}'.format(str(100 + 20 * x)), True, MENU_FONT_COLOUR) for x in range(41)]
# make a list of rendered lines corresponding to number of kills, which cannot exceed 40
kills_lines = [stats_font.render('Kills: {}'.format(str(x)), True, MENU_FONT_COLOUR) for x in range(41)]
